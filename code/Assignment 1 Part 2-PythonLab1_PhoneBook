# Phone Book Application
# Define each function individually and run a loop until the user chooses to exit the application.

# Define global variable to store contact
myPhoneBook = {}

# Define a function for main menu
def mainMenu():
    print("\nWelcome to the Main Menu")
    # Function ID: OPT01
    print("1. Display all contacts")
    # Function ID: OPT02
    print("2. Insert a new contact")
    # Function ID: OPT03
    print("3. Delete an existing contact")
    # Function ID: OPT04
    print("4. Sort contacts")
    # Function ID: OPT05
    print("5. Search for a contact")
    # Function ID: OPT06
    print("6. Exit\n")

# Define a function for OPT01-Display all contacts
def displayContact():
    # If myPhoneBook is not empty, loop through and output each key(name)-value(number) pair in myPhoneBook until all of them have been processed 
    if len(myPhoneBook) > 0:
        for myName, myNumber in myPhoneBook.items():
            print(myName, ":", myNumber)
    # If myPhoneBook is empty, output error message
    else:
        print("\nPhone Book is empty. Return to Main Menu.\n")

# Define a function for OPT02-Insert a new contact
def insertContact():
    # Get user input for contact name
    myNameAny = input("Enter contact name: ")
    # Convert input to upper case to ensure that the user input does not impact the case sensitivity
    myName = myNameAny.upper()
    # Get user input for phone number
    myNumber = input("Enter phone number: ")
    # If myName not exists
    if myName not in myPhoneBook:
        # add the input key-value pair to myPhoneBook and output successful message
        myPhoneBook[myName] = myNumber
        print("\nContact successfully added.\n")
    # If myName already exists, output error message 
    else:
        print("\nContact already exists.\n")

# Define a function for OPT03-Delete an existing contact
def deleteContact():
    # Get user input for the name of the contact to be deleted
    myNameAny = input("Enter the name of the contact to delete: ")
    # Convert input to upper case
    myName = myNameAny.upper()
    # If myName already exist
    if myName in myPhoneBook:
    # Get user confirmation for the deletion of myName
        confirm = input("Please confirm to delete " + myName + ", yes or no: ")
        # If confirmed yes is True, delete key-value pair of myName in myPhoneBook and output successful message
        if confirm.lower() == "yes":
            del myPhoneBook[myName]
            print("\nContact successfully deleted.\n")
        # if confirmed yes is False, output return to main menu message
        else:
            print("\nReturn to Main Menu.\n")
    # if myName not exsit, output error message
    else:
        print("\nContact not found.\n")

# Define a function for OPT04-Sort contacts
def sortContact():
    # Create a copy to avoid modifying the original contact list
    sortedContacts = list(myPhoneBook.keys())
    # If myPhoneBook is not empty, run bubble sort
    if len(myPhoneBook) > 0:
        n = len(sortedContacts)
        # Loop the swap function until all contacts have been processed and the last element is the greatest
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if sortedContacts[j] > sortedContacts[j + 1]:
                    # Swap if the element found is greater
                    sortedContacts[j], sortedContacts[j + 1] = sortedContacts[j + 1], sortedContacts[j]
       # Output a successful message and the sorted key-value pairs in sortedContacts
        print("\nContacts sorted by alphabetical order:")
        for myName in sortedContacts:
            print(myName, ":", myPhoneBook[myName])
    # If myPhoneBook is empty, output error message
    else:
        print("\nPhone Book is empty. Return to Main Menu.\n")

# Define a function for OPT05-Search for a contact
def searchContact():
    # Get user input for the name to search
    myNameAny = input("Enter the name to search: ")
    # Convert input to upper case
    myName = myNameAny.upper()
    # If myName already exist, output selected key-value pair in myPhoneBook
    if myName in myPhoneBook:
        print(myName, ":", myPhoneBook[myName])
    # if myName not exsit, output error message    
    else:
        print("\nContact not found.\n")

# Define Phone Book Application
def myPhoneBookApp():
    # Loop while myOption is True. Return to main menu after selected function completed, until myOption is '6'
    while True:
        mainMenu()
        # Get user input as integer
        myOption = input("Enter your option (1, 2, 3, 4, 5, or 6): ")
        # OPT01-Display all contacts
        if myOption == "1":
            displayContact()
        # OPT02-Insert a new contact
        elif myOption == "2":
            insertContact()
        # OPT03-Delete an existing contact
        elif myOption == "3":
            deleteContact()
        # OPT04-Sort contacts
        elif myOption == "4":
            sortContact()
        # OPT05-Search for a contact
        elif myOption == "5":
            searchContact()
        # OPT06-Exit the application
        elif myOption == "6":
            print("\nExiting the application.\n")
            break
        # If the user input is none of the above options, output an invalid input message
        else:
            print("\nInvalid input, please try again.\n")
            continue

# Run program
myPhoneBookApp()
