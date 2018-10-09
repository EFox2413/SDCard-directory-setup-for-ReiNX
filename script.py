import wget
import zipfile
from pathlib import Path
import os
from shutil import copy
import tkinter as tk
from tkinter import filedialog

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

#set up the download directory to avoid downloading dupe files
dldir = os.path.join(os.getcwd(), 'downloads')

try:
    os.mkdir(dldir)
except FileExistsError:
    pass

#enumerate over our arrays defined above
for i, link in enumerate(links):
    #checks to see if the file already exists and downloads if so
    if not Path(files[i]).is_file():
        filename = wget.download(link, out=dldir)

#Have the user select the root directory of their SD card
root = tk.Tk()
root.withdraw()

directory = filedialog.askdirectory(initialdir="C://",
                                    title="Select SD card root directory for ReiNX installation",
                                    parent=root)


# Makes directories and unzips files to the proper locations
# If the files already exist they will be overwritten.
zipfile.ZipFile(files[0]).extractall(directory)
copy(files[1], directory)

tmpdir = os.path.join(directory, 'switch')

try:
    os.mkdir(tmpdir)
except FileExistsError:
    print(tmpdir + " directory already exists")
    
copy(files[4], os.path.join(tmpdir))
zipfile.ZipFile(files[3]).extract('tinfoil.nro', tmpdir)

tmpdir = os.path.join(directory, 'ReiNx', 'titles')

try:
    os.mkdir(tmpdir)
except FileExistsError:
    print (tmpdir + " directory already exists")
    
zipfile.ZipFile(files[2]).extractall(tmpdir)

tmpdir = os.path.join(directory, 'tinfoil', 'nsp')

try:
    os.makedirs(tmpdir)
except FileExistsError:
    print (tmpdir + " directory already exists")


print("Finished setting up ReiNX directories in " + directory)
