def merge(arr1, arr2):
    left = 0
    right = 0
    res = []

    for i in range(0, len(arr1) + len(arr2)):
        if right == len(arr2):
            res.extend(arr1[left:])
            break

        if left == len(arr1):
            res.extend(arr2[right:])
            break
        
        if arr1[left] < arr2[right]:
            res.append(arr1[left])
            left += 1
        else:
            res.append(arr2[right])
            right += 1

    return res

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    n = len(arr) // 2

    return merge(mergeSort(arr[:n]), mergeSort(arr[n:]))
