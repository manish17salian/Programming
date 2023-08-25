def pushZerosToEnd(arr, n):
    i = 0
    zeros = 0
    while i+zeros <= len(arr)-1:
        print(arr)
        if arr[i] == 0:
            for j in range(i, n-1):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                zeros +=1
        else:
            i+=1
    print(arr)
    return arr

pushZerosToEnd([3,5,0,0,4], 5)

print('Fuck')