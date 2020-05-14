import os
import shutil 

def inputAllPath(path, pathToFile, fileName, level):
    if level <= 0:
        return 0

    print (path)
    dirs = os.listdir(path)
    
    if not os.path.exists(path + "\\" + fileName):
        shutil.copy(pathToFile, path)
    
    for dir in dirs:
        if os.path.isdir(path + "\\" + dir):
            inputAllPath(path + "\\" + dir, pathToFile, fileName, level - 1)
            
    return 0

if __name__ == "__main__":
    pathToFile = input("Enter the name of the file to be copied: ")
    path = input("Enter directory name: ")
    fileName = pathToFile.split("\\")[-1]
    inputAllPath(path, pathToFile, fileName, 4)