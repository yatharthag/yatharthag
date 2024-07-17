import pandas as kullu

# Read data from a CSV file
data = kullu.read_csv('data.csv')

# Calculate the average of a specific column
average = data['marks'].mean()

print(f'The average is: {average}')
