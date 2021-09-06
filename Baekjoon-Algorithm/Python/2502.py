day, quan = map(int, input().split())
for i in range(quan):
    qlist.append(quan-i)
    #quan, quan-i, i, quan-2i
    if quan-3*i > 0:
        print()
        pass