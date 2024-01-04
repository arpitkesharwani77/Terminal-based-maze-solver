import random
from queue import Queue
# Define constants for maze elements

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
END_COLOR = "\033[0m" 


WALL = f'{RED}▓{END_COLOR}'
OPEN_SPACE = f'{BLUE}◌{END_COLOR}'
START = 'S'
END = 'E'
PATH = f'{GREEN}◍{END_COLOR}'


def generate_maze(n, wall_percentage):
    maze = [[OPEN_SPACE] * n for _ in range(n)]
    # Add walls
    num_walls = int(n * n * wall_percentage / 100)
    for _ in range(num_walls):
        row, col = random.randint(0, n - 1), random.randint(0, n - 1)
        maze[row][col] = WALL
    # Set start and end points
    maze[0][0] = START
    maze[n - 1][n - 1] = END
    return maze
  
def print_maze(maze):
    for row in maze:
        print(" ".join(row))

def find_path(maze):
    start = (0, 0)
    end = (len(maze) - 1, len(maze[0]) - 1)
    visited = set()
    queue = Queue()
    queue.put((start, [start]))
    while not queue.empty():
        current, path = queue.get()
        if current == end:
            return path
        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.put((neighbor, path + [neighbor]))
    return None        