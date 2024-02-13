# Algorithm video : https://youtu.be/nP_ns3uSh80

def majorityElement(v: [int]) -> int:
    candidate = None
    count = 0

    for i in v:
        if count == 0:
            candidate = i
            count+=1
        elif candidate != i:
            count -=1
        else:
            count +=1
    
    return candidate
    