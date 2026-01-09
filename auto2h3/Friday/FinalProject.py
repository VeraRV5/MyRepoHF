import requests
from cryptography.fernet import Fernet

###########Opgave 1#############

#Token and the ip link
token = "49259f43"
link = "20.91.198.208:8081"

#A function that takes the token and link and, send an html request, with Token as parameters
def httprequest(l, t):
    link = l
    token = t
    payload = {'token': token}
    
    #Use Try and Catch method, to run the request and print outs the header and body of the html link
    try:
        Data = requests.get(link +'/get', params=payload)

        print ("header", Data.headers)
        print ("Body", Data.text)
        return Data
    except Exception as e:
        print ("error:", e)

#Calling the function with parameters
HttpData = httprequest(link, token)


############Opgave 2##################

#Given Key and Encrypted data from head and body, taken from opgave 1
Skey = "uz61s234NrKrVzRqkzC5IawFSmbbhb-fJXOD4w1qNRg="
Encrypted = "gAAAAABpYMff_HIXNJjSQZdqNY2xgDqxIdBqxTMjAik5h69fh0BQ4RKGa33YJGfnnzuGNXJdtV7wRYz_HpMpHzG3Y7asxK_8cGRYdCNreunt3PEXK9lzvo6prFXOEJN6jO10WXArWGyqBURPkClYcDd6p244k1UY1TRqwzZDvu1FSBZyBw3tv3m_oOX4kghelULQ1kK9wV6Sbpxvl7IAxqk7CGGylsWbGPtUS6pk2InX0ECmZ5c8f_fe_FuHfNEvN2vB1C_yC3VV_gYt_B8ZV1eCGP4Uts_80xqmdjHElP5JQRhzGcR_-i-g20MyFoOktUyiaytv8bNZVVbHV9r_YDALrwkAC-iyBy_1yNxiprIFEdXgpRx3u8FZxLk3rfxjJB-8diBJSIdPrWEHAHbSw-zdfi4N8qnnokliEkRKi3jp78ukvHHDceOcfFmMHwJl2dFeJXXkzRXp-1No4pnrvPQ0VUMfoqUysEd97yXl4KFm-IUh-DWBIOQ="

#Function that Decrypts the Data, with the key and the encrypted Data, using Fernet library
def decrypter (S, E):
    Secretkey = S
    Encrypted = E
    key = Fernet(Secretkey)
    print ("Decrypted: ", key.decrypt(Encrypted))

#Calling Decrypter function
decrypter(Skey, Encrypted)


############Opgave 3###################


# A function that will measure the length of the Encrypted Data, and multiply it by two, and print the result
def lenMulti(D):
    Data = D
    #Measure Data length & prints it
    lenEncrypted = len(Data)
    print ("Length of Data: ", lenEncrypted)
    
    #Multiple the result by 2, and prints it
    Multi = lenEncrypted * 2
    print 
    print("Length Multiplied by 2: ", Multi, ": Answer")

#Calling the dunction
lenMulti(Encrypted)

Send = requests.get("http://20.91.198.208:8081/submit?token=49259f43&ansvar=1008")
print (Send.text)


######Opgave 4#####
#Explanation
######Opgave 5#####

txt = "Python is powerful, but sometimes tricky"

def lettercounter (T):
    Data = T
    DataLength = len(Data)
    count = 0
    for x in range(DataLength):
       if Data[x] == "t":
           count += 1
           print (count)  
    print ("Total Count of T:", count)

lettercounter(txt)

def stringreverser(T):
    Data = T
    #is a slicing operation. The first colon (:) means that the entire string is being selected.-1 indicates the step, meaning the string is read from right to left.
    reversed = Data[::-1]
    print (reversed)

stringreverser(txt)

def pythonreplacer(T):
    Data = T
    print (Data.replace("Python", "PYTHON"))

pythonreplacer(txt)

