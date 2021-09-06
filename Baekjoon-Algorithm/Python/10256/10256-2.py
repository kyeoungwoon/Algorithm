def reverse(word, dna):
    
    new = set()
    n = len(word)
    for i in range(n+1):
        for j in range(i, n+1):
            # print(word[:i], word[i:j:-1], word[j:])
            app = word[:i]+word[i:j][::-1]+word[j:]
            new.add(app)

    # print(new)

    ret = 0
    for chk in new:
        if chk in dna:
            ret+=1

    return ret

case = int(input())
for _ in range(case):
    dnalen, markerlen = map(int, input().split())
    dna = input()
    marker = input()
    print(reverse(marker, dna))
