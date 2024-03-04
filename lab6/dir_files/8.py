import os

ex = os.access(r"C:\pp2\lab6\dir_files\test\remove.txt", os.F_OK)
print("Existence:", ex)
os.remove(r"C:\pp2\lab6\dir_files\test\remove.txt")