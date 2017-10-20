import glob
import os

file_path = 'C:/Users/Rebecca Napolitano/Documents/datafiles/mike/vecchio/existing/2017_10_19_Existinggeometryfull_brick/'
originalDate= '10_17'
newDate = '10_19'

os.chdir(file_path)
fileHandles = glob.glob('2017_*')

for file in fileHandles:
    newFile = file.replace(originalDate,newDate)
    os.rename(file, newFile)
    
    