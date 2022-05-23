ret = [-1 for _ in range(26)]
word = input()
for i in range(1, len(word)+1):
    ret[ord(word[len(word)-i])-ord('a')] = len(word)-i
for i in ret:
    print(i, end = ' ')