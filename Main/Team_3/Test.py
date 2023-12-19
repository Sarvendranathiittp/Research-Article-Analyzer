import csv

# Specify the path to your CSV file
csv_file_path = 'Research-Article-Analyzer/Resources/Scientist_Names/Top_scientists_2022.csv'
list=[]
# Open the CSV file
with open(csv_file_path, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        # Access the first column (index 0) in each row
        list.append(row[0].split(','))
        #first_column_value = row[0]
    
        # Do something with the value from the first column
#print(list)
str = 'Isaac Newton'
print(str in list)

