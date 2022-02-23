inp = open("input.txt", "r").readline().replace("\n", "")

def match(br):
    if br == "(":
        return ")"
    elif br == "{":
        return "}"
    elif br == "[":
        return "]"
    else:
        return None

st = []
suc = True
for z in inp:
    if match(z) == None:
        if len(st) > 0:
            if z == match(st[-1]):
                st.pop()
            else:
                print("FAIL")
                exit()
        else:
            print("FAIL")
            exit()
    else:
        st.append(z)

if len(st) == 0:
    print("OK")
else:
    print("FAIL")