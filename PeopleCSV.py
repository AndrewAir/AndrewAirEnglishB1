import csv

# Define the header row
header = ['Name', 'Age', 'City']

# Define the data rows
data = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'San Francisco'],
    ['Charlie', 35, 'London']
]

# Open a file for writing
with open('people.csv', 'w', newline='') as file:

    # Create a CSV writer object
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(header)

    # Write the data rows
    for row in data:
        writer.writerow(row)

