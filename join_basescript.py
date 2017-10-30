import sys

path = 'C:\\Users\\Rebecca Napolitano\\Documents\\GitHub\\python_random\\'
sys.path.insert(0,path) #navigate to function folder
from joining_files import joining_files 

file_path = 'C://Users//Rebecca Napolitano//Google Drive//Documents//Research//Roman-bonding-courses//2017_10_27_models//'
globString = '_3DEC_FILE.3ddat'
joinedName = '2017_10_30_roman-wall_3DEC_FILE.3ddat'


joining_files(file_path, globString, joinedName)