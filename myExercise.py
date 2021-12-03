import sys

with open(sys.argv[1]) as file:
    lines = file.readlines()

for line in lines:
    index = lines.index(line)
    faulty = line
    lines.remove(line)
    lines.insert(index,faulty.strip("\n"))
    
recordBook = dict()
for line in lines:
    record = line[:line.find(":")]
    recordBook[record] = line[line.find(":")+1:].split(",")

arguments = sys.argv[2].split(",")

for arg in arguments:
    try:
        print(f"Name: {arg}, University: {recordBook[arg][1]},{recordBook[arg][0]}")
    except:
        print(f"No record of '{arg}' was found!")