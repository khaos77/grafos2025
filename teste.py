from atividades_grafos.meu_grafo_matriz_adj_dir import MeuGrafo

grafo_simple = MeuGrafo()

grafo_simple.adiciona_vertice("A")
grafo_simple.adiciona_vertice("B")
grafo_simple.adiciona_vertice("C")

grafo_simple.adiciona_aresta("a1", "A", "C")
grafo_simple.adiciona_aresta("a2", "C", "A")
grafo_simple.adiciona_aresta("a3", "A", "B")

print("Grafo Simple Matriz:")
for i in range(len(grafo_simple.matriz)):
    for j in range(len(grafo_simple.matriz)):
        if grafo_simple.matriz[i][j]:
            print(f"[1]", end='')

        else:
            print("[0]", end='')

    print()

print("\nGrafo Simple Warshall:")

for i in range(len(grafo_simple.matriz)):
    for j in range(len(grafo_simple.matriz)):
        if grafo_simple.warshall()[i][j]:
            print(f"[1]", end='')

        else:
            print("[0]", end='')

    print()