import sys

# --- Segment Tree Implementation ---
class SegmentTree:
    """
    Segment Tree supporting range product queries modulo m.
    It's built on an initial array and allows efficient querying
    of the product of elements within any given range [l, r].
    """
    def __init__(self, arr, modulus):
        """
        Initializes the segment tree.

        Args:
            arr: The initial array of numbers.
            modulus: The modulus m to apply to the products.
        """
        self.n = len(arr)
        self.mod = modulus
        # Initialize tree size. 4*N is generally safe for segment trees.
        # Initialize nodes to 1 (the identity element for multiplication).
        self.tree = [1] * (4 * self.n)
        self.arr = arr
        # Build the tree from the input array if it's not empty.
        if self.n > 0:
            self._build(0, 0, self.n - 1)

    def _build(self, node_idx, start, end):
        """
        Recursively builds the segment tree structure.

        Args:
            node_idx: The index of the current node in the self.tree list.
            start: The starting index of the array segment covered by this node.
            end: The ending index of the array segment covered by this node.
        """
        # Base case: If the segment is a single element (leaf node)
        if start == end:
            # Store the array element modulo m in the leaf node.
            self.tree[node_idx] = self.arr[start] % self.mod
        else:
            mid = (start + end) // 2
            left_child_idx = 2 * node_idx + 1
            right_child_idx = 2 * node_idx + 2
            # Recursively build the left and right subtrees.
            self._build(left_child_idx, start, mid)
            self._build(right_child_idx, mid + 1, end)
            # The value of an internal node is the product of its children, modulo m.
            self.tree[node_idx] = (self.tree[left_child_idx] * self.tree[right_child_idx]) % self.mod

    def _query(self, node_idx, start, end, query_l, query_r):
        """
        Recursively performs the range product query.

        Args:
            node_idx: The index of the current node being considered.
            start: The starting index of the segment covered by the current node.
            end: The ending index of the segment covered by the current node.
            query_l: The starting index of the range we want to query.
            query_r: The ending index of the range we want to query.

        Returns:
            The product of elements in the intersection of the node's range
            [start, end] and the query range [query_l, query_r], modulo m.
            Returns 1 (identity) if there is no overlap.
        """
        # Case 1: No overlap.
        # If the segment [start, end] is completely outside the query range [query_l, query_r].
        if query_r < start or end < query_l:
            return 1 # Return identity element for multiplication.

        # Case 2: Complete overlap.
        # If the segment [start, end] is completely inside the query range [query_l, query_r].
        if query_l <= start and end <= query_r:
            return self.tree[node_idx] # Return the precomputed product for this segment.

        # Case 3: Partial overlap.
        # Recursively query the left and right children and combine results.
        mid = (start + end) // 2
        left_child_idx = 2 * node_idx + 1
        right_child_idx = 2 * node_idx + 2

        left_product = self._query(left_child_idx, start, mid, query_l, query_r)
        right_product = self._query(right_child_idx, mid + 1, end, query_l, query_r)

        # Combine the results from children, applying modulo m.
        return (left_product * right_product) % self.mod

    def query_range(self, query_l, query_r):
         """
         Performs a range product query for the range [query_l, query_r].

         Args:
            query_l: The starting index of the query range (inclusive).
            query_r: The ending index of the query range (inclusive).

         Returns:
            The product of array elements from index query_l to query_r, modulo m.
            Returns 1 if the range is empty (query_l > query_r).
         """
         # Handle empty range: If left index exceeds right index, the range is empty.
         # The product of an empty set is conventionally 1.
         if query_l > query_r:
              return 1
         # Start the recursive query from the root node (index 0),
         # covering the full original array range [0, n-1].
         return self._query(0, 0, self.n - 1, query_l, query_r)

# --- Main Solve Function ---
def solve():
    """
    Solves a single test case according to the problem description.
    Reads input, simulates the process using a segment tree, and prints the output.
    """
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    s = sys.stdin.readline().strip()

    # Create a segment tree for efficient range product calculation.
    st = SegmentTree(a, m)

    # Initialize left (l) and right (r) pointers to represent the current subarray.
    # Initially, it covers the whole array [0, n-1].
    l, r = 0, n - 1
    results = [] # List to store the results (products modulo m) for each step.

    # Process each of the n commands.
    for i in range(n):
        # 1. Calculate the product modulo m for the current range [l, r].
        #    This is done *before* applying the effect of command s[i].
        current_product = st.query_range(l, r)
        results.append(current_product)

        # 2. Update the range [l, r] based on the i-th command (s[i]).
        command = s[i]
        if command == 'L':
            # Remove the leftmost element by advancing the left pointer.
            l += 1
        else: # command must be 'R'
            # Remove the rightmost element by retreating the right pointer.
            r -= 1

    # Print the collected results for this test case, separated by spaces.
    print(*(results))


# --- Input Handling ---
# Read the total number of test cases.
T = int(sys.stdin.readline())
# Iterate through each test case and call the solve function.
for _ in range(T):
    solve()