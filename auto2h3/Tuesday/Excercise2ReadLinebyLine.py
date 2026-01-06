from pathlib import Path


#using Path, to locate the currect parent directory, where script is placed together with the sample.txt file
BasePath = Path(__file__).parent

#Combining Base path with the file, to complete a full path to the file
sampleLoc = BasePath / 'sample.txt'

#open the file using open()
Sample = sampleLoc.open()


def Filereader (F):
    File = F

    In = File.readlines()

    for x in range(len(In)):
        print (In[x])

    


Filereader(Sample)


