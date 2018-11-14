# Demonstration of th print statement
# Other information
print("Hello World")
print('Hello World')

print("I can't do it")
print('Scott sure "tries"')

# # escape charector
# print('This is the first line \nThis is the second line')
print("\n")

# printed integer and a integer string
#print(35)
#print("35")

#Concatenation combining strings
firstName = "Meghan"    # this is an inline comment
lastName  = "Rasmussen" # this stores the users lastname

print(firstName + "" + lastName) #fisrtName lastName

    # Other Options
print(firstName,lastName)

#print ('{0} first Name {1} last name'.format(firstName,lastName))
#print ('{1} first Name {0} last name'.format(firstName,lastName))

# printing integers
firstNumber = 5
secondNumber = 10
print(firstNumber + secondNumber)
print(firstNumber, secondNumber)
print('{0} is greater than {1}'.format(firstNumber, secondNumber))

# perform math function
# floatingNumber 3.24532
highTestScore = 0.9372 #floating point number
lowTestScore  = 0.4598 #floating point number
print('The high score was ' + str(highTestScore) + '\nThe low score was '+ str(lowTestScore))
print('The high score was {0:.2f}\nThe low score was {1:.2f}'.format(highTestScore, lowTestScore))

print('The print a list of things\n'
        'Apple\n'
        'Banana\n'
        'Orange\n')
    