# https://www.acmicpc.net/problem/10256

# from itertools import combinations

'''
def marker(marker, markerlen):
    mt=list()
    div = list(combinations(range(markerlen+1), 2)) #list actually unneeded
    for divs in div:
        mt.append(marker[:divs[0]]+marker[divs[0]:divs[1]][::-1]+marker[divs[1]:])
    return list(set(mt))

def mutant(marker, markerlen):
    mt=list()
    for x in range(markerlen):
        for y in range(markerlen-x):
            reversed_part=marker[x:x+y] #wrong code
            mt.append(marker[:x]+reversed_part[::-1]+marker[x+y:])
    return mt
'''

def mutants(marker, markerlen):
    mt=set()
    for x in range(markerlen+1):
        start = marker[:x]
        for y in range(x+1, markerlen+1):
            middle = marker[x:y][::-1]
            end = marker[y:]
            mt.add(start + middle + end)
    return set(mt)

'''
def search(dna, dnalen, mutants, markerlen):
    mutantnum=0
    trackers = list()
    for i in range(dnalen):
        c = dna[i]

        for tracker in trackers:
            if c == tracker[0][tracker[1]]:
                tracker[1] += 1
            else:
                trackers.remove(tracker)

        for mutant in mutants:
            if mutant[0] == c:
                trackers.append([mutant, 1])

        print(c, trackers)
        for tracker in trackers:
            if tracker[1] == markerlen:
                mutantnum+=1
                print('Found', tracker)
                trackers.remove(tracker)
    print(mutantnum)
'''

def dna4(dna, dnalen, markerlen):
    d = list()
    for x in range(dnalen-markerlen+1):
        d.append(dna[x:x+markerlen-1])
    return d

case = int(input())
mutantnum = 0

for x in range(case):
    dnalen, markerlen = map(int, input().split())
    dna = input()
    marker = input()
    '''for mark in mutant(marker, markerlen):
        if mark in dna:
            mutantnum+=1
    '''
    #search(dna, dnalen, mutants(marker, markerlen), markerlen)
    for dnacut in dna4(dna, dnalen, markerlen):
        if dnacut in mutants(marker, markerlen):
            mutantnum+=1
    print(mutantnum)