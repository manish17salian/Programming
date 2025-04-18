# Question: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxEl = max(candies)
        res = []
        for i in candies:
            res.append(i+extraCandies >= maxEl)
        return res