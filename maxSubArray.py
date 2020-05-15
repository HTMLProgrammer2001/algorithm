def maxSubArray(arr):
    maximum = float('-Inf')
    partialSum = 0

    for elem in arr:
        partialSum += elem
        maximum = max([maximum, partialSum])

        if partialSum < 0:
            partialSum = 0

    return maximum
    
