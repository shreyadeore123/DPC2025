def find_missing_number(arr):
    n = len(arr) + 1   # Since one number is missing
    total_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return total_sum - actual_sum


#  Example Test Cases
print("Missing number:", find_missing_number([1, 2, 4, 5]))  # 3
print("Missing number:", find_missing_number([2, 3, 1, 5]))  # 4
print("Missing number:", find_missing_number([1]))           # 2
print("Missing number:", find_missing_number([2]))           # 1
print("Missing number:", find_missing_number([1, 2, 3, 4, 6])) # 5
