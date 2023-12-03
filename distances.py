import numpy as np
import heapq

class Functions:
    """_summary_
    """    

    def __init__(self, matrix,start,goal,distance_type) -> None:
        #Constructor
        self.matrix = matrix
        self.start = start
        self.goal = goal
        self.distance_type = distance_type
        pass

    def __del__(self):
        pass

    #Defining the Manhattan Distance
    def manhattan_distance(self,a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    #Defining the Euclidean Distance
    def euclidean_distance(self,a,b):
        return np.sqrt(pow(a[0]-b[0],2) + pow(a[1]-b[1],2))

    
    #Defining the path map
    def path_map(self,matrix, path, start, goal):
        #
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if (i, j) == start:
                    print("S", end=" ") # start
                elif (i, j) == goal:
                    print("E", end=" ") # goal
                elif (i, j) in path:
                    print("X", end=" ") # Part of path
                else:
                    if matrix[i, j] == 0:
                        print(".", end=" ") # Free cell
                    else:
                        print("#", end=" ") # Obstacle
            print()