def insertion_sort(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            for j in range(0, i):
                if arr[i] < arr[j]:
                    temp = arr[i]
                    for k in range(j, i):
                        arr[k+1] ,arr[j] = arr[j], arr[k+1]
                    arr[j] = temp
    return arr


insertion_sort([13,46,23,21,46,1])