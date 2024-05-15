# Question: https://www.codingninjas.com/studio/problems/longest-repeating-substring_980523?leftPanelTabValue=PROBLEM

def longestRepeatingSubstring(stri: str, k: int) -> int:
    countDict = {}
    res = 0
    maxCount = 0
    left = 0
    for right in range(len(stri)):
        if stri[right] in countDict:
            countDict[stri[right]]+=1
        else:
            countDict[stri[right]] = 1
        
        maxCount = max(maxCount, countDict[stri[right]])
        if(right-left+1) - maxCount > k:
            countDict[stri[left]]-=1
            left+=1
        res = max(res, right-left+1)
    return res