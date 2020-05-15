def bubbleSort(arr):
    for i in range(0, len(arr)):
        for j in range(1, len(arr)):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]

    return arr
