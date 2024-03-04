with open(r"C:\pp2\lab6\dir_files\test\txt1.txt", "r") as fp:
    lines = len(fp.readlines())
    print("Number of lines:", lines)