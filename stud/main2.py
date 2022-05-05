list = []
def nacteni_do_slovniku():
    with open("students.txt") as f:
        lines = f.readlines()
        for i in range(0,len(lines),4):
            jmeno = lines[i].split()
            list.append({
                "name": jmeno[0],
                "surname": jmeno[1],
                "id": lines[i+1].strip(),
                "file": lines[i+2].strip(),
                "percent": []
            })
    return list

def nacteni_procent(list):
    x = 0
    for i in list:
        with open(list[x]["file"]) as f:
            for number in f.readlines():
                list[x]["percent"].append(number)
            x = x+1
    print(list)
    return list

data = nacteni_do_slovniku()
nacteni_procent(data)