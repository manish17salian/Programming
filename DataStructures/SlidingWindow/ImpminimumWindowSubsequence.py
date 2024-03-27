# Question: https://www.naukri.com/code360/problems/minimum-window-subsequence_2181133?leftPanelTabValue=SUBMISSION

def minWindow(S, T):
    min_len = float("infinity")
    start = 0
    res = ""
    left =0
    # Function to check if all characters of T can be found in sequence in the window of S
    for right in range(len(S)):
        tIndex = 0
        
        while right < len(S) and tIndex <len(T):
            if S[right] == T[tIndex]:
                tIndex+=1
            right+=1
        
        if tIndex !=len(T):
            break

        newRight = right-1
        tIndex-=1

        while tIndex >= 0:
            if S[newRight] == T[tIndex]:
                tIndex-=1
            newRight-=1
        
        newRight+=1

        if right-newRight<min_len:
            min_len = right-newRight
            start = newRight
        
        left = newRight+1
        right = left
    
    if min_len == float('inf'):
        return ""
    else:
        return S[start:start + min_len]


