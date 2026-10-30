import glob
from datetime import datetime

def merge_file(filePath, fileNames):
    with open(filePath, "a") as newFile:
        for fileName in fileNames:
            with open(fileName) as existing_file:
                content = existing_file.read()
            newFile.write(content + "\n")    

time = datetime.now()
filePath = time.strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt"
filenames = glob.glob("TextFiles/*.txt")

merge_file(filePath, filenames)