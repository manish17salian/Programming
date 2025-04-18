# Question: https://leetcode.com/problems/max-number-of-k-sum-pairs/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hashmap = defaultdict(int)
        res = 0

        for num in nums:
            rem = k-num
            if hashmap[rem] > 0:
                res+=1
                hashmap[rem]-=1
            else:
                hashmap[num]+=1

        return res