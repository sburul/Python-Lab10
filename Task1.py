# Seyfullah Burul
# Last Modified: November 27, 2020
# Reading text file and converting it into a csv file format

# Importing necessary library
import csv

# The function that creates CSV file from comma-delimited TXT file
def createCsvFileFromTextFile(txtFileName, csvFileName):    
    # Open Txt and Csv files
    with open(txtFileName, 'r') as txtFile, open(csvFileName, 'w', newline='' ) as csvFile:
        # Reading lines from the txt file
        lines = [line.rstrip() for line in txtFile]
        # Splitting lines with comma
        splitted = [line.split(',') for line in lines if len(line.split(',')) >= 2 ]
        # Create writer object for writing lines to CSV
        writer = csv.writer(csvFile)
        # Adding header for column names
        writer.writerow(('First Name', 'Count'))
        # Adding lines as rows
        writer.writerows(splitted)
        # Checking the number of lines written and the number of lines read
        if len(splitted) != len(lines):
            # Printing erorr explanations
            print(f'Please check {txtFileName}')
            print('Some errors found in the data structure of the file')
            print(f'Number of lines in txt file:{len(lines)}')
            print(f'Number of lines transferred:{len(splitted)}')
            print(f'Number of lines with error(s):{len(lines) - len(splitted)}')
        
# Calling function to create CSV file for the file named 2000_GirlsNames.txt
createCsvFileFromTextFile('2000_GirlsNames.txt', '2000_GirlsNames.csv')

# Calling function to create CSV file for the file named 2000_BoysNames.txt
createCsvFileFromTextFile('2000_BoysNames.txt', '2000_BoysNames.csv')

