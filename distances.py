import numpy as np
import heapq

class Functions:


    def __init__(self, matrix,start,goal,distance_type) -> None:
        self.matrix = matrix
        self.start = start
        self.goal = goal
        self.distance_type = distance_type
        pass

    def manhattan_distance(self,a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def euclidean_distance(self,a,b):
        return np.sqrt(pow(a[0]-b[0],2) + pow(a[1]-b[1],2))

    

    def path_map(self,matrix, path, start, goal):

        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if (i, j) == start:
                    print("S", end=" ") # start
                elif (i, j) == goal:
                    print("E", end=" ") # goal
                elif (i, j) in path:
                    print("X", end=" ") # Parte de la ruta
                else:
                    if matrix[i, j] == 0:
                        print(".", end=" ") # Celda libre
                    else:
                        print("#", end=" ") # Obstáculo
            print()