import os
def renameNamesFromDir(path,ending):

    files = os.listdir(path)

    for file in files:
        nameArray=file.split(ending)
        name = nameArray[0]
        nameFinal = name.rstrip()
        os.rename(os.path.join(path,file), os.path.join(path, nameFinal+ending))
        print(name + " -> " , nameFinal)
    print("Success")

renameNamesFromDir('','.pdf')