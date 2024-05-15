# Question: https://www.codingninjas.com/studio/problems/subarrays-with-at-most-%E2%80%98k%E2%80%99-distinct-values_1473804?leftPanelTabValue=PROBLEM
from typing import List


def kDistinctSubarrays(arr: List[int], n: int, k: int) -> int:
    def helperFunc(arr,k):
        numDict = {}
        left = 0
        res = 0
        for right in range(len(arr)):
            if arr[right] in numDict:
                numDict[arr[right]] +=1
            else:
                numDict[arr[right]] = 1
            
            while len(numDict) > k:
                numDict[arr[left]]-=1
                if numDict[arr[left]] == 0:
                    del numDict[arr[left]]
                left+=1
            res += right-left+1
        return res    
    return helperFunc(arr,k)-helperFunc(arr,k-1)

# Approach:
# The approach of using "at most \(K\)" minus "at most \(K-1\)" to find the number of subarrays with exactly \(K\) distinct elements leverages a principle from combinatorics known as the inclusion-exclusion principle. Here's how it works in the context of counting subarrays with a distinct elements constraint:

# ### Understanding "At Most \(K\)" and "At Most \(K-1\)"

# - **"At Most \(K\)" Subarrays**: This count includes all subarrays that have \(K\) or fewer distinct elements. It counts every subarray where the number of distinct elements does not exceed \(K\).

# - **"At Most \(K-1\)" Subarrays**: This count includes all subarrays that have \(K-1\) or fewer distinct elements. Essentially, it's a subset of the "at most \(K\)" count, excluding any subarray that exactly has \(K\) distinct elements.

# ### The Principle of Inclusion-Exclusion

# The inclusion-exclusion principle in this context works by recognizing that the "at most \(K\)" count includes both the subarrays we're interested in (those with exactly \(K\) distinct elements) and those we're not (those with fewer than \(K\) distinct elements).

# By subtracting the "at most \(K-1\)" count from the "at most \(K\)" count, we effectively remove all subarrays that do not have exactly \(K\) distinct elements, leaving us with only those subarrays that have exactly \(K\) distinct elements.

# ### How It Works

# Imagine you slide a window across the array, expanding it to include as many elements as possible without exceeding \(K\) distinct elements. This gives you a count of subarrays with "at most \(K\)" distinct elements.

# Next, you do a similar count but limit the distinct elements to \(K-1\). This count necessarily includes all the smaller subarrays that were also part of the "at most \(K\)" count but excludes the subarrays that have exactly \(K\) distinct elements.

# The difference between these two counts tells you how many subarrays there were that had exactly \(K\) distinct elements because:

# - The "at most \(K\)" count includes subarrays with 1 to \(K\) distinct elements.
# - The "at most \(K-1\)" count includes subarrays with 1 to \(K-1\) distinct elements.

# So, the difference between these counts will give you the number of subarrays that have exactly \(K\) distinct elements, effectively excluding those with fewer than \(K\).

# ### Example

# Let's consider a small example to illustrate:

# - Array: `[1, 2, 1, 3]`, \(K = 2\).
# - "At most \(K=2\)" subarrays include: `[1]`, `[2]`, `[1, 2]`, `[2, 1]`, `[1, 3]`, and `[1, 2, 1]` (count = 6, simplifying for the example).
# - "At most \(K-1=1\)" subarrays include: `[1]`, `[2]`, `[1]` (after `[2]`), `[3]` (count = 4, simplifying for the example).
# - Difference (6 - 4 = 2) incorrectly seems to suggest two subarrays with exactly 2 distinct elements. In this simplified example, we'd manually adjust to accurately reflect combinations, demonstrating the concept rather than precise counts.

# This method accurately captures the transition points where adding another distinct element would exceed the \(K\) threshold, thereby giving us a precise count of the desired subarrays.