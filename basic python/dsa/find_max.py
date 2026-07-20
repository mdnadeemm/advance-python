def find_max(arr):
    m = arr[0]
    for item in arr:
        if item > m:
            m = item
    return m


print(find_max([10, 8, 76, 9, 7, 24, 6, 3, 45]))
