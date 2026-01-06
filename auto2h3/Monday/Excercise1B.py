




def midthree (s):
    #taking parameter into a variable
    str1 = s

    #measuring length of the string from parameter input
    slength = len(str1)
    
    #Taking first value, which is the middle of the string, by taking full length and dividing to two
    midint = int (slength / 2)

    #taking the value before middle, by subtracting 1
    formid = midint - 1

    #taking after middle value by adding 1
    aftermid = midint + 1

    #Adding each letter one by one to the result variable
    result = str1[formid] 
    result = result + str1[midint]
    result = result + str1[aftermid]
  
    #function returning result
    return result

name = "Kerveen"

print (midthree (name))
