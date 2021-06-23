le = int(input())
s = input()

def isUpper(ch):
    return ch ==ch.upper()

def boi(s):
    out = ""
    for ch in range(len(s)-1):
        if (s[ch] == "?"):
            _1 = s[ch-1]
            _2 = s[ch+1]
            if(isUpper(_1) == isUpper(_2)):
                if (isUpper(_1)):
                    out+="a"
                else:
                    out+="A"
            else:
                return -1
        else:
            out += s[ch]
    
    if (s[-1] == "?"):
        if (isUpper(s[-2])):
            out+="a"                
        else:
            out+="A"
    else:
        out += s[-1]
    return out

print(boi(s))

