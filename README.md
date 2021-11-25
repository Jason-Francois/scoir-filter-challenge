# csv-filter-challenge-public

## How-To
1. To run the program, from the root directory, run `python3 Main.py <path to CSV file>`.
2. It is important to remember to run this program with `python3` as opposed to `python` because it will crash if ran with `python`.
3. The Main.py script will ask the user to select a field from the csv file, and then ask the user what they would like the filter value to be.
4. The script will then output the records in the CSV file that contain the filter value, if there are any.
5. For example, `python3 Main.py test.csv` will print the following:
```
Ken,Thompson,19430204
Billy,Thompson,19710225
```
## Assumptions
- The CSV file is formatted correctly (All fields are in the correct place)
- That all input values are valid (names are strings, dates are in correct format, etc.)

# Instructions
1. Click "Use this template" to create a copy of this repository in your personal github account.  
1. Using technology of your choice, complete assignment listed below.
1. Update the README in your new repo with:
    * a `How-To` section containing any instructions needed to execute your program.
    * an `Assumptions` section containing documentation on any assumptions made while interpreting the requirements.
1. Send an email to Scoir (andrew@scoir.com) with a link to your newly created repo containing the completed exercise.

## Expectations
1. This exercise is meant to drive a conversation. 
1. Please invest only enough time needed to demonstrate your approach to problem solving, code design, etc.
1. Within reason, treat your solution as if it would become a production system.

## Assignment
Create a command line application that parses a CSV file and filters the data per user input.

The CSV will contain three fields: `first_name`, `last_name`, and `dob`. The `dob` field will be a date in YYYYMMDD format.

The user should be prompted to filter by `first_name`, `last_name`, or birth year. The application should then accept a name or year and return all records that match the value for the provided filter. 

Example input:
```
first_name,last_name,dob
Bobby,Tables,19700101
Ken,Thompson,19430204
Rob,Pike,19560101
Robert,Griesemer,19640609
```
