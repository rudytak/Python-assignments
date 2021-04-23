input()
f = input().split(" ")
s = input().split(" ")

def sort(a):
    ret = []
    for i in range(len(a)):
        ret.append(min(a))
        a.pop(a.index(min(a)))
    return ret

def concat(a,b):
    ret = []

    for i in a:
        ret.append(i)
    for j in b:
        ret.append(j)

    return ret

def getItegerized(a):
    bruh = []
    for i in a:
        bruh.append(int(i))
    return bruh

def printArrTyDebul(a):
    killme = str(a[0])

    for i in a[1:]:
        killme+=", "+str(i)
    print(killme)

printArrTyDebul(sort(concat(getItegerized(f),getItegerized(s))))