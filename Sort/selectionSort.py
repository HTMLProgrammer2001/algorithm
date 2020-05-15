def selectionSort(arr):
    for i in range(0, len(arr)):
        minimum = i

        for j in range(i, len(arr)):
            if arr[minimum] > arr[j]:
                minimum = j

        arr[i], arr[minimum] = arr[minimum], arr[i]

    return arr
    
