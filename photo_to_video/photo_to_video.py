import glob
import shutil
import os

#grab the right files with glob
videoTags = ['displacement', 'xdisplacement', 'ydisplacement','zdisplacement']

ffmpegBin = 'C:\\Users\\Rebecca Napolitano\\Documents\\GitHub\\python_random\\photo_to_video\\ffmpeg\\bin\\'
fileLocation = 'C:\\Users\\Rebecca Napolitano\\Documents\\datafiles\\zippervaults\\2018_8_6_dead\\'
os.chdir(ffmpegBin)

i = 0
numTags = len(videoTags)
while i < numTags:
    print('i = ' + str(i))
    #get images
    tag = '_' + videoTags[i] + '.png'
    print('working on tag ' + tag)
    fileHandles = glob.glob(fileLocation+'*'+tag)
    newFiles = []
    for file in fileHandles:
        #replace filelocation
        newfile = file.replace(fileLocation,'')
        #replace tag string
        newfile = newfile.replace(tag,'')
        #replace cycstate_
        newfile = newfile.replace('cycstate_','')
        #replace unique numbers
        numStart = newfile.rfind('_') 
        remove = newfile[numStart:]
        removeNum = str(remove)
        newfile = newfile.replace(removeNum,'')
        #print('final file: ' + file)
        newFiles.append(newfile)
    
    
    uniqueNames = list(set(newFiles))
    numUnique = len(uniqueNames)
    print('this many unique names ' + str(numUnique))

    for name in uniqueNames:
        #clean out bin
        oldFiles = glob.glob('*.png')
        oldMovieFiles = glob.glob('*.mp4')
        #print('removing old videos')
        for oldFile in oldFiles:
            os.remove(oldFile)
        for oldFile in oldMovieFiles:
            os.remove(oldFile)
        
#        #move files in
#        os.chdir(fileLocation)
#        for file in fileHandles:
#            shutil.copy(file, ffmpegBin)
        os.chdir(fileLocation)
        filesOfInterest = glob.glob('*'+name+'*' + tag)
        for file in filesOfInterest:
            #print('copying ' + file)
            shutil.copy(file,ffmpegBin)
        
        os.chdir(ffmpegBin)
        #get name of movie
        files = glob.glob('*.png')
        tagLength = len(tag)
        for file in files:
            renamedFile = file.replace(tag,'') + '.png'
            #print('renamedFile is ' + renamedFile)
            os.rename(file, renamedFile)
            numberedName = file.replace(tag,'')
            underscoreID = numberedName[::-1].find('_') 
            genericName = numberedName[:-underscoreID]
    
        #call ffmpeg
        print('making movie')
        call = "ffmpeg -r 1 -i " + genericName + "%01d.png -vcodec mpeg4 -y " + genericName + tag.replace('.png','.mp4')
        os.system(call)
        #os.system("ffmpeg -r 1 -i img%01d.png -vcodec mpeg4 -y movie.mp4")
        
        #move movie back to the original folder
        movieFile = glob.glob('*.mp4')
        shutil.copy(movieFile[0], fileLocation)
        #IT DOES NOT ACTUALLY SHOW UP IN THE DIRECTORY LATER!!! 
    i = i + 1
    
    
