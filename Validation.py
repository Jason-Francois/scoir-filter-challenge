# Validation.py: Handles all argument validation
import os.path


# Validates command line arguments
def validate(args):

    # Check if the num file arguements is correct
    if len(args) != 2:
        print("Invalid number of arguments. Only enter one csv file")
        return False

    # Check if the file exists
    if not os.path.exists(args[1]):
        print("File does not exist.")
        return False

    # Check if the file is a csv file
    if not args[1].lower().endswith(".csv"):
        print("File not csv. Run script with csv file")
        return False

    # Check if file is empty
    if os.path.getsize(args[1]) == 0:
        print("File is empty.")
        return False
    else:
        return True
