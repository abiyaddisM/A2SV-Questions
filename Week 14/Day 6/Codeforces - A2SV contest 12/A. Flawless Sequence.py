import math
import sys

# Use sys.stdin.readline for potentially faster input reading
input = sys.stdin.readline


def is_square(val):
    """Checks if a non-negative integer val is a perfect square using integer square root."""
    # Negative numbers cannot be perfect squares.
    if val < 0:
        return False
    # Calculate integer square root using math.isqrt. Handles large integers safely.
    k = math.isqrt(val)
    # Check if k*k equals the original value to confirm it's a perfect square.
    return k * k == val


def solve():
    """Solves a single test case for constructing a flawless permutation."""
    # Read the integer N, the length of the permutation.
    n = int(input())

    # Calculate the total sum S_N = N * (N + 1) / 2.
    total_sum = n * (n + 1) // 2

    # If the total sum S_N is a perfect square, no flawless permutation exists.
    # The condition requires ALL prefix sums to be non-squares, including S_N.
    if is_square(total_sum):
        # Print -1 and return if impossible.
        sys.stdout.write("-1\n")
        return

    # Initialize permutation p = [N, N-1, ..., 1].
    # Python list uses 0-based indexing: p[0]=N, p[1]=N-1, ..., p[N-1]=1.
    p = list(range(n, 0, -1))

    # Calculate prefix sums for the initial permutation p = [N, N-1, ..., 1].
    # prefix_sums[k] stores the sum p[0] + ... + p[k].
    prefix_sums = [0] * n  # Pre-allocate list.
    current_sum = 0
    for i in range(n):
        current_sum += p[i]
        prefix_sums[i] = current_sum

        # Iterate downwards through 0-based indices k from N-1 down to 0.
    # This corresponds to checking prefix sums S_{N}, S_{N-1}, ..., S_1 in 1-based indexing.
    for k in range(n - 1, -1, -1):
        # Check if the prefix sum S_{k+1} (which is prefix_sums[k]), calculated
        # based on the *initial* sequence p=[N, ..., 1], is a perfect square.
        if is_square(prefix_sums[k]):
            # If it was square, swap elements at indices k and k+1
            # in the *current* state of the permutation p.
            # This strategy relies on the assumption that this swap resolves the issue.
            # The check k+1 < n ensures we don't access p[N] (out of bounds).
            # This condition is guaranteed because the S_N case (k=N-1) is handled
            # by the initial check. Thus, the largest k needing a swap is N-2.
            if k + 1 < n:
                p[k], p[k + 1] = p[k + 1], p[k]
            # else: # This case k=N-1 should not trigger 'is_square' due to the initial check
            #    pass

    # Print the final permutation elements separated by spaces.
    # Convert each number to string and join them. Add a newline character.
    sys.stdout.write(" ".join(map(str, p)) + "\n")


# Read the number of test cases.
t = int(input())
# Process each test case by calling the solve function.
for _ in range(t):
    solve()