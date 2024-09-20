


# The situation is this: You work in a company where salespeople receive 13%
# commissions on their total sales, and your boss wants you to help the salespeople
# calculate their commissions by creating a program that asks them their name and
# how much they've sold this month.


# This program should start by asking the user for things. So, you're going to need to use
# input to receive user input, and you should use variables to store that input. Remember
# that user inputs are s
#stored as strings, so you should convert one of those inputs to float
# to be able to do operations on it.

# And what operation do you need to do? Well, calculate 13% of the number that the user
# has entered. That is, multiply the number by 13, then divide by 100.

# It would be good to print the result on the screen, so make sure this information has no
# more than two decimals, so it is going to be easy to read. Then, organize all that in a
# string that you would format. Remember, we learned two ways to do it, and any of them is valid.



# Group members: Esteban Galvan, Lance Espino, Ryan Ostrowski
name = input("Hello fellow employee, What's your name? ")
#asks for their name
sales = int(input ("Hello " + name + " How much sales have you currently made? "))
#asks for the sales they made, which becomes a string to do the calculation
com = str((sales*13/100))
#the calculations, we have to convert the entire thing into a string so it can be used later in a print statement
print(name + " is entitled to " + com + " dollars worth of commissions")
#the final sentence which will add their name, and the commissions which is the variable "com" which was converted from an integer into a string




# ^^ put the final sentence in this print statement 
# Your program will answer them with a sentence that includes their name and the
# amount of commissions they are entitled to.