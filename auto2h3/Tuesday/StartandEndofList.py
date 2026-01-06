


def StartEndList (L):
    #List from Parameter
    List = L
    #New list to be made
    NewList = []

    #Adding the first value from the old list to the new list
    NewList.append(List[0])
    #adding the last value from the old list to the new list, using list length
    NewList.append(List[len(List)-1])

    print (NewList)
    





List = [5, 52, 2, 2, 78]
StartEndList (List)