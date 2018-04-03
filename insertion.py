
def insertion(slist):
    newArray = []

    for i in range(1,len(slist)):
        while i>0 and slist[i-1]>slist[i]:
            slist[i],slist[i-1]=slist[i-1],slist[i]
            i -=1
    newArray.extend(slist)

    return newArray

print(insertion([12,31,1,13,65,3,1,98,76]))
