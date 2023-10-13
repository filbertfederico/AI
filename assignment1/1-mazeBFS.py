from collections import deque

def bfs_maze_search(maze, start, end):
    queue = deque([(start, 0)])
    visited = set()
    parent = {}

    while queue:
        current, distance = queue.popleft()
        
        if current == end:
            # Destination reached, reconstruct the path
            path = []
            while current:
                path.append(current)
                current = parent.get(current)
            return list(reversed(path))
        
        visited.add(current)

        # Explore neighboring cells (up, down, left, right)
        for neighbor in get_neighbors(current, maze):
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))
                parent[neighbor] = current


def get_neighbors(cell, maze):
    row, col = cell
    rows, cols = len(maze), len(maze[0])
    neighbors = []
    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < rows and 0 <= c < cols and maze[r][c] != 'W':
            neighbors.append((r, c))

    return neighbors

maze = [
    ['S', 'W', ' ', ' ', ' ', ' ', 'W', ' '],
    [' ', 'W', ' ', 'W', 'W', ' ', 'W', ' '],
    [' ', 'W', ' ', 'W', 'E', ' ', 'W', ' '],
    [' ', 'W', ' ', 'W', 'W', ' ', 'W', ' '],
    [' ', 'W', ' ', 'W', ' ', ' ', ' ', ' '],
    [' ', 'W', ' ', 'W', 'W', 'W', ' ', ' '],
    [' ', 'W', ' ', ' ', 'W', ' ', ' ', ' '],
    [' ', ' ', ' ', 'W', 'W', 'W', ' ', ' '],
    [' ', 'W', ' ', ' ', ' ', ' ', ' ', ' ']
]

start = (0, 0)
end = (4, 5)   

path = bfs_maze_search(maze, start, end)
if path:
    print("Path found:", path)
else:
    print("No path found.")
