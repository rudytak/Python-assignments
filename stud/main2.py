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
                "percent": [],
                "average": 0
            })
    return list

def nacteni_procent(list):
    x = 0
    for i in list:
        with open(list[x]["file"]) as f:
            for number in f.readlines():
                list[x]["percent"].append(int(number.strip()))
            avg_value = sum (list[x]["percent"]) / len (list[x]["percent"])
            list[x]["average"] = avg_value
            x = x + 1
            #print(list)
    return list

def kompet_data(list):
    x = 0
    text = ""
    for i in list:
        text+=list[x]["name"] + ";" + list[x]["surname"] + ";" + list[x]["id"] + ";" + ";".join(str(p) for p in list[x]["percent"][0:10])+";"+str(list[x]["average"])+"00\n"
        x = x + 1
    
    f = open("output.csv", "a")
    f.write(text)
    return

list = nacteni_do_slovniku()
list = nacteni_procent(list)
(kompet_data(list))