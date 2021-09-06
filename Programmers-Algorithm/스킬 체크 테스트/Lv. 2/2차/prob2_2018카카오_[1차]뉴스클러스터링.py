import string

def solution(str1, str2):
    answer = 0
    
    str1 = str1.lower()
    str2 = str2.lower()

    # print(str1, str2) ##
    
    l1 = len(str1)
    l2 = len(str2)
    
    # s1 = [str1[i]+str1[i+1] for i in range(l1-1)]
    # for i in s1:
    #     for j in i:
    #         if j not in string.ascii_lowercase:
    #             s1.remove(i)
    #             print(f"s1 remove '{i}'") ##
    #             break
    
    # s2 = [str2[i]+str2[i+1] for i in range(l2-1)]
    # for i in s2:
    #     for j in i:
    #         if j not in string.ascii_lowercase:
    #             s2.remove(i)
    #             print(f"s2 remove '{j}' | '{i}'") ##
    #             break

    s1 = [str1[i]+str1[i+1] for i in range(l1-1) if str1[i] in alp and str1[i+1] in alp]  
    s2 = [str2[i]+str2[i+1] for i in range(l2-1) if str2[i] in alp and str2[i+1] in alp]

    print(s1, s2) ##
    
    inter = len(s1 & s2)
    union = len(s1 | s2)
    
    print(inter, union)

    if not inter and not union:
        answer = 65536
    
    else:
        answer = int(inter/union*65536)

    print(f"ANS : {answer}") ##

    return answer

solution("handshake", "shake hands")
solution("aa1+aa2", "AAAA12")