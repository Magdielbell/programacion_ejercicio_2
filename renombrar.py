import os
path = "/home/uwu/Escritorio/car1"
files = os.listdir(path)

print(os.listdir(path))

print("nombre que desea darle a los archivo")
nombre = input()

for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, "".join([nombre,str(index), '.jpg'])))