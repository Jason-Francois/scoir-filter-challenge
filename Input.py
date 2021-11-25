# Input.py: Handles all user input functionality

# Returns a dict {field: field, value: value} based on user input
def getValidInput():

    # Get input for the field
    validInputs = ["first_name", "last_name", "year"]
    userFieldInput = ""
    while not userFieldInput.lower() in validInputs:
        userFieldInput = input(
            "Enter a desired filter (first_name, last_name, or year):\n"
        )

    # Gets input for the field value
    userValueInput = input("Enter value for field:\n")
    return {"field": userFieldInput, "fieldValue": userValueInput}
