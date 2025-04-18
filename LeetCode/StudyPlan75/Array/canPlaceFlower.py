# Question: https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        count = 0

        for i in range(length):
            if flowerbed[i] == 0:
                left = (i==0) or (flowerbed[i-1] == 0)
                right = (i==length-1) or (flowerbed[i+1]==0)

                if left and right:
                    flowerbed[i] = 1
                    count+=1

        return count >= n        