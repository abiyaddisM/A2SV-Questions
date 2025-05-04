import sys

def solve():
    """
    Solves a single test case.
    Reads the input strings a and b, determines if string a can be made
    all zeros using the allowed swap operations, and prints "YES" or "NO".
    """
    n = int(sys.stdin.readline())
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()

    # The core idea is that the swap operations create two independent
    # connected components of positions. Within each component, the values
    # (0s and 1s) can be freely rearranged.
    #
    # Component 1 consists of positions:
    #   - a[i] where i is even (0, 2, 4, ...) -> C1_a
    #   - b[i] where i is odd  (1, 3, 5, ...) -> C1_b
    # Component 2 consists of positions:
    #   - a[i] where i is odd  (1, 3, 5, ...) -> C2_a
    #   - b[i] where i is even (0, 2, 4, ...) -> C2_b
    #
    # To make string 'a' all zeros, we need to be able to move all the 1s
    # initially in C1_a into C1_b, and all the 1s initially in C2_a into C2_b.
    #
    # For Component 1, this is possible if and only if the number of slots
    # in C1_b is greater than or equal to the total number of 1s in Component 1
    # (i.e., the 1s originally in C1_a plus the 1s originally in C1_b).
    #
    # Similarly for Component 2, the number of slots in C2_b must be >= the
    # total number of 1s in Component 2.

    # Initialize counts for Component 1
    ones_c1_a = 0  # Count of 1s in a[i] for even i
    ones_c1_b = 0  # Count of 1s in b[i] for odd i
    size_c1_b = 0  # Number of slots in b[i] for odd i

    # Initialize counts for Component 2
    ones_c2_a = 0  # Count of 1s in a[i] for odd i
    ones_c2_b = 0  # Count of 1s in b[i] for even i
    size_c2_b = 0  # Number of slots in b[i] for even i

    # Iterate through the strings using 0-based indexing
    for i in range(n):
        if i % 2 == 0: # Even index i (0, 2, 4, ...)
            # Position (a, i) is in C1_a
            # Position (b, i) is in C2_b
            if a[i] == '1':
                ones_c1_a += 1
            if b[i] == '1':
                ones_c2_b += 1
            # Count the slots available in the 'b' part of Component 2
            size_c2_b += 1
        else: # Odd index i (1, 3, 5, ...)
            # Position (a, i) is in C2_a
            # Position (b, i) is in C1_b
            if a[i] == '1':
                ones_c2_a += 1
            if b[i] == '1':
                ones_c1_b += 1
            # Count the slots available in the 'b' part of Component 1
            size_c1_b += 1

    # Condition 1: Can Component 1 have its 'a' parts made zero?
    # Check if the 'b' slots (size_c1_b) can accommodate all 1s from Component 1.
    total_ones_c1 = ones_c1_a + ones_c1_b
    cond1 = (size_c1_b >= total_ones_c1)

    # Condition 2: Can Component 2 have its 'a' parts made zero?
    # Check if the 'b' slots (size_c2_b) can accommodate all 1s from Component 2.
    total_ones_c2 = ones_c2_a + ones_c2_b
    cond2 = (size_c2_b >= total_ones_c2)

    # Both components must satisfy the condition for 'a' to become all zeros.
    if cond1 and cond2:
        print("YES")
    else:
        print("NO")

# Read the number of test cases
t = int(sys.stdin.readline())
# Process each test case
for _ in range(t):
    solve()