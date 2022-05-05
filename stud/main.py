# import json

f=open("students.txt","r")
lines=f.readlines()
f.close()

clas = { 
    "class_name":"36",
    "students":[]
}
for i in range(0, len(lines),4):
    names = lines[i].strip().split(" ")
    path = lines[i+2].strip()
    
    f1 = open(path, "r")
    marks = list(map(lambda x: int(x.strip()), f1.readlines()))
    f1.close()

    clas["students"].append({
        "first_name":names[1],
        "last_name":names[0],
        "id": lines[i+1].strip(),
        "file_path": path,
        "marks": marks,
        "avg": sum(marks)/len(marks)
    })

# f3=open("students.json","w")
# f3.write(json.dumps(clas, indent=4))
# f3.close()

out = ""
for s in clas["students"]:
    out += ";".join([s["last_name"],s["first_name"],s["id"]] + list(map(str,s["marks"])) + [f'{s["avg"]:.{3}f}']) + "\n"


f4=open("output.csv","w")
f4.write(out)
f4.close()



