import os

existence = os.access(r"C:\User\user\Documents\Оно точно нормально записывает.docx", os.F_OK)
readability = os.access(r"C:\User\user\Documents\Оно точно нормально записывает.docx", os.R_OK)
writability = os.access(r"C:\User\user\Documents\Оно точно нормально записывает.docx", os.W_OK)
exucatability = os.access(r"C:\User\user\Documents\Оно точно нормально записывает.docx", os.X_OK)

print("Exist:", existence)
print("Readable:", readability)
print("Writable:", writability)
print("Exucatable:", exucatability)