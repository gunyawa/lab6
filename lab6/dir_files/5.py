myList = ["apple", "banana", "cherry"]
with open (r"C:\pp2\lab6\dir_files\test\txt1.txt", "w") as file:
    for x in myList:
        file.write(x+"\n")


cont = open(r"C:\pp2\lab6\dir_files\test\txt1.txt")
print(cont.read())