import glob
import shutil
import os

#grab the right files with glob
videoTags = ['*zdisp.png','*ydisp.png', '*xdisp.png', '*dispM.png', '*minpStress.png', '*maxpStress.png']

ffmpegBin = 'C:\\Users\\Rebecca Napolitano\\Documents\\GitHub\\python_random\\photo_to_video\\ffmpeg\\bin\\'
fileLocation = 'C:\\Users\\Rebecca Napolitano\\Documents\\datafiles\\mike\\vecchio\\existing\\2017_11_10_Existing_brick\\'


os.chdir(fileLocation)
i = 0
numTags = len(videoTags)
while i < 6: 
    tag = videoTags[i]
    fileHandles = glob.glob(tag)
    os.chdir(ffmpegBin)
   
    #clean out bin
    oldFiles = glob.glob('*.png')
    oldMovieFiles = glob.glob('*.mp4')
    #oldFiles.append(oldMovieFiles)
    for oldFile in oldFiles:
        os.remove(oldFile)
    for oldFile in oldMovieFiles:
        os.remove(oldFile)
    
    #move files in
    os.chdir(fileLocation)
    for file in fileHandles:
        shutil.copy(file, ffmpegBin)
    
    os.chdir(ffmpegBin)
    #get name of movie
    files = glob.glob('*.png')
    for file in files:
        tagLength = len(tag)-1
        renamedFile = file[0:-tagLength] + ".png"
        os.rename(file, renamedFile)
        genericName = renamedFile[0:-5]
             
    #call ffmpeg
    call = "ffmpeg -r 1 -i " + genericName + "%01d.png -vcodec mpeg4 -y " + genericName + ".mp4"
    os.system(call)
    #os.system("ffmpeg -r 1 -i img%01d.png -vcodec mpeg4 -y movie.mp4")
    
    #move movie back to the original folder
    movieFile = glob.glob('*.mp4')
    shutil.copy(movieFile[0], fileLocation)
    #IT DOES NOT ACTUALLY SHOW UP IN THE DIRECTORY LATER!!! 
    i = i + 1