import sys


# No external libraries like math are needed as only integer arithmetic and comparisons are used.

def solve():
    """Solves a single test case for the permutation sorting problem."""
    n = int(sys.stdin.readline())
    p = list(map(int, sys.stdin.readline().split()))

    # --- Step 1: Precompute positions ---
    # Create an array 'pos' where pos[x] stores the 1-based index (position) 
    # of the value 'x' in the input permutation 'p'.
    # Example: if p = [1, 5, 4, 2, 3], then pos = [0, 1, 4, 5, 3, 2] (pos[0] unused)
    pos = [0] * (n + 1)
    for i in range(n):
        pos[p[i]] = i + 1

        # --- Step 2: Find the initial central ordered block ---
    # 'l' and 'r' will store the values defining the boundaries of the longest 
    # contiguous block of numbers [l, l+1, ..., r] that are:
    # 1. Centered (l + r = n + 1)
    # 2. Already in ascending order of their positions in the original permutation p.
    # 'L' stores the length of this block (r - l + 1).

    l, r = 0, 0  # Initialize block boundaries
    L = 0  # Initialize block length

    if n % 2 == 1:  # Case: n is odd
        # The single center value is m = (n+1)/2.
        m = (n + 1) // 2
        # The initial block must contain at least this center element.
        l, r = m, m
        L = 1
    else:  # Case: n is even
        # The two center values are m1 = n/2 and m2 = n/2 + 1.
        m1 = n // 2
        m2 = n // 2 + 1
        # Check if these two center values appear in the correct relative order (pos[m1] < pos[m2]).
        if pos[m1] < pos[m2]:
            # If yes, the initial block is [m1, m2].
            l, r = m1, m2
            L = 2
        else:
            # If no, the center pair is out of order. The longest central block 
            # satisfying the conditions has length 0. 
            # We set l, r such that the expansion loop condition (l > 1) might still 
            # be initially true but will likely fail immediately if needed.
            l = m1 + 1
            r = m1
            L = 0  # Explicitly set length to 0.

    # --- Step 3: Expand the central block outwards ---
    # Try to extend the block [l, r] to [l-1, r+1] iteratively,
    # as long as the boundary conditions and the ascending position order are maintained.
    # The condition 'l > 1' checks if left expansion (to l-1) is possible.
    while l > 1:
        # Check right boundary: Can we expand to r+1? (needs r+1 <= n)
        if r + 1 > n:
            break  # Cannot expand rightwards, so stop.

        # Check order conditions for expansion:
        # 1. Does element l-1 appear before element l? (pos[l-1] < pos[l])
        # 2. Does element r appear before element r+1? (pos[r] < pos[r+1])
        if pos[l - 1] < pos[l] and pos[r] < pos[r + 1]:
            # If both conditions hold, the expansion is valid.
            l -= 1  # Extend block to the left
            r += 1  # Extend block to the right
            L += 2  # Length increases by 2
        else:
            # If either order condition fails, stop expanding.
            break

    # --- Step 4: Calculate the minimum operations ---
    # After the loop, L is the maximum length of the central block [l, r] 
    # satisfying l+r = n+1 and appearing in ascending positional order.
    # These L elements form the core that doesn't need to be touched by operations.
    # The number of elements outside this core is n - L.
    # Each operation effectively places one smaller element towards the beginning 
    # and one larger element towards the end, handling 2 elements per operation.
    # Therefore, the minimum number of operations is (n - L) / 2.
    k = (n - L) // 2
    print(k)


# Read the number of test cases.
T = int(sys.stdin.readline())
# Process each test case.
for _ in range(T):
    solve()