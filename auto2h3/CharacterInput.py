import datetime



def AgecalYearStatic (N, A, C):
    Name = N
    Age = int(A)
    BirthdayCelebrated = C
        
    #Taking only year value
    CurrenntYear = 2026

    #Defining variable for the final year to hundred
    YearToHundred = 0

    #Subtracts 100 by age, then adds the result to the current year using if and for loop statement
    if Age < 100:
      MaxYear = 100 - Age
      for x in range (MaxYear):
         Age += 1
         CurrenntYear += 1
         print (Age)
         print (CurrenntYear)
    else:
      print ( "Already 100:")
      print (Age)

    #If statement that take birthday to account, for if birthday hasnt occured, current year birthday wouldnt be included to the calculation which then would be wrong
    #if birthday hasnt occured, year would be advance than current age, which makes calculation adds one
    if BirthdayCelebrated == "No" or "no":
       CurrenntYear = CurrenntYear - 1
       YearToHundred = CurrenntYear

    else:
       YearToHundred = CurrenntYear

    print ("Printing Name")
    print (Name)
    print ("Printing what year you will be 100 years old") 
    print (YearToHundred)


def AgecalYearAuto (N, A, C):
    Name = N
    Age = int(A)
    BirthdayCelebrated = C
    
    #Current Date from datetime library
    CurrentDate = datetime.datetime.now()
    
    #Taking only year value
    CurrenntYear = CurrentDate.year

    #Defining variable for the final year to hundred
    YearToHundred = 0

    #Subtracts 100 by age, then adds the result to the current year using if and for loop statement
    if Age < 100:
      MaxYear = 100 - Age
      for x in range (MaxYear):
         Age += 1
         CurrenntYear += 1
         print (Age)
         print (CurrenntYear)
    else:
      print ( "Already 100:")
      print (Age)

    #If statement that take birthday to account, for if birthday hasnt occured, current year birthday wouldnt be included to the calculation which then would be wrong
    #if birthday hasnt occured, year would be advance than current age, which makes calculation adds one
    if BirthdayCelebrated == "No" or "no":
       CurrenntYear = CurrenntYear - 1
       YearToHundred = CurrenntYear

    else:
       YearToHundred = CurrenntYear

    print ("Printing Name")
    print (Name)
    print ("Printing what year you will be 100 years old") 
    print (YearToHundred)



Name = input("Enter your name")
Age = input ("Enter your Age")
BC = input("Have you celebrated your birthday this year? Yes or No")
print (AgecalYearStatic(Name, Age, BC))


