import string, os

os.chdir(r"C\pp2\lab6\dir_files\letters")

for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)