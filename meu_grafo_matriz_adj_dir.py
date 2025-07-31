from bibgrafo.grafo_matriz_adj_dir import *
from bibgrafo.grafo_errors import *
from copy import deepcopy

class MeuGrafo(GrafoMatrizAdjacenciaDirecionado):

    def vertices_nao_adjacentes(self):
        '''
        Provê uma lista de vértices não adjacentes no grafo. A lista terá o seguinte formato: [X-Z, X-W, ...]
        Onde X, Z e W são vértices no grafo que não tem uma aresta entre eles.
        :return: Uma lista com os pares de vértices não adjacentes
        '''
        pass

    def ha_laco(self):
        '''
        Verifica se existe algum laço no grafo.
        :return: Um valor booleano que indica se existe algum laço.
        '''
        pass


    def grau_entrada(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def grau_saida(self, V=''):
        '''
        Provê o grau do vértice passado como parâmetro
        :param V: O rótulo do vértice a ser analisado
        :return: Um valor inteiro que indica o grau do vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def ha_paralelas(self):
        '''
        Verifica se há arestas paralelas no grafo
        :return: Um valor booleano que indica se existem arestas paralelas no grafo.
        '''
        pass

    def arestas_sobre_vertice(self, V):
        '''
        Provê uma lista que contém os rótulos das arestas que incidem sobre o vértice passado como parâmetro
        :param V: O vértice a ser analisado
        :return: Uma lista os rótulos das arestas que incidem sobre o vértice
        :raises: VerticeInvalidoException se o vértice não existe no grafo
        '''
        pass

    def eh_completo(self):
        '''
        Verifica se o grafo é completo.
        :return: Um valor booleano que indica se o grafo é completo
        '''
        pass

    def warshall(self):
        '''
        Provê a matriz de alcançabilidade de Warshall do grafo
        :return: Uma lista de listas que representa a matriz de alcançabilidade de Warshall associada ao grafo
        '''

        alcan = deepcopy(self.matriz)
        for i in range(len(alcan)):
            for j in range(len(alcan)):
                if len(alcan[i][j]) > 0:
                    alcan[i][j] = True
                else:
                    alcan[i][j] = False
        for i in range(len(alcan)):
            for j in range(len(alcan)):
                if alcan[j][i] == True:
                    for k in range(len(alcan)):
                        if alcan[j][k] == True or alcan[i][k] == True:
                            alcan[j][k] = True
        return alcan

'''
        matriz_clone = deepcopy(self.matriz)
        n = len(matriz_clone)

        for j in range(n):  # j é o vértice intermediário
            for i in range(n):
                if matriz_clone[i][j]:
                    for k in range(n):
                        matriz_clone[i][k] = matriz_clone[i][k] or matriz_clone[j][k]

        return matriz_clone '''
