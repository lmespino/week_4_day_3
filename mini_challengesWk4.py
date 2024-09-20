#################################string properties################################
# Esteban Galvan, Lance Espino, Ryan Ostrowski

# String Properties Practice #1
# Concatenate the text "Repetition" 15 times and display the result on the screen.
# Luckily, you know that strings are multipliable and you can do this activity in a simple and elegant way.
print("Repetition " * 15)

# String Properties Practice #2
# Check if the word "beach" is not found in the following haiku. You should print the boolean.
# "Whitecaps on the bay:
# A broken signboard banging
# In the April wind."
# — Richard Wright, collected in Haiku: This Other World, 1998
Haiku = "Whitecaps on the bay: A broken signboard banging: In the April wind."
HasBeach = Haiku.find("Beach")
# words that aren't able to be found will be listed with a value of -1, which will be used in our boolean IF statement
if HasBeach == -1 :
    print("The word 'beach' is not in the Haiku")

# String Properties Practice #3
# Check the Python Documentation to find the description of the len() function. Then, display on the screen the length (in number of characters) of the word electroencephalographist.
print(len("electroencephalographist"))