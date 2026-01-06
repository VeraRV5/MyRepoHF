



def ListinOrder (l, h):
    Numlist = l
    Highestnum = h
    #Total Length og the list
    listlength = len(Numlist)
    #New list that will contain the number lower or equal to the chosen number
    Newlist = []
 
    #For loop that reiterate through the length of the List
    for x in range(listlength):
        #if statement that take the number from original list to the new list if its less than or equal to the chosen number
        if Numlist[x] <= Highestnum:
            Newlist.append(Numlist[x])
            print(Numlist[x])
        else:
            print("not this number")

    print (Newlist)





RanNum = [5,3,7,87,3,14,24,4,25,34,55,7,78]
hn = 10
print(ListinOrder(RanNum,hn))

