import re
import glob
import os



def joining_files(file_path, globString, joinedName):
#file_path = 'C://Users//Rebecca Napolitano//Google Drive//Documents//Research//Roman-bonding-courses//2017_10_27_models//'    
#globString = '_3DEC_FILE.3ddat'    
#joinedName = 'thisisatest.3ddat'

    os.chdir(file_path)
    
    fileHandles = glob.glob('*' + globString)
    lenFileHandles = len(fileHandles)
    i = 0
    while i <= lenFileHandles - 1:
        output = file_path + joinedName
        inputData = file_path + fileHandles[i]
        inputData = open(inputData, 'r')
        inputdata = inputData.read()
        inputData.close()
        inputdata = re.sub(r'\bret\b','', inputdata)
        if i ==0: 
            mode = 'w+'
        else:
            mode = 'a+'
        outputOpen = open(output, mode)
        #output.write('\n; ________________________________________________________________\n')
        outputOpen.write(inputdata)
        outputOpen.close()
        i = i + 1