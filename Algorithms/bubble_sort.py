def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

bubble_sort([3,4,2,1,4,8,2,3])    