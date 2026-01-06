from pathlib import Path


#using Path, to locate the currect parent directory, where script is placed together with the sample.txt file
BasePath = Path(__file__).parent

#Combining Base path with the file, to complete a full path to the file
sampleLoc = BasePath / 'sample.txt'

#open the file using open()
Sample = sampleLoc.open()


def Filereader (F):
    #take File from parameter
    File = F
    
    #Use readlines, to append the txt line by line to a list
    In = File.readlines()

    #Use a for loop to reiterate from the In List and print line by line
    for x in range(len(In)):
        print (In[x])

    

#Call Filereader Function
Filereader(Sample)


