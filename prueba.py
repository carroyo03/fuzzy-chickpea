import numpy as np
import heapq

####

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
    """_summary_

    Args:
        matrix (_type_): _description_
        ruta (_type_): _description_
        start (_type_): _description_
        goal (_type_): _description_
    """
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
                    print("#", end=" ")  # Obstáculo
        print()

if __name__ == "__main__":
    # Define la matriz con obstáculos (10x10) usando NumPy
    rows = 10
    cols = 10

    
    random_matrix = np.zeros((rows, cols), dtype=int)
    numero_de_unos = np.random.randint(20,30)
    indices_unos = np.random.choice(rows * cols, numero_de_unos, replace=False)
    random_matrix.flat[indices_unos] = 1
   
    
    print(random_matrix)
    
    '''
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
'''
    start = {'x': np.random.randint(10),'y': np.random.randint(10)} # Posición inicial
    goal = {'x': np.random.randint(10),'y': np.random.randint(10)} # Posición goal

    




    while random_matrix[start['x']][start['y']] == 1 or random_matrix[goal['x']][goal['y']] == 1:
        start = {'x': np.random.randint(10),'y': np.random.randint(10)} 
        goal = {'x': np.random.randint(10),'y': np.random.randint(10)}

    ruta_optima = a_star(random_matrix, start, goal)

    if ruta_optima:
        print("Ruta óptima encontrada:")
        imprimir_mapa_con_ruta(random_matrix, ruta_optima, start, goal)
    else:
        print("No se encontró una ruta óptima.")
        print(start,goal)