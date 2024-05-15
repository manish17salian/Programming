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
    print(candidate)
    return candidate

majorityElement( [2, 2, 1, 3, 1, 1, 3, 1, 1])

my_dict = {1: 5, 2: 4, 3: 6}

# Find the key with the maximum value
key_with_max_occurrence = max(my_dict, key=my_dict.get)

# Print the key and its corresponding value
print(f"Number with maximum occurrence: {key_with_max_occurrence}, Occurrences: {my_dict[key_with_max_occurrence]}")
