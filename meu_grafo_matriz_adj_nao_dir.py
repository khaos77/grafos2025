from bibgrafo.grafo_matriz_adj_nao_dir import GrafoMatrizAdjacenciaNaoDirecionado
from bibgrafo.grafo_errors import *


class MeuGrafo(GrafoMatrizAdjacenciaNaoDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê um conjunto (set) de vértices não adjacentes no grafo.
        O conjunto terá o seguinte formato: {X-Z, X-W, ...}
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Um conjunto (set) com os pares de vértices não adjacentes
        '''

        vna = set()
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if len(self.matriz[i][j]) == 0 and i < j:
                    vna.add("{}-{}".format(self.vertices[i].rotulo, self.vertices[j].rotulo))
        return vna

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''

        for vertice in range(len(self.matriz)):
            if len(self.matriz[vertice][vertice]) > 0:
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

        indice = self.indice_do_vertice(self.get_vertice(V))
        grau = 0
        for i in range(len(self.matriz)):
            if i == indice:
                grau += len(self.matriz[indice][i]) * 2
                #caso laço para contar a ida e a volta para o grau
            else:
                grau += len(self.matriz[indice][i])
        return grau


    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz[i])):
                if len(self.matriz[i][j]) > 1:
                    return True
        return False


    def arestas_sobre_vertice(self, V):
        '''
        Provê um conjunto (set) que contém os rótulos das arestas que
        incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Um conjunto com os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoError se o vértice não existe no grafo
        '''
        pass
        if not self.existe_rotulo_vertice(V):
            raise VerticeInvalidoError()

        indice = self.indice_do_vertice(self.get_vertice(V))
        grau = 0
        for i in range(len(self.matriz)):
            if len(self.matriz[i]) > 1:
                return True
        return False


    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        if (not self.ha_laco()) and (not self.ha_paralelas()):
            if len(self.vertices_nao_adjacentes()) == 0:
                return True
        return False