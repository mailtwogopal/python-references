file = open("test.txt", 'w')
file.write("\n")
file.write("line1\n")
file.write("line2\n")
file.write("line3\n")
file.write("line4\n")
file.write("line5\n")
file.write("line6\n")
file.write("line7\n")
file.write("line8\n")
file.close()

fl = open("test.txt", "r")
content = fl.readlines()[4:5] # this will read till line 4 excluding 5
print(content)

print("below are from with method")

with open("test.txt", "r") as f:
    filecontent = ""
    for line in f:
        if "line5" not in line:
            filecontent = filecontent + line
    with open("newtxt.txt", "w") as wf:
        wf.write(filecontent)

