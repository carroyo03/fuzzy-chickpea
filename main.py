#################################
#    Artificial Intelligence    #
################################# 



# Import numpy for making the matrix, and the files for calculating the distances and the path
import numpy as np
from distances import *
from a_star import *

        

if __name__ == "__main__":
    
    rows = int(input("Insert the number of rows:"))
    cols = int(input("Insert the number of columns:"))
   

    #Creating the matrix with random values and dimensions
    random_matrix = np.zeros((rows, cols), dtype=int)
    n_ones = np.random.randint(20,30)
    indexes_ones = np.random.choice(rows * cols, int(n_ones * .01 * rows * cols), replace=False)
    random_matrix.flat[indexes_ones] = 1
   
   
    #Random start and goal, which are not obstacles
    while True:
        start = [np.random.randint(rows), np.random.randint(cols)]
        goal = [np.random.randint(rows), np.random.randint(cols)]

        if random_matrix[start[0]][start[1]] == 0 and random_matrix[goal[0]][goal[1]] == 0:
            start = tuple(start)
            goal = tuple(goal)
            break
        
    #Type of distance election
    while True:
        distance_type = input("Insert the type of distance you want to be used (manhattan or euclidean):")
        if distance_type == 'manhattan' or 'euclidean':
            print()
            break
        print('Error')
    
    function_ = Functions(random_matrix,start,goal,distance_type)
    a_star1 = a_star(random_matrix,start,goal,distance_type)
    optimal_path = a_star1.path()

    #Cresting the path info
    if optimal_path:
        function_.path_map(random_matrix, optimal_path, start, goal)
        print("- "*cols)
        print("\n[Key]: S: Start | E: Goal | #: Obstacle | .: Free cell | X: Path" )
        print()
        print(f"S:{start}\n")
        print(f"E:{goal}\n")  
    else:
        print("Optimal path not found.")
    
    del a_star1,function_