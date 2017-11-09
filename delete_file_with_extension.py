import glob
import os

fileHandles_unwanted = glob.glob('*_outofplane.*')

for file in fileHandles_unwanted:
    os.remove(file)