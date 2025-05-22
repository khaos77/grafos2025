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
        '''
        DFS recursivo que retorna uma árvore DFS
        :param V: Vértice inicial (rótulo)
        :return: Novo grafo representando a árvore DFS
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError()

        # Cria nova árvore DFS
        self.arvore_dfs = MeuGrafo()
        self.visitados_dfs = set()

        # Adiciona o vértice inicial
        self.arvore_dfs.adiciona_vertice(V)
        self.visitados_dfs.add(V)

        # Chama a função recursiva
        self._dfs_recursivo(V)

        return self.arvore_dfs

    def _dfs_recursivo(self, atual):
        '''
        Função auxiliar recursiva para o DFS
        :param atual: Vértice atual sendo visitado (rótulo)
        '''
        # Percorre todas as arestas do vértice atual
        for aresta_rotulo in self.arestas_sobre_vertice(atual):
            aresta = self.arestas[aresta_rotulo]

            # Determina o vértice oposto
            if aresta.v1.rotulo == atual:
                vizinho = aresta.v2.rotulo
            else:
                vizinho = aresta.v1.rotulo

            # Se o vizinho não foi visitado
            if vizinho not in self.visitados_dfs:
                # Adiciona o vértice e a aresta na árvore
                self.arvore_dfs.adiciona_vertice(vizinho)
                self.arvore_dfs.adiciona_aresta(aresta_rotulo, atual, vizinho)
                self.visitados_dfs.add(vizinho)

                # Chamada recursiva
                self._dfs_recursivo(vizinho)

    def bfs_recursivo(self, V=''):
        '''
        BFS recursivo a partir do vértice V.
        Retorna um novo grafo representando a árvore BFS.
        '''
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError()

        arvore_bfs = MeuGrafo()
        visitados = {V}
        fila = [V]
        arvore_bfs.adiciona_vertice(V)

        def bfs_helper(fila, index=0):
            if index >= len(fila):
                return

            atual = fila[index]

            # Visita todos os vizinhos do vértice atual
            for aresta in sorted(self.arestas_sobre_vertice(atual)):
                aresta_obj = self.arestas[aresta]
                vizinho = aresta_obj.v2.rotulo if aresta_obj.v1.rotulo == atual else aresta_obj.v1.rotulo

                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)
                    arvore_bfs.adiciona_vertice(vizinho)
                    arvore_bfs.adiciona_aresta(aresta, atual, vizinho)

            # Chama recursivamente para o próximo vértice na fila
            bfs_helper(fila, index + 1)

        bfs_helper(fila)
        return arvore_bfs
