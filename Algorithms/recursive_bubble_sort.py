def recursive_bubble_sort(arr):
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            break
    else:
        print(arr)
        return arr
    print(len(arr))
    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            # pass``
            arr[i], arr[i+1] = arr[i+1], arr[i]
            break;
    return recursive_bubble_sort(arr)



recursive_bubble_sort([1,3,2,9,2,3])