
print("Addition")
Addition = 9
print("4 + 5 =")
print(Addition)

print("Subtraction")
Subtraction = 4
print("7 - 3 =")
print(Subtraction)

print("Multiplication")
Multiplication = 12
print("3 * 4 =")
print(Multiplication)

print("Division")
Division = 3.5
print("7 / 2 =")
print(Division)

print("RoundedDivision")
RoundedDivision = 3
print("7 // 2 =")
print(RoundedDivision)

print("Exponent")
Exponent = 8
print("2**3 =")
print(Exponent)

def printLyrics():
    print("La de da de da")
    print("doo da doo")

printLyrics()

#10 row Table

i=0
j=0
while i < 5:
    while j < 5:
        print(j, end='')
        j += 1
    print('\n#############')
    j=0
    i += 1

    
#boolean stuff

boolean = 1 #Change number to change results
if boolean > 1 :
    print("Greater than 1")
elif boolean < 1 :
    print("Less than 1")
elif boolean == 1 :
    print("equal to 1")
elif boolean >= 1 :
    print("greater than or equal to 1")
elif boolean <= 1 :
    print("less than or equal to 1")

# split()

# any string can be "split" on any character, or characters
# the result is a list (sometimes called an array)
# you may not realize it now, but this can be very handy
someValues = "Laconia Gilford Belmont"
listOfValues = someValues.split()
print(listOfValues[1])
#here is a more complex example
keyValuePairs = "Bill: Laconia, Jane: Gilford, Tom: Belmont"
listOfPairs = keyValuePairs.split(", ")
count = 0
while count < len(listOfPairs):
    fname, town = listOfPairs[count].split(": ")
    print("first name is: " + fname + "\n town is: " + town)
    count += 1
    
