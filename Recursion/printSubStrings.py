# Question: https://www.codingninjas.com/studio/problems/print-subsequences_8416366?leftPanelTabValue=SUBMISSION 

from typing import List

def generateSubsequences(s:str) -> List[str]:
    result = []
    def recursion(current, string, count):
        if count == len(string):
            result.append(current)
            return
        
        recursion(current+string[count], string, count+1)
        recursion(current, string, count+1)

    recursion('', s, 0)
    return result
