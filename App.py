from os import path, listdir, mkdir
from shutil import move

def main() -> None:
    basepath:str = 'd:\\Descargas' #Change the Downloads Path to yours.

    for file in listdir(basepath):
        if path.isfile(path.join(basepath,file)):
            _, extension = path.splitext(file)
            dst_Path:str = path.join(basepath,extension)
            if extension not in listdir(basepath):
                mkdir(path.join(basepath,extension))
            move(path.join(basepath,file),path.join(dst_Path,file))

if __name__ == "__main__":
    main()