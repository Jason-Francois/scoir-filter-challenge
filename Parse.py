#!/usr/bin/python

# Parse.py - Handles all code 
# related to parsing the csv file

import csv, sys, os;

#Returns the records in the csv file
#Matching the input values
def parseCSV(parseInfo):
    fields = []
    rows = []
    fileName = parseInfo["fileName"]
    with open(fileName, "r") as csvFile:
        csvReader = csv.reader(csvFile)
        fields = next(csvReader)
        fieldIndex = fields.index(parseInfo["field"])
        
        for row in csvReader:
            if(row[fieldIndex] == parseInfo["fieldValue"]):
                rows.append(row)
                
    return rows

