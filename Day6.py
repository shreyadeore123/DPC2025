def find_zero_sum_subarrays(arr):
    n = len(arr)
    result = []
    
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            if s == 0:
                result.append((i, j))
    return result


arr = [1, 2, -3, 3, -1, 2]
print(find_zero_sum_subarrays(arr))  
