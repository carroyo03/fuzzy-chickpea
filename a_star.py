from heapq import heappop,heappush
from distances import Functions as func

class AStar:
    """Implements the A* algorithm for pathfinding on a 2D matrix."""

    def __init__(self, matrix, start, goal, distance_type):
        """
        Constructor for the AStar class.

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
        """Destructor for the AStar class."""
        pass

    def path(self):
        """
        Find the optimal path from the start to the goal using the A* algorithm.

        Returns:
        - list or None: List of coordinates representing the optimal path, or None if no path is found.

        Authors: Carlos Arroyo, Juan Carlos Estefanía and Gabriel Nassri
        """
        functions = func(self.matrix, self.start, self.goal, self.distance_type)

        # Heuristic: Manhattan distance
        if self.distance_type.startswith('m'):
            heuristic = functions.manhattan_distance
            neighbourhood = ((-1, 0), (1, 0), (0, -1), (0, 1))
        else:
            # Heuristic: Euclidean distance
            heuristic = functions.euclidean_distance
            neighbourhood = ((-1, 0), (-1, -1), (-1, 1), (1, 0), (1, 1), (1, -1), (0, -1), (0, 1))

        # Dictionary to store the minimum distance of each cell
        distances = {self.start: 0}

        # Dictionary to store the parent of each cell
        parents = {}

        # Openset 
        #(cost to current state, current state, remaining heuristic distance to goal)
        # Each element in the openset is a tuple.
        openset = [(0, self.start, heuristic(self.start, self.goal))]

        # Closedset
        # Set of the nodes completely explored
        closedset = set()

        while openset:
            # Pop the node with the smallest cost
            _, current, _ = heappop(openset)

            # In case the current node is completely explored, 
            # continue with the next node with the smallest cost
            if current in closedset:
                continue
            
            if current == self.goal:
                # Reconstruct the path from goal to start
                path = []
                while current in parents:
                    path.append(current)
                    current = parents[current]
                return path[::-1]
            
            

            for dx, dy in neighbourhood:
                # Explore neighbors
                next_node = (current[0] + dx, current[1] + dy)

                if (
                    0 <= next_node[0] < self.matrix.shape[0]
                    and 0 <= next_node[1] < self.matrix.shape[1]
                    and self.matrix[next_node[0], next_node[1]] == 0
                ):
                    # Calculate the distance from the start node to the neighbor
                    cost_distance = distances[current] + 1

                    # Check if this distance is shorter than the current known distance to the neighbor
                    if next_node not in distances or cost_distance < distances[next_node]:
                        # Update the distance to the neighbor
                        distances[next_node] = cost_distance

                        # Calculate the cost for the neighbor in the openset
                        total_cost = cost_distance + heuristic(next_node, self.goal)

                        # Push the neighbor and its cost into the openset
                        heappush(openset, (total_cost, next_node, heuristic(next_node, self.goal)))

                        # Set the current cell as the parent of the neighbor
                        parents[next_node] = current

            # The current node is completely explored
            closedset.add(current)

        return None

