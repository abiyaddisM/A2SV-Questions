import sys
input = sys.stdin.read

def main():
    data = input().split()
    n = int(data[0])
    points = []
    for i in range(n):
        x = int(data[2 * i + 1])
        y = int(data[2 * i + 2])
        points.append((x, y, i + 1))  # Store x, y, and original index (1-based)

    # Group points into buckets based on x // 1000
    from collections import defaultdict
    buckets = defaultdict(list)
    for x, y, idx in points:
        buckets[x // 1000].append((x, y, idx))

    # Process buckets in order of bucket key
    result = []
    reverse = False
    for bucket_key in sorted(buckets.keys()):
        bucket = buckets[bucket_key]
        # Sort by y-coordinate
        bucket.sort(key=lambda p: p[1])
        # Reverse every other bucket to create snake pattern
        if reverse:
            bucket.reverse()
        result.extend(p[2] for p in bucket)
        reverse = not reverse

    print(' '.join(map(str, result)))

main()
