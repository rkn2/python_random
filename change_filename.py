import glob
import os

file_path = 'C:/Users/Rebecca Napolitano/Documents/datafiles/mike/vecchio/existing/2017_11_10_Existing_brick/'
originalDate= '10_30'
newDate = '11_10'
originalName = 'Existinggeometryfull_finalmodel'
newName = 'Existing'

os.chdir(file_path)
fileHandles = glob.glob('2017_*')

for file in fileHandles:
    newFile = file.replace(originalDate,newDate)
    #newFile = file.replace(originalName, newName)
    os.rename(file, newFile)
    
    