alist = [0,1,2,3,4,6]
blist = [5,4,3,2,1,0]
for a in alist:
    for b in blist:
        print(b)
        if blist.index(b) == a:
            break
    else:
        print("a")
    print("b\n")