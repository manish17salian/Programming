'Demo Link https://www.youtube.com/watch?v=MZaf_9IZCrc&t=3s'

def quick_sort(arr):
    if len(arr) > 1:
        print(arr, 'Array')
        pivot = arr[-1]
        i = -1
        for j in range(0, len(arr)-1):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        z = len(arr)-1
        print(z,i)
        while z > i+1:
            arr[z-1], arr[z] = arr[z], arr[z-1]
            z-=1
        
        # if len(arr) != 2 and arr[i] != arr[i+1] :
        first_arr = arr[:i+1]
        second_arr = arr[i+1:]
        print(first_arr, second_arr)
        quick_sort(first_arr)
        quick_sort(second_arr)
        k=0
        m=0
        while m < len(first_arr):
            arr[k] = first_arr[m]
            m+=1
            k+=1
        n=0
        while n < len(second_arr):
            arr[k] = second_arr[n]
            n+=1
            k+=1
    print(arr)
    return arr
quick_sort([2,2])
# # quick_sort([4,6,2,5,7,9,1,3])
# quick_sort([1,99,1000,121,2,2,3,7])
# quick_sort([92,99,79,9,3,0])
# quick_sort([1,2,3,0,4])



def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Example usage
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
