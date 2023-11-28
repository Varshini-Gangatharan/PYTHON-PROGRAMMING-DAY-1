def num_string(n):
    arr = [[0] * 5 for _ in range(n + 1)]
    for j in range(5):
        arr[1][j] = 1
    for i in range(2, n + 1):
        for j in range(5):
            arr[i][j] = sum(arr[i - 1][:j + 1])
    total_count = sum(arr[n])
    return total_count
n =int(input("Enter the number: ")) 
res = num_string(n)
print("Output: ",res)
