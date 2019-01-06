import os

def change_name():
    new= os.listdir('prank/')   
    print(os.getcwd())
    
    tanstable= str.maketrans(dict.fromkeys("0123456789"))
    for file_name in new:
        os.renames("prank/"+file_name,"prank/"+file_name.translate(tanstable))
    print(new)

change_name()
