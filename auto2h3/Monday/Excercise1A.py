


string2 = "Kerveen"


print(len(string2))

#total length of name
length =len(string2)

#first letter is 0
first = string2[0]

#total length divided two 2 then float number is turned to integer
midint = int(length / 2)
midletter = string2[midint]
print(midletter)

#total length minus 1, because it starts from index starts from 0, number count is -1 from total value
last = string2[length - 1]


total = first + midletter + last

print(total)

