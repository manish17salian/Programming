# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

def merge_the_tools(string, k):
    list_char = []
    dum_str = string
    final_list = []
    # count = 0
    # char = ''
    # for i in string:
    #     count +=1
    #     if count == k:
    #         char+=i
    #         list_char.append(char)
    #         char=''
    #         count=0
    #     else:
    #         char+=i
    # print(list_char)
    while len(dum_str) >= k:
        list_char.append(dum_str[0:k])
        dum_str = dum_str[k:]
    
    for i in range(0, len(list_char)):
        char = list_char[i]
        dum_str = ''
        for x in char:
            if x not in dum_str:
                dum_str+=x
        final_list.append(dum_str)
        print(dum_str)
merge_the_tools('AABCAAADA',3)
