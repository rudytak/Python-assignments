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
                "average": 0,
                "conditions": 0,
                "grade": 0
            })
    return list

def nacteni_procent(list):
    x = 0
    for i in list:
        with open(list[x]["file"]) as f:
            lines = f.readlines()
            conditions = lines[-1]
            list[x]["conditions"] = conditions.strip()
            for number in range ((len(lines))-1):
                list[x]["percent"].append(int(lines[number]))
            avg_value = sum (list[x]["percent"]) / len (list[x]["percent"])
            list[x]["average"] = "{:.2f}".format(avg_value)
            x = x + 1
    return list

def kompet_data(list):
    x = 0
    text = ""

    for i in list:
        if list[x]["conditions"] == "T":
            avg = float(list[x]["average"])
            print(avg)
            if avg < 100 and avg > 87.51:
                list[x]["grade"] = "1"
            elif avg < 87.51 and avg > 62.51:
                list[x]["grade"] = "2"
            elif avg < 62.51 and avg > 37.51:
                list[x]["grade"] = "3"
            elif avg < 37.51 and avg > 12.51:
                list[x]["grade"] = "4"
            else:
                list[x]["grade"] = "5"
        else: 
            list[x]["grade"] = "N"

        text+=list[x]["name"] + ";" + list[x]["surname"] + ";" + list[x]["id"] + ";" + ";".join(str(p) for p in list[x]["percent"][0:10])+";"+str(list[x]["average"]) + ";" +str(list[x]["grade"]) + "\n"
        x = x + 1

    f = open("output.csv", "w")
    f.write(text)
    return

list = nacteni_do_slovniku()
list = nacteni_procent(list)
(kompet_data(list))