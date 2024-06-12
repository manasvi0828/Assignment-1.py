import csv
with open('annual-enterprise-survey-2021-financial-year-provisional-csv.csv', mode='r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)