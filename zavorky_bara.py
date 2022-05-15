text = ""
zavorky = []
with open("input.txt") as f:
    for radek in f:
        text += radek.strip()

for i in text:
    if i == "(" or i == "[" or i == "{":
        zavorky.append(i)
    else:
        if(len(zavorky) >= 1):
            if zavorky[-1] + i == "()" or zavorky[-1] + i == "[]" or zavorky[-1] + i == "{}":
                zavorky.pop()
                print(zavorky)
            else: 
                print("FAIL")
                exit(0)
        else:
            print("FAIL")
            exit(0)

if(len(zavorky) == 0):
    print("OK")
else:
    print("FAIL")