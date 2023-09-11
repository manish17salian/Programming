###Doubt####



def recursive_insertion_sort(arr):

    if len(arr) <= 1:
        return arr
    else:
        for i in range(1, len(arr)):
            # print(i)
            current = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > current:
                arr[j+1] = arr[j]
                j -= 1
                print(arr)

            arr[j+1] = current
        print(arr[:-1])
        return recursive_insertion_sort(arr[:-1]) + [arr[-1]]

    # print(arr)
    

recursive_insertion_sort([13,46,23,21,46,1])