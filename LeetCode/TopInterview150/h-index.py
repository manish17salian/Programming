class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n= len(citations)
        citations.sort()

        for index, val in enumerate(citations):
            if n - index <=val:
                return n - index
        return 0
        
        





# The Goal:
# We want to find the h-index, which is the highest number h such that a researcher has at least h papers that have been cited at least h times.

# Key Insight:
# The main idea here is that once the citations are sorted in increasing order, we can check how many papers have enough citations for each potential h-index.

# Step-by-Step Explanation:
# Sorting the citations: When we sort the list of citations from lowest to highest, it becomes easier to check how many papers meet the h-index condition.

# For example, if the sorted list of citations is: [0, 1, 3, 5, 6], we can easily compare the number of papers that have at least h citations by looking at the list.

# What does n - i <= v mean?

# n is the total number of papers.

# i is the current index in the sorted list.

# v is the number of citations of the current paper.

# The expression n - i tells us how many papers are left starting from the current paper (including it). It’s the number of papers after the current one, including the current one itself. So if we’re at index i, n - i gives us the remaining papers that have at least the same number of citations as the current paper.

# Why do we check n - i <= v?

# What we're checking is whether there are enough papers that have at least v citations to satisfy the condition for the h-index.

# If n - i <= v, that means:

# From this point onward (starting from paper i), there are enough papers to satisfy the condition for h-index v.

# Example to make it clearer:
# Let’s use the sorted list of citations: [0, 1, 3, 5, 6].

# We want to check for each paper how many papers have at least h citations.

# At index 0 (citations = 0):

# n - i = 5 - 0 = 5 (there are 5 papers from here onward).

# v = 0 (the number of citations of this paper).

# Since 5 >= 0, this is valid. We could have an h-index of 5.

# At index 1 (citations = 1):

# n - i = 5 - 1 = 4 (there are 4 papers from here onward).

# v = 1 (the number of citations of this paper).

# Since 4 >= 1, this is valid. We could have an h-index of 4.

# At index 2 (citations = 3):

# n - i = 5 - 2 = 3 (there are 3 papers from here onward).

# v = 3 (the number of citations of this paper).

# Since 3 >= 3, this is valid. We could have an h-index of 3.

# At index 3 (citations = 5):

# n - i = 5 - 3 = 2 (there are 2 papers from here onward).

# v = 5 (the number of citations of this paper).

# Since 2 < 5, this doesn't work. We can't have an h-index of 5 because there aren’t enough papers with at least 5 citations.

# At index 4 (citations = 6):

# n - i = 5 - 4 = 1 (there is 1 paper from here onward).

# v = 6 (the number of citations of this paper).

# Since 1 < 6, this doesn't work either.

# The largest valid h-index is 3 because, at index 2, we have 3 papers with at least 3 citations.
# Why n - i <= v is important:
# It tells us if there are enough papers with at least v citations (starting from the current paper) to satisfy the h-index condition.

# When we find that n - i <= v, we know that we’ve found a valid h-index.

# In summary:
# n - i: Number of papers remaining (including the current one) from index i.

# v: The citation count of the current paper.

# If n - i <= v, that means there are enough papers left (from index i onward) to satisfy the condition for the h-index at that value.

# This approach works because, by sorting the citations and checking from the lowest index onward, we can efficiently find the largest h for which the condition holds.