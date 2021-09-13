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
    
    (inter, union) = func(s1, s2)

    print(inter, union)
    
    if not inter and not union:
        answer = 65536
    
    else:
        answer = int(inter/union*65536)
    
    return answer

# def intersection(l1, l2):
#     res = [val for val in l1 if val in l2]
#     return res

# def union_(l1, l2):
#     res = [val for val in l1+l2 if val not in intersection(l1, l2)] + intersection(l1, l2)
#     return res

def func(l1, l2):
    res = []
    for i in l1:
        if i in l2:
            res.append(i)
            l1.remove(i)
            l2.remove(i)
            print(f"RES {res} TRG {i} l1 {l1} l2 {l2}")
    union = l1+l2+res
    print(res, union)
    return (len(res), len(union))


solution("aa1+aa2", "AAAA12")