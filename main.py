import sqlite3
import os
import sys

DB_EXTENSION = ".db"
def main():

    # Initial script prompt
    print("Welcome to DBMakerPy!\n")

    # Check if the current working directory has any databases
    if any(file.endswith('.db') for file in os.listdir('.')):
        print("Database file(s) found:\n")

        # Loop through the directory and print out the names of all the databases
        for file in os.listdir('.'):
            if file.endswith('.db'):
                print(file)

    # No database files are found in the directory
    # Ask the user if they would like to start one
    else:
        user_input = input("No database file(s) found. Would you like to make one? [Y/n] ")

        if user_input == "" or "y" == user_input.lower():
            database_name = input("Enter database name: ")

            if database_name.find(DB_EXTENSION) == -1: # the string used does not have the database extension
                database_name += DB_EXTENSION
            
            print("Database name is:", database_name)






if __name__ == "__main__":
    main()