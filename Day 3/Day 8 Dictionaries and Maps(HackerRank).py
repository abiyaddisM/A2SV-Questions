def main():
    import sys

    n = int(input())

    phone_book = {}

    for _ in range(n):
        entry = input().strip().split()
        phone_book[entry[0]] = entry[1]

    for line in sys.stdin:
        query = line.strip()
        if query in phone_book:
            print(query + '=' + phone_book[query])
        else:
            print("Not found")

if __name__ == "__main__":
    main()