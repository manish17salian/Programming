def maxSubArraySum(arr):
    ##Your code here
    max_sum = current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0

    print(max_sum)
    return max_sum

maxSubArraySum([5,-4,-2, 6, -1])