from bibgrafo.grafo_lista_adj_nao_dir import GrafoListaAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoListaAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um objeto do tipo set que contém os pares de vértices não adjacentes
        '''
        n = len(self.vertices)
        nao_adjacentes = set()

#conjunto dict de vertices adjacentes para comparar com as arestas, resultando os nao adj
        adjacentes = {v.rotulo: set() for v in self.vertices}
#'A':set(),'B':set()
        for aresta in self.arestas.values():
            adjacentes[aresta.v1.rotulo].add(aresta.v2.rotulo)
            adjacentes[aresta.v2.rotulo].add(aresta.v1.rotulo)
#adiciona no conj o vertice de cada aresta, sendo v1 e v2 vertices de cada aresta
        for i in range(n):
#percorre cada vertice do grafo
            rotulo_i = self.vertices[i].rotulo
#rotulo_i recebe o rotulo de cada vertice
            for j in range(i + 1, n):
                rotulo_j = self.vertices[j].rotulo
                if rotulo_j not in adjacentes[rotulo_i]:
                    nao_adjacentes.add(f"{rotulo_i}-{rotulo_j}")
#se o rotulo analisado nao estiver nos adjacentes, certamente é nao adjacente
        return nao_adjacentes

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        for a in self.arestas.values():
            if a.v1 == a.v2:
                return True
        return False

    def grau(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError()

        grau = 0
        for a in self.arestas:
            if self.arestas[a].v1.rotulo == V:
                grau += 1
            if self.arestas[a].v2.rotulo == V:
                grau += 1
        return grau

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for a in self.arestas.values():
            for b in self.arestas.values():
                if a.rotulo != b.rotulo and a == b:
                    return True
        return False

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: Um string com o rótulo do vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
#se o vertice nao existir no grafo
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError()

        lista = []
        for a in self.arestas:
#pega cada chave(nome de cada aresta) e se ela for igual a aresta de v1 ou v2, adiciona a aresta analisada na lista
            if self.arestas[a].v1.rotulo == V or self.arestas[a].v2.rotulo == V:
                lista.append(self.arestas[a].rotulo)
        return set(lista)
    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if self.ha_laco():
            return False

        n = len(self.vertices)

        if len(self.arestas) != n * (n - 1) // 2:
            return False

        for vertice in self.vertices:
            if self.grau(vertice.rotulo) != n - 1:
                return False

        return True

    def dfs(self, V=''):
        grafo_dfs = MeuGrafo()  # Grafo formado após a DFS
        grafo_dfs.adiciona_vertice(V)  # Incluindo no grafo resposta nosso primeiro vértice
        return self.dfs_rec(V, grafo_dfs)

    def dfs_rec(self, V, grafo_dfs):
        arestas = sorted(self.arestas_sobre_vertice(V))  # Aqui estamos acessando os rótulos das arestas, pois essa função retorna um conjunto de rotulos
        for a in arestas:
            if not grafo_dfs.existe_rotulo_aresta(a):  # Verifica se a aresta não está no grafo_dfs
                ares = self.get_aresta(a)  # Pegando o objeto aresta caso ela não esteja no grafo_dfs
                if ares.v1.rotulo == V:  # Verfica os vertices que a aresta incide (Nao queremos o que chamou a recursão)
                    proxV = ares.v2.rotulo
                else:
                    proxV = ares.v1.rotulo
                if grafo_dfs.existe_rotulo_vertice(proxV):
                    continue
                else:
                    grafo_dfs.adiciona_vertice(proxV)
                    grafo_dfs.adiciona_aresta(ares)
                    self.dfs_rec(proxV, grafo_dfs)
            else:
                continue
        return grafo_dfs

    def bfs(self, v=''):
        grafo_bfs = MeuGrafo()
        grafo_bfs.adiciona_vertice(v)
        return self.bfs_rec(v, grafo_bfs)

    def bfs_rec(self, v, grafo_bfs):
        arestas = sorted(self.arestas_sobre_vertice(v))
        v_visit = []
        for a in arestas:
            if not grafo_bfs.existe_rotulo_aresta(a):
                are = self.get_aresta(a)
                if are.v1.rotulo == v:
                    proxv = are.v2.rotulo

                else:
                    proxv = are.v1.rotulo

                if not grafo_bfs.existe_rotulo_vertice(proxv):
                    grafo_bfs.adiciona_vertice(proxv)
                    grafo_bfs.adiciona_aresta(are)
                    v_visit.append(proxv)

                else:
                    continue
            else:
                continue
        for ve in v_visit:
            self.bfs_rec(ve, grafo_bfs)
        return grafo_bfs

    def ha_ciclo(self):
        def ha_ciclo_rec(V):
            caminho.append(V)
            arestas = sorted(self.arestas_sobre_vertice(V))
            for a in arestas:
                if a not in caminho:
                    ares = self.get_aresta(a)
                    if ares.v1.rotulo == V:
                        proxV = ares.v2.rotulo
                    else:
                        proxV = ares.v1.rotulo
                    if proxV in caminho:
                        caminho.append(a)
                        caminho.append(proxV)
                        break
                    else:
                        caminho.append(ares.rotulo)
                        result = ha_ciclo_rec(proxV)
                    if result:
                        caminho.pop()
                        return result
            i = caminho.index(caminho[-1])
            if i != len(caminho) - 1:
                return caminho[i:]
            for i in range(2):
                if len(caminho) > 0:
                    caminho.pop()
            return False
        for vertice in self.vertices:
            caminho = []
            result = ha_ciclo_rec(vertice.rotulo)
            if result:
                return result
        return False

    def eh_conexo(self):
        #caminho entre os vertices
        dfs = self.dfs(sorted(self.vertices)[0])
        return len(self.vertices) == len(dfs.vertices)

    def ha_ciclo(self):
        vert = self.vertices[0].rotulo
        dfs = self.dfs(vert)
        return self != dfs

    def eh_arvore(self):
        if not self.eh_conexo() or self.ha_ciclo():
            return False
        folha = [v.rotulo for v in self.vertices if self.grau(v.rotulo) == 1]
        return folha

    def eh_bipartido(self):
        #todos os vertices de 0 se conectam com cada um de 1
        cor = {}
        for v in self.vertices:
            rotulo = v.rotulo
            if rotulo not in cor:
                fila = list()
                fila.append(rotulo)
                cor[rotulo] = 0  # cor 0
                while fila:
                    atual = fila.pop()
                    for aresta in self.arestas_sobre_vertice(atual):
                        v1 = self.arestas[aresta].v1.rotulo
                        v2 = self.arestas[aresta].v2.rotulo
                        vizinho = v2 if atual == v1 else v1

                        if vizinho not in cor:
                            cor[vizinho] = 1 - cor[atual]
                            fila.append(vizinho)
                        elif cor[vizinho] == cor[atual]:
                            return False
        return True