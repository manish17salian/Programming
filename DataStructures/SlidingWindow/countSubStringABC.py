# Question: https://www.codingninjas.com/studio/problems/count-substring-with-abc_8160465?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=PROBLEM

from typing import *

def countSubstring(s : str) -> int:
    charCount = {'a': 0, 'b': 0, 'c': 0}
    left = 0
    res = 0
    
    
    for right in range(len(s)):
        
        charCount[s[right]] += 1
        
        while all(count > 0 for count in charCount.values()):
            res += len(s) - right
            
            # Move left pointer to shrink the window
            charCount[s[left]] -= 1
            left += 1
            
    return res