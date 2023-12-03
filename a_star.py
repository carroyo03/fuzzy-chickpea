
import heapq
from distances import Functions as func

class a_star:
    def __init__(self, matrix, start, goal, distance_type) -> None:
        # Constructor
        self.matrix = matrix
        self.start = start
        self.goal = goal
        self.distance_type = distance_type
        self.f = func(self.matrix, self.start, goal, distance_type)

    def __del__(self):
        pass

    def path(self):
        # Heuristic: Manhattan distance
        if self.distance_type.startswith('m'):
            heuristic = self.f.manhattan_distance
            neighbourhood = ((-1, 0), (1, 0), (0, -1), (0, 1))
        else:
            # Heuristic: Euclidean distance
            heuristic = self.f.euclidean_distance
            neighbourhood = ((-1, 0), (-1, -1), (-1, 1), (1, 0), (1, 1), (1, -1), (0, -1), (0, 1))

        # Dictionary to store the minimum distance of each cell
        distances = {self.start: 0}

        # Dictionary to store the parent of each cell
        parents = {}

        # Priority queue (current state, cost to current state, remaining heuristic distance to goal)
        priority_queue = [(0, self.start, heuristic(self.start, self.goal))]

        while priority_queue:
            # Pop the element with the smallest priority
            _, current, _ = heapq.heappop(priority_queue)

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
                    # Calculate the tentative distance from the start to the neighbor
                    tentative_distance = distances[current] + 1

                    # Check if the tentative distance is shorter than the current known distance to the neighbor
                    if next_node not in distances or tentative_distance < distances[next_node]:
                        # Update the distance to the neighbor
                        distances[next_node] = tentative_distance

                        # Calculate the priority for the neighbor in the priority queue
                        priority = tentative_distance + heuristic(next_node, self.goal)

                        # Push the neighbor and its priority into the priority queue
                        heapq.heappush(priority_queue, (priority, next_node, heuristic(next_node, self.goal)))

                        # Set the current cell as the parent of the neighbor
                        parents[next_node] = current


        return None
