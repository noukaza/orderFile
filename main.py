import glob
from shutil import copyfile
import os

src = "src"
dist = "dist"

def gestionFile(path, firstLine):
    folder = firstLine.replace('\n', '')
    if not os.path.exists(dist+"/"+folder):
        os.mkdir(dist+"/"+folder) 
    splitpath = path.split('/')
    name=  splitpath[len(splitpath) - 1]
    copyfile(path, dist+"/"+folder+"/"+name)


files = glob.glob(src+'/**/*.txt')
files.extend(glob.glob(src+'/*.txt'))

for filepath in files :
    infile = open(filepath, 'r')
    firstLine = infile.readline()
    gestionFile(filepath,firstLine)




