class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        
        curr = [1]*n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                curr[i] = curr[i-1]+1
        
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                curr[i] = max(curr[i], curr[i+1]+1)
        return sum(curr)
        