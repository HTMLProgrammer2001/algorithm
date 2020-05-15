def shellSort(arr):
    d = len(arr)

    while d > 0:
        for i in range(d, len(arr), d):
            if arr[i] < arr[i - d]:
                arr[i], arr[i - d] = arr[i - d], arr[i]

        d = d//2

    return arr
