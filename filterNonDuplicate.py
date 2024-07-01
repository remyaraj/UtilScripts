import os
from pathlib import Path

import sys, getopt

import shutil


f1 = sys.argv[1]
print(f1)

files_1 = os.listdir(f1)

print(len(files_1))

f2 = sys.argv[2]
print(f2)

f3 = sys.argv[3]
print(f3)

#files_2 = sorted(os.listdir(f2))
#print(len(files_2))

for filename in files_1:
	path = os.path.join(f2, filename)
	if not os.path.isfile(path):
		#print(path)
		srcpath = os.path.join(f1,filename)
		destpath = os.path.join(f3,filename)
		shutil.copyfile(srcpath, destpath);

desfiles = os.listdir(f3);
print(len(desfiles))


for f in desfiles:
	print(f)

