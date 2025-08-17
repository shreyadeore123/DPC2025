def findDuplicate(arr):
    tortoise = arr[0]
    hare = arr[0]
    while True:
        tortoise = arr[tortoise]
        hare = arr[arr[hare]]
        if tortoise == hare:
            break

    tortoise = arr[0]
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[hare]

    return hare


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    print("Duplicate number:", findDuplicate(arr))
