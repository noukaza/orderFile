import glob
from shutil import copyfile
import os

src = "src"
dist = "dist"

def gestionFile(path, firstLine):
    folder = firstLine.replace('\n', '')
    folder = firstLine.replace(' ', '')
    if not os.path.exists(dist+"\\"+folder):
        os.mkdir(dist+"\\"+folder) 
    splitpath = path.split('\\')
    name=  splitpath[len(splitpath) - 1]
    pa = os.path.dirname(os.path.abspath(__file__))
    pathSrc = os.path.join (pa,path)
    pathDist = os.path.join(pa,dist,folder,name)
    copyfile(pathSrc,pathDist)


files = glob.glob(src+'\\**\\*.*')
files.extend(glob.glob(src+'\\*.*'))

for filepath in files :
    file_name = filepath.split('\\')
    file_name = file_name[1]
    proto = file_name.split('_--_')[0]
    # infile = open(filepath, 'r')
    gestionFile(filepath,proto)





    
