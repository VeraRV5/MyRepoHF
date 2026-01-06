from pathlib import Path


#using Path, to locate the currect parent directory, where script is placed together with the sample.txt file
BasePath = Path(__file__).parent

#Combining Base path with the file, to complete a full path to the file
sampleLoc = BasePath / 'sample.txt'

#open the file using open()
File = sampleLoc.open()

#Reading File using read()
print(File.read())
