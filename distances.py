import numpy as np

class Functions:
    """Contains various functions related to pathfinding on a 2D matrix."""

    def __init__(self, matrix, start, goal, distance_type):
        """
        Constructor for the Functions class.

        Parameters:
        - matrix (numpy.ndarray): The 2D matrix representing the environment.
        - start (tuple): The starting point (row, column) on the matrix.
        - goal (tuple): The goal point (row, column) on the matrix.
        - distance_type (str): The type of distance to be used (e.g., 'manhattan' or 'euclidean').

        Authors: Carlos Arroyo and Gabriel Nassri
        """
        self.matrix = matrix
        self.start = start
        self.goal = goal
        self.distance_type = distance_type

    def __del__(self):
        """Destructor for the Functions class."""
        pass

    def manhattan_distance(self, a, b):
        """
        Calculate the Manhattan distance between two points.

        Parameters:
        - a (tuple): The coordinates of the first point (row, column).
        - b (tuple): The coordinates of the second point (row, column).

        Returns:
        - int: The Manhattan distance between points a and b.

        Author: Juan Carlos Estefanía
        """
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def euclidean_distance(self, a, b):
        """
        Calculate the Euclidean distance between two points.

        Parameters:
        - a (tuple): The coordinates of the first point (row, column).
        - b (tuple): The coordinates of the second point (row, column).

        Returns:
        - float: The Euclidean distance between points a and b.

        Author: Carlos Arroyo
        """
        return np.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))

    def path_map(self, matrix, path, start, goal):
        """
        Display a visual representation of the path on the matrix.

        Parameters:
        - matrix (numpy.ndarray): The 2D matrix representing the environment.
        - path (list): List of coordinates representing the path.
        - start (tuple): The starting point (row, column) on the matrix.
        - goal (tuple): The goal point (row, column) on the matrix.

        Authors: Juan Carlos Estefanía and Gabriel Nassri
        """
        for i in range(matrix.shape[0]):
            for j in range(matrix.shape[1]):
                if (i, j) == start:
                    print("S", end=" ")  # Start
                elif (i, j) == goal:
                    print("E", end=" ")  # End
                elif (i, j) in path:
                    print("X", end=" ")  # Part of the path
                else:
                    if matrix[i, j] == 0:
                        print(".", end=" ")  # Free cell
                    else:
                        print("#", end=" ")  # Obstacle
            print()
