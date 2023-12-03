import heapq
from distances import Functions as func

class a_star:
    def __init__(self,matrix,start,goal,distance_type) -> None:
        self.matrix = matrix
        self.start = start
        self.goal = goal
        self.distance_type = distance_type
        self.f = func(self.matrix,self.start,goal,distance_type)
        pass

    def path(self):


            # Heurística: distancia de Manhattan
            if self.distance_type.startswith('m'):
                heuristic = self.f.manhattan_distance
                neighbourhood = ((-1, 0), (1, 0), (0, -1), (0, 1))
            else:
                heuristic = self.f.euclidean_distance
                neighbourhood = ((-1, 0), (-1,-1),(-1,1),(1, 0),(1,1),(1,-1), (0, -1), (0, 1))

            # Diccionario para guardar la distancia mínima de cada celda
            distances = {self.start: 0}

            # Diccionario para guardar el padre de cada celda
            parents = {}

            # Cola de prioridad (estado actual, costo hasta el estado actual, heurística de la distancia restante al estado actual)
            priority_queue = [(0, self.start, heuristic(self.start,self.goal))]

            while priority_queue:
                _, current, _ = heapq.heappop(priority_queue)

                if current == self.goal:
                    path = []
                    while current in parents:
                        path.append(current)
                        current = parents[current]
                    return path[::-1]

                for dx, dy in neighbourhood:
                    next_node = (current[0] + dx, current[1] + dy)

                    if (
                        0 <= next_node[0] < self.matrix.shape[0]
                        and 0 <= next_node[1] < self.matrix.shape[1]
                        and self.matrix[next_node[0], next_node[1]] == 0
                    ):
                        tentative_distance = distances[current] + 1

                        if next_node not in distances or tentative_distance < distances[next_node]:
                            distances[next_node] = tentative_distance
                            priority = tentative_distance + heuristic(next_node, self.goal)
                            heapq.heappush(priority_queue, (priority, next_node, heuristic(next_node, self.goal)))
                            parents[next_node] = current

            return None