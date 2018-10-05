import wget
import zipfile
from pathlib import Path
import os
from shutil import copy

links = ['http://builds.reinx.guide/nightly/ReiNX-latest.zip',
          'https://reinx.guide/u/hbmenu.nro',
          'https://reinx.guide/u/010000000000100D.zip',
          'https://reinx.guide/u/tinfoil.zip',
          'https://reinx.guide/u/ReiNX_Toolkit.nro']

files = ['./downloads/ReiNX-latest.zip',
              './downloads/hbmenu.nro',
              './downloads/010000000000100D.zip',
              './downloads/tinfoil.zip',
              './downloads/ReiNX_Toolkit.nro']


try:
    os.mkdir('./downloads/')
except FileExistsError:
    pass

#enumerate over our arrays defined above
for i, link in enumerate(links):
    #checks to see if the file already exists and downloads if so
    if not Path(files[i]).is_file():
        filename = wget.download(link, out='./downloads')

#TODO: Autodetect if they have a SDCard drive and attempt to set the directory
#      to the drive
directory = os.getcwd() + '\\sdcard\\'


# Makes directories and unzips files to the proper locations
# If the files already exist they will be overwritten.
zipfile.ZipFile(files[0]).extractall(directory)
copy(files[1], directory)

try:
    os.mkdir(directory + 'switch')
except FileExistsError:
    print(directory + 'switch' + " directory already exists")
    
copy(files[4], directory + 'switch/')
zipfile.ZipFile(files[3]).extract('tinfoil.nro', directory + 'switch/')

try:
    os.mkdir(directory + 'ReiNX/titles')
except FileExistsError:
    print (directory + 'ReiNX/titles' + " directory already exists")
    
zipfile.ZipFile(files[2]).extractall(directory + 'ReiNX/titles')

try:
    os.makedirs(directory + 'tinfoil/nsp/')
except FileExistsError:
    print (directory + 'tinfoil/nsp/' + " directory already exists")


print("Finished setting up ReiNX directories in " + directory)
