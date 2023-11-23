import heapq
import numpy as np

def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(matrix, start, goal):

    # Heurística: distancia de Manhattan
    heuristic = manhattan_distance

    # Diccionario para guardar la distancia mínima de cada celda
    distances = {start: 0}

    # Diccionario para guardar el padre de cada celda
    parents = {}

    # Cola de prioridad (estado actual, costo hasta el estado actual, heurística de la distancia restante al estado actual)
    queue = [(0, start, heuristic(start, goal))]

    while queue:
        _, current, _ = heapq.heappop(queue)

        if current == goal:
            path = []
            while current in parents:
                path.append(current)
                current = parents[current]
            return path[::-1]

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            next_node = (current[0] + dx, current[1] + dy)

            if (
                0 <= next_node[0] < matrix.shape[0]
                and 0 <= next_node[1] < matrix.shape[1]
                and matrix[next_node[0], next_node[1]] == 0
            ):
                tentative_distance = distances[current] + 1

                if next_node not in distances or tentative_distance < distances[next_node]:
                    distances[next_node] = tentative_distance
                    priority = tentative_distance + heuristic(next_node, goal)
                    heapq.heappush(queue, (priority, next_node, heuristic(next_node, goal)))
                    parents[next_node] = current

    return None

def imprimir_mapa_con_ruta(matrix, ruta, start, goal):
    #ruta = ruta + [start]
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if (i, j) == start:
                print("S", end=" ") # start
            elif (i, j) == goal:
                print("E", end=" ") # goal
            elif (i, j) in ruta:
                print("X", end=" ") # Parte de la ruta
            else:
                if matrix[i, j] == 0:
                    print(".", end=" ") # Celda libre
                else:
                    print("#", end=" ") # Obstáculo
        print()

        

if __name__ == "__main__":
    # Define la matriz con obstáculos (10x10) usando NumPy
    rows = np.random.randint(10,20)
    cols = np.random.randint(10,20)

    
    random_matrix = np.zeros((rows, cols), dtype=int)
    numero_de_unos = np.random.randint(20,30)
    indices_unos = np.random.choice(rows * cols, int(numero_de_unos * .01 * rows * cols), replace=False)
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
    '''start = {'x': np.random.randint(10),'y': np.random.randint(10)} # Posición inicial
    goal = {'x': np.random.randint(10),'y': np.random.randint(10)} # Posición goal'''

    while True:
        start = [np.random.randint(10), np.random.randint(10)]
        goal = [np.random.randint(10), np.random.randint(10)]

        if random_matrix[start[0]][start[1]] == 0 and random_matrix[goal[0]][goal[1]] == 0:
            start = tuple(start)
            goal = tuple(goal)
            break

    ruta_optima = a_star(random_matrix, start, goal)

    if ruta_optima:
        print("Ruta óptima encontrada:")
        imprimir_mapa_con_ruta(random_matrix, ruta_optima, start, goal)
    else:
        print("No se encontró una ruta óptima.")
        print(start,goal)