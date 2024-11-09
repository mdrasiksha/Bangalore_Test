import os
file_path = "C:\Users\10720021\Downloads\Mohamed Rasik I.pdf"
if os.path.isfile(file_path):
    print("file exists")
else:
    print("file not exists")