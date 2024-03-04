import os

link = "C:\Users\user\Documents\Оно точно нормально записывает.docx"
print(os.path.exists(link))
print(os.path.basename(link))
print(os.path.dirname(link))