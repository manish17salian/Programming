'EXPLANATION AT https://www.youtube.com/watch?v=4VqmGXwpLqc'

def merge_sort(arr):
    print('CALLED')
    if len(arr) > 1:
        middle = len(arr)//2
        left_arr = arr[:middle]
        right_arr = arr[middle:]
        merge_sort(left_arr)
        merge_sort(right_arr)
        i = 0
        j = 0
        k = 0
        print('Now', left_arr, right_arr)
        
        while (i < len(left_arr)) and (j < len(right_arr)):
            print(left_arr, right_arr, 'Inside first while')
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j+=1
            k+=1
            print(arr)
        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1
        
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1

    print(arr, 'Finally')    
    return arr
merge_sort([9,4,7,6,3,1,5])