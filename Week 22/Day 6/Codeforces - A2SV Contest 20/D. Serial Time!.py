def solve():
    """
    Solves the Cereal Guy's friend Serial Guy problem.
    """
    k, n, m = map(int, input().split())
    input()  # Consume the blank line after dimensions

    plate = []
    for _ in range(k):
        layer = [list(input()) for _ in range(n)]
        plate.append(layer)
        if _ < k - 1:
            input()  # Consume the blank line between layers

    x, y = map(int, input().split())

    # Adjust to 0-based indexing for list access
    start_x = x - 1
    start_y = y - 1
    start_z = 0  # Water starts at the top layer (layer 0)

    # A queue for the Breadth-First Search (BFS)
    q = [(start_z, start_x, start_y)]

    # A set to keep track of visited cells to avoid cycles and redundant checks
    visited = set()
    visited.add((start_z, start_x, start_y))

    count = 0

    while q:
        z, r, c = q.pop(0)

        # This cell can be filled with water
        count += 1

        # Possible moves in 6 directions (up, down, left, right, forward, backward)
        # (dz, dr, dc) corresponds to changes in layer, row, and column
        moves = [
            (0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0),  # Same layer
            (1, 0, 0), (-1, 0, 0)  # Different layers
        ]

        for dz, dr, dc in moves:
            nz, nr, nc = z + dz, r + dr, c + dc

            # Check if the new position is within the plate's boundaries
            if 0 <= nz < k and 0 <= nr < n and 0 <= nc < m:
                # Check if the new cell is empty ('.') and hasn't been visited yet
                if plate[nz][nr][nc] == '.' and (nz, nr, nc) not in visited:
                    visited.add((nz, nr, nc))
                    q.append((nz, nr, nc))

    print(count)


solve()