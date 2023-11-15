import numpy as np
import heapq

def distancia_manhattan(p1, p2):
    return np.abs(p1[0] - p2[0]) + np.abs(p1[1] - p2[1])

def a_star(matrix, start, goal):
    movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    n, m = matrix.shape
    open = [(distancia_manhattan(start, goal), 0, start)]  # f(n), g(n), nodo
    close = set()
    padres = {}

    while open:
        _, g_actual, (x, y) = heapq.heappop(open)

        if (x, y) == goal:
            # Reconstruir la ruta y terminar
            camino = [(x, y)]
            while (x, y) in padres:
                (x, y) = padres[(x, y)]
                camino.insert(0, (x, y))
            return camino

        close.add((x, y))

        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and matrix[nx, ny] == 0 and (nx, ny) not in close:
                coste_g = g_actual + 1
                nueva_distancia = coste_g + distancia_manhattan((nx, ny), goal)

                if (nx, ny) not in [n[2] for n in open]:
                    heapq.heappush(open, (nueva_distancia, coste_g, (nx, ny)))
                    padres[(nx, ny)] = (x, y)
                else:
                    indice = next(i for i, (_, _, nodo) in enumerate(open) if nodo == (nx, ny))# Cambiar
                    if coste_g < open[indice][1]:
                        open[indice] = (nueva_distancia, coste_g, (nx, ny))
                        padres[(nx, ny)] = (x, y)

    return None

def imprimir_mapa_con_ruta(matrix, ruta, start, goal):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if (i, j) == start:
                print("S", end=" ")  # start
            elif (i, j) == goal:
                print("E", end=" ")  # goal
            elif (i, j) in ruta:
                print("X", end=" ")  # Parte de la ruta
            else:
                if matrix[i, j] == 0:
                    print(".", end=" ")  # Celda libre
                else:
                    print("1", end=" ")  # Obstáculo
        print()

if __name__ == "__main__":
    # Define el mapa con obstáculos (10x10) usando NumPy
    mapa = np.array([
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
        [0, 0, 1, 1, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])

    start = (0, 0)  # Posición inicial
    goal = (9, 9)  # Posición goal

    ruta_optima = a_star(mapa, start, goal)

    if ruta_optima:
        print("Ruta óptima encontrada:")
        imprimir_mapa_con_ruta(mapa, ruta_optima, start, goal)
    else:
        print("No se encontró una ruta óptima.")


'''
S 1 . . . . . . . . 
X 1 . 1 . . . 1 . . 
X X . 1 . 1 . 1 . . 
. X 1 1 . 1 . 1 . . 
. X X 1 . 1 . 1 . . 
. . X 1 . 1 . . . . 
. . X X X 1 . 1 . . 
. . . 1 X 1 . 1 . . 
. . . 1 X X X 1 . . 
. . . . . . X X X E 
'''

