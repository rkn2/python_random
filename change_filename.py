import glob
import os

file_path = 'C:/Users/Rebecca Napolitano/Google Drive/Documents/Research/mikehess/palazzo vecchio/2017_9_7_ElementiModels/FoundationModels/ExistingGeometry/bricks/2017_10_19_Existinggeometryfull_brick/'
originalDate= '9_7'
newDate = '10_17'

os.chdir(file_path)
fileHandles = glob.glob('2017_*')

for file in fileHandles:
    newFile = file.replace(originalDate,newDate)
    os.rename(file, newFile)
    
    