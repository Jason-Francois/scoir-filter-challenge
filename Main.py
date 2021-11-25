import sys, Parse, Validation, Input

# Main.py - driver module
# Driver function, validates the command arguments,
# Gets user input, and then parses the file

def run():
    args = sys.argv
    outputRows = []
    if (Validation.validate(args)):
        
        # Get the records from the csv file
        parseInfo = Input.getValidInput()
        parseInfo["fileName"] = args[1]
        outputRows = Parse.parseCSV(parseInfo)
        
        # Print the results
        if len(outputRows) == 0:
            print("No records were found matching the user input")
        else:
            for row in outputRows:
                print(",".join(row))

if __name__ == "__main__":
    run()