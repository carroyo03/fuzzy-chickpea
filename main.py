#################################
#    Artificial Intelligence    #
#        A* Algorithm           #
#          2023/24              #
################################# 

"""
This project implements pathfinding using the A* algorithm in a 2D matrix environment. 
The matrix is randomly generated with obstacles, and the A* algorithm finds the optimal path 
from a randomly selected start point to a goal point. The user can choose between Manhattan 
and Euclidean distance heuristics. The project is organized into three files:

 distances.py:
 - Defines a Functions class with functions for pathfinding, including Manhattan and Euclidean distances.
 - Provides a method to display a visual representation of a path on the matrix.

 a_star.py:
 - Implements the A* algorithm for finding the optimal path on a 2D matrix.
 - Utilizes the Functions class from distances.py for distance calculations.

 main.py:
 - Generates a random matrix with obstacles and user-specified dimensions.
 - Selects random start and goal positions ensuring they are not obstacles.
 - Allows the user to choose between Manhattan and Euclidean distances for path calculation.
 - Uses the A* algorithm to find the optimal path and displays the results on the console.

Authors: Carlos Arroyo, Gabriel Nassri, and Juan Carlos Estefanía
"""

# Import numpy for making the matrix, time for "sleeping" the output and making it more user-friendly, and the files for calculating the distances and the path
import numpy as np
import time
from distances import Functions
from a_star import AStar

        

if __name__ == "__main__":
    """

    This program generates a random matrix, selects a start and goal position,
    and uses the A* algorithm to find the optimal path. The results are then
    displayed on the console.

    Parameters:
    - None

    Returns:
    - None

    Authors: Carlos Arroyo, Gabriel Nassri and Juan Carlos Estefanía
    """
    
    # User input of the dimensions of the matrix
    rows = int(input("Insert the number of rows:"))
    cols = int(input("Insert the number of columns:"))

    print("Creating a random matrix with obstacles...")
    time.sleep(2)
    # Creating the matrix with random values and dimensions
    random_matrix = np.zeros((rows, cols), dtype=int)

    # Determine the number of obstacles by generating a random percentage 
    # between 20 and 30, multiplying it by the dimensions and converting it
    # an integer.
    n_obstacles = int(np.random.randint(20,30) * .01 * rows * cols)
    # Randomly select unique indexes to represent obstacle positions in the flattened matrix.
    indexes_obstacles = np.random.choice(rows * cols, n_obstacles, replace=False)
    # Set the elements at the randomly chosen obstacle indexes to 1 in the matrix.
    random_matrix.flat[indexes_obstacles] = 1
   
    # Random start and goal of the path
    while True:
        start = [np.random.randint(rows), np.random.randint(cols)]
        goal = [np.random.randint(rows), np.random.randint(cols)]

        # Checking start and goal are not obstacles.
        # In case they are not, they will be converted into tuples,
        # as the other path points.

        if random_matrix[start[0]][start[1]] == 0 and random_matrix[goal[0]][goal[1]] == 0:
            start = tuple(start)
            goal = tuple(goal)
            break
        
    # Choose the type of distance for path calculation:
    # Choose between Manhattan and Euclidean distance based on data characteristics:
    # - Use Euclidean distance for continuous data with important value differences.
    # - Opt for Manhattan distance for discrete data or when differences in one dimension are crucial.
    # - Computational efficiency: Euclidean involves square root, Manhattan is often computationally cheaper.
    while True:
        distance_type = input("Choose the distance metric for pathfinding (Enter 'manhattan' or 'euclidean'): ")
        time.sleep(2.5)
        if distance_type in ['manhattan','euclidean']:
            print()
            break
        print('Invalid input. Please choose either "manhattan" or "euclidean".')
    # Create instances of Functions and AStar classes
    function_ = Functions(random_matrix, start, goal, distance_type)
    a_star1 = AStar(random_matrix, start, goal, distance_type)
    optimal_path = a_star1.path()


    # Creating the path visualization
    if optimal_path:
        function_.path_map(random_matrix, optimal_path, start, goal)
        print("- "*cols)
        print("\n[Key]: S: Start | E: Goal | #: Obstacle | .: Free cell | X: Path" )
        print()
        print(f"S:{start}\n")
        print(f"E:{goal}\n")  
    else:
        print("Optimal path not found.")
    
    # Cleaning up instances
    del a_star1, function_
