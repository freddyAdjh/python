
import shutil
import os

import time

# the directory where you want to store all your files

dirname = input("Enter the name of the directory you want to create : ")

# A list of keywords contained in the file name

print("Now provide the useful keywords to sort your files")

keywords = []

again = True

while again:
    keywords.append(input("Enter a keyword : ").lower())
    rep = input("continue ? (Y/n) : ")
    if rep not in ["Y",'y']:
        again = False
    else:
        continue




def MoveMyFiles(dirname,keywords):
    if os.path.isdir('./'+dirname):
        print(f"the directory {dirname} already exists")
    else:
        os.mkdir(f'{dirname}')
        print(f'{dirname} was created')

    for k in keywords:
        for f in os.listdir():
            if not os.path.isdir(f):
                name,ext = os.path.splitext(f)
                if k in name.lower():
                    shutil.move(f,f'./{dirname}/{f}')

    print(f'All files containing the keywords {keywords} was moved')




start = time.time()
MoveMyFiles(dirname,keywords)
end = time.time()

# check the time of the moving

print(f'moved in {end - start} s')