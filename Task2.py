# Seyfullah Burul 040963942
# Last Modified: November 27, 2020
# Reading CSV file and displaying each line of the file as a Python list.

# Importing necessary library
import csv, os

# The function listing files according to the file type
def listFileNameByType(fileType):
    fileList = os.listdir()
    notFound = True
    for fileName in fileList:
        if(fileName.find(f'.{fileType}')!=-1):
            print(fileName)
            notFound=False
    if(notFound):
        print(f'Could not be found {fileType} files')

# The function displaying lines of the CSV file
def listLinesFormCSVFile(fileName):
    # Define lines as a list
    lines = []    
    try:
        # Opening the CSV file
        with open(fileName, 'r') as csvFile:
            # Reading datas from the CSV file
            reader = csv.reader(csvFile)
            # Converting data to the Python list 
            lines = list(reader)
            # Print each item in the Python list
            for line in lines:
                print(line)
    except Exception as ex:
        # Error message
        print(f'Error occurred - {ex}')
    finally:
        # Clear variable
        del lines
    
        

# Listing CSV files in the current directory
listFileNameByType('csv')

# Prompting file name from the user
fileName = input('Please enter csv file name listed above:')

# Listing lines from the CSV file
# fileName = '2000_BoysNames.csv'
# fileName = '2000_GirlsNames.csv'
listLinesFormCSVFile(fileName)









