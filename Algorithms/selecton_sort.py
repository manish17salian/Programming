def selectionSort(arr):
    for i in range(0, len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            print(arr[min_index] ,arr[j])
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

selectionSort([3, 4, 3, 2, 5])
            
