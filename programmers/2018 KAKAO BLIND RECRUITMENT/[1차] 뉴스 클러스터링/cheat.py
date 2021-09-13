from collections import Counter

def solution(str1, str2):
    answer = 0
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    l1 = len(str1)
    l2 = len(str2)
    
    s1 = [str1[i]+str1[i+1] for i in range(l1-1) if (str1[i]+str1[i+1]).isalpha()]  
    s2 = [str2[i]+str2[i+1] for i in range(l2-1) if (str2[i]+str2[i+1]).isalpha()]

    print(s1, s2)
    
    cs1 = Counter(s1)
    cs2 = Counter(s2)

    print(cs1, cs2)

    inter = list((cs1 & cs2).elements())
    union = list((cs1 | cs2).elements())

    print(inter, union)

    inter, union = len(inter), len(union)
    
    if not inter and not union:
        answer = 65536
    
    else:
        answer = int(inter/union*65536)
    
    return answer


solution("aa1+aa2", "AAAA12")