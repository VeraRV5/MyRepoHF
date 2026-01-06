

def namemixer (s1, s2):
    str1 = s1
    str2 = s2

    #measure total character of string 1
    length1 = len (str1)
    #finding the middle of string 1
    mid = int(length1 / 2)

    #Adding string2 in middle of string1, using slicing syntax for strings
    mixedstr = str1[:2] + str2 + str1[2:]
    
    #returning the final value
    return mixedstr

    


string1 = "Vera"
string2 = "Roy"

print (namemixer(string1,string2))