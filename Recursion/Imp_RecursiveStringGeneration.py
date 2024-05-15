# question: https://www.codingninjas.com/studio/problems/-binary-strings-with-no-consecutive-1s._893001?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTabValue=SUBMISSION

from typing import List

def generateString(N: int) -> List[str]:
    result = []
    def recursiveGenerate(current, lastAdded, N):
        if len(current) == N:
            result.append(current)
            return
        
        recursiveGenerate(current+'0', '0', N)
        if lastAdded != '1':
            recursiveGenerate(current+'1', '1', N)
    

    recursiveGenerate('', '0', N)
    return result