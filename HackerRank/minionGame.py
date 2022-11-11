# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
def minion_game(string):
    if len(string) <=10**6:
        def occurance(mainstr,substr):
            count = 0
            for i in range(0, len(mainstr)):
                if mainstr[i] == substr[0]:
                    if (i + len(substr))>=len(mainstr):
                        newstr = mainstr[i:]
                    else:
                        newstr = mainstr[i:i+len(substr)]
                    j = 0
                    con = False
                    if len(newstr)>=len(substr):
                        while j <=len(substr)-1:
                            if newstr[j] == substr[j]:
                                con = True
                            else:
                                con = False
                                break;
                            j+=1
                        if (con == True):
                            count +=1
            return count

        vowels = ('A','E','I','O','U')
        stuart_score = 0
        kevin_score = 0
        stuart_word_list = []
        kevin_word_list = []
        stuart_str = string
        kevin_str = string
        for i in string:
            if i in vowels:
                str = ''
                for x in kevin_str:
                    str +=x
                    if str[0] in vowels:
                        if str not in kevin_word_list:
                            kevin_word_list.append(str)
                            count = occurance(string,str)
                            kevin_score +=count
            else:
                str = ''
                for x in stuart_str:
                    str +=x  
                    if str[0] not in vowels:
                        if str not in stuart_word_list:
                            stuart_word_list.append(str)
                            count = occurance(string,str)
                            stuart_score +=count
            kevin_str = kevin_str[1:]
            stuart_str = stuart_str[1:]
        
        if kevin_score == stuart_score:
            print('Draw')
        elif kevin_score>stuart_score:
            print('Kevin',kevin_score)
        else:
            print('Stuart',stuart_score)

minion_game('BAANANAS') #kevin 12


#Not Optimised


#Optimised
def minion_game(string):
    vowels = 'AEIOU'
    kevin_score, stuart_score = 0, 0
    strlen = len(string)
    
    for i in range(0, strlen):
        if string[i] in vowels:
            kevin_score += strlen-i
        else:
            stuart_score += strlen-i

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif kevin_score < stuart_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

