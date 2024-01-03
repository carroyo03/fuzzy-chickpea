# Pathfinding Algorithm using A* in a 2D Matrix

This Python program demonstrates the A* algorithm for finding an optimal path in a randomly generated 2D matrix. The code is organized into three main files: `distances.py`, `a_star.py`, and `main.py`.

## Files:

1. **distances.py:**
   - Contains a `Functions` class with methods for pathfinding-related functions.
   - Includes Manhattan and Euclidean distance calculations, along with a function to display a visual representation of a path on the matrix.

2. **a_star.py:**
   - Implements the A* algorithm within the `AStar` class for pathfinding on a 2D matrix.
   - Utilizes the `Functions` class from `distances.py` for distance calculations and path visualization.

3. **main.py:**
   - The main program file where the user interacts with the application.
   - Prompts the user for matrix dimensions, generates a random matrix with obstacles, and selects random start and goal positions.
   - Allows the user to choose between Manhattan and Euclidean distances for path calculation.
   - Uses the A* algorithm to find the optimal path and displays the matrix with the path on the console.

## Instructions:

1. Run `main.py` to execute the program.
2. Input the number of rows and columns for the matrix when prompted.
3. The program generates a random matrix with obstacles and visually displays the optimal path using the A* algorithm.
4. Choose between Manhattan and Euclidean distances for path calculation.
5. The result, including the matrix with the path and key information, is printed on the console.

## Authors:

- Carlos Arroyo
- Gabriel Nassri
- Juan Carlos Estefanía
