import math

def merge(arr1, arr2):
    n, m = len(arr1), len(arr2)
    gap = math.ceil((n + m) / 2)

    while gap > 0:
        i, j = 0, gap
        while j < (n + m):
            if i < n:
                a = arr1[i]
            else:
                a = arr2[i - n]

            if j < n:
                b = arr1[j]
            else:
                b = arr2[j - n]

            if a > b:
                if i < n and j < n:
                    arr1[i], arr1[j] = arr1[j], arr1[i]
                elif i < n and j >= n:
                    arr1[i], arr2[j - n] = arr2[j - n], arr1[i]
                else:
                    arr2[i - n], arr2[j - n] = arr2[j - n], arr2[i - n]
            
            i += 1
            j += 1

        if gap == 1:
            gap = 0
        else:
            gap = math.ceil(gap / 2)

    return arr1, arr2

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
arr1, arr2 = merge(arr1, arr2)
print("arr1:", arr1)
print("arr2:", arr2)
