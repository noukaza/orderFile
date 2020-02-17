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


files = glob.glob(src+'/**/*.*')
files.extend(glob.glob(src+'/*.*'))

for filepath in files :
    file_name = filepath.split('/')
    file_name = file_name[1]
    proto = file_name.split('|')[0]
    # infile = open(filepath, 'r')
    gestionFile(filepath,proto)





