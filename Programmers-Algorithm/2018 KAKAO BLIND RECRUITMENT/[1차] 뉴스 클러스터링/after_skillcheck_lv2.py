import string

def solution(str1, str2):
    answer = 0
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    l1 = len(str1)
    l2 = len(str2)
    
    alp = string.ascii_lowercase
    
    s1 = [str1[i]+str1[i+1] for i in range(l1-1) if str1[i] in alp and str1[i+1] in alp]  
    s2 = [str2[i]+str2[i+1] for i in range(l2-1) if str2[i] in alp and str2[i+1] in alp]

    print(s1, s2)
    

    inter = 
    union = s1+s2
    for i in inter:
        if i in union:
            union.remove(i)

    print(inter, union)

    inter, union = len(inter), len(union)
    
    if not inter and not union:
        answer = 65536
    
    else:
        answer = int(inter/union*65536)
    
    return answer


solution("aa1+aa2", "AAAA12")