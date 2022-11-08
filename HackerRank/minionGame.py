# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
def minion_game(string):
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
    # your code goes here
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
                print(str)
                if str[0] in vowels:
                    if str not in kevin_word_list:
                        kevin_word_list.append(str)
                        count = occurance(string,str)
                        print(count)
                        kevin_score +=count
            kevin_str = kevin_str[1:]
        else:
            str = ''
            for x in stuart_str:
                str +=x       
                if str[0] not in vowels:
                    if str not in stuart_word_list:
                        stuart_word_list.append(str)
                        count = occurance(string,str)
                        stuart_score +=count
            stuart_str = stuart_str[1:]
    
    print(kevin_score, stuart_score,kevin_word_list)

    if kevin_score == stuart_score:
        print('Draw')
    elif kevin_score>stuart_score:
        print('Kevin ',kevin_score)
    else:
        print('Stuart',stuart_score)
        
    

                    
                    
# minion_game('BANANANAAAS') #draw
minion_game('ANANAS') #kevin 12
            

# if __name__ == '__main__':