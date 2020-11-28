# Seyfullah Burul 040963942
# Last Modified: November 27, 2020
# Reading CSV file and displaying each line of the file as a Python list.


# Importing necessary libraries
from gfxhat import fonts, lcd, backlight
from os import system
from click import getchar

# Getting screen dimensions
scrWidth, scrHeight = lcd.dimensions()

# Screen back-lighting function
def setBacklight(light):
    if(light):
        backlight.set_all(0,255,0)
    else:
        backlight.set_all(0,0,0)
    backlight.show()

# Clear screen function
def clearScreen(lcd):
    lcd.clear()
    lcd.show()

# The function displays an object on the screen
def displayObject(obj,x,y, ignoreOutOfRangeError = True):    
    if ignoreOutOfRangeError:
        # Getting dimension of object
        pixWidth, pixHeight = 8, 8

        # Checking the position on the screen according to given X coordinate
        if(pixWidth + x > scrWidth - 1):
            x = scrWidth - pixWidth
        
        # Checking the position on the screen according to given Y coordinate
        if(pixHeight + y > scrHeight -1):
            y = scrHeight - pixHeight

    try:
        for i in range(len(obj)):
            for j in range(len(obj[i])):            
                lcd.set_pixel(x + j, y + i, obj[i][j])
        # Show marked pixel on the screen       
        lcd.show()
    except IndexError:
        print('Your object has outed off the screen according to the coordinates you entered')


# Getting 8x8 bit list from the Hex value
def getBinaryListFromHexValue(hexValue):
    # Convert Hex to Binary String
    stringBinary = bin(int(hexValue, 16))
    # Clear binary sign from the string
    stringBinary = stringBinary[2:]
    # Define list for binary values
    listBinary = []
    # Define sub-list for part of 8 bit binary
    subList = []
    for inx in range(8):
        # Get 8 bit binary from particular part 
        binValue = stringBinary[(inx * 8):((inx + 1) * 8)]
        # Append each bit to the sub-list
        for sub_bin in binValue:
            subList.append(int(sub_bin))
        # Append sub-list to the main list
        listBinary.append(subList)
        # Clear items from sub-list
        subList = []
    # Return main list
    return listBinary

# Generating dictionary from TXT file
def generateDictionary(fileName='font3.txt'):
    dictionary = {}
    try:
        # Opening the TXT file
        with open(fileName, 'r') as dataFile:
            # Reading datas from the CSV file            
            for line in dataFile.readlines():
                # Split line with comma
                splitted = line.split(',')
                # Add key and value to the dictionary
                dictionary[splitted[1].rstrip()] = getBinaryListFromHexValue(splitted[0])
            return dictionary
    except Exception as ex:
        # Error message
        print(f'Error occurred - {ex}')

# The function that reads a charachter from the user and displays the associate character on the gfxHat
def executeProgram():
    # Generate dictionary
    charDictionary = generateDictionary()
    # Define escape variable
    ESC = '\x1b'
    # Print info
    print('Please enter a character (Quit - ESC):')
    while True:
        # Get a char from the user
        c = getchar()
        # Check for quitting
        if(c == ESC):            
            break
        # Get object from dictionary
        objectList = charDictionary.get(c)
        # Check object
        if(objectList == None):
            print(f'Character {c} is not present in the dictionary')
            print('Please enter a character (Quit - ESC):')
        else:
            setBacklight(True)
            displayObject(objectList,5,5,ignoreOutOfRangeError=False)
    # End of the program
    print('End of the program')
    setBacklight(False)
    clearScreen(lcd)

# Execute the program
executeProgram()
