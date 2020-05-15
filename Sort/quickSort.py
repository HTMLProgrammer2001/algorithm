def quickSort(arr):
    if len(arr) <= 1:
        return arr
    
    n = len(arr) // 2
    less = [val for index, val in enumerate(arr) if val <= arr[n] and index != n]
    more = [val for index, val in enumerate(arr) if val > arr[n] and index != n]

    return quickSort(less) + [arr[n]] + quickSort(more)
