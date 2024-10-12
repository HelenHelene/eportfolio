# e-Portfolio activity: Improving Code Quality

## Introduction
Refer to the [Mertz (2019)](https://docslib.org/doc/9751240/writing-clean-and-pythonic-code) resource.  
Use some Python code which I have developed in the past and apply at least 3 of the strategies presented at the source to improve its quality. 

### Original Python code
Below is the Python code developed in the past

```python
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
    # If myPhoneBook is is not empty, run bubble sort
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
```

<br>

### Improved Python code
To improve the above Python code, I'll apply three strategies from the "Writing Clean and Pythonic Code" resource:

 - **Use Tools to Help You:** Use black for auto-formatting to ensure consistent style.
 - **Follow a Style Guide:** Adhere to PEP 8, including naming conventions and indentation.
 - **Document All the Things:** Add docstrings for better understanding.

Here's the improved code:

```python
# Phone Book Application

my_phone_book = {}

def main_menu():
    """Display the main menu options."""
    print("\nWelcome to the Main Menu")
    print("1. Display all contacts")
    print("2. Insert a new contact")
    print("3. Delete an existing contact")
    print("4. Sort contacts")
    print("5. Search for a contact")
    print("6. Exit\n")

def display_contact():
    """Display all contacts in the phone book."""
    if my_phone_book:
        for name, number in my_phone_book.items():
            print(name, ":", number)
    else:
        print("\nPhone Book is empty. Return to Main Menu.\n")

def insert_contact():
    """Insert a new contact into the phone book."""
    name_input = input("Enter contact name: ")
    name = name_input.upper()
    number = input("Enter phone number: ")
    if name not in my_phone_book:
        my_phone_book[name] = number
        print("\nContact successfully added.\n")
    else:
        print("\nContact already exists.\n")

def delete_contact():
    """Delete a contact from the phone book."""
    name_input = input("Enter the name of the contact to delete: ")
    name = name_input.upper()
    if name in my_phone_book:
        confirm = input(f"Please confirm to delete {name}, yes or no: ")
        if confirm.lower() == "yes":
            del my_phone_book[name]
            print("\nContact successfully deleted.\n")
        else:
            print("\nReturn to Main Menu.\n")
    else:
        print("\nContact not found.\n")

def sort_contact():
    """Sort and display contacts alphabetically."""
    if my_phone_book:
        sorted_contacts = sorted(my_phone_book.items())
        print("\nContacts sorted by alphabetical order:")
        for name, number in sorted_contacts:
            print(name, ":", number)
    else:
        print("\nPhone Book is empty. Return to Main Menu.\n")

def search_contact():
    """Search for a contact by name."""
    name_input = input("Enter the name to search: ")
    name = name_input.upper()
    if name in my_phone_book:
        print(name, ":", my_phone_book[name])
    else:
        print("\nContact not found.\n")

def my_phone_book_app():
    """Run the Phone Book Application."""
    while True:
        main_menu()
        option = input("Enter your option (1, 2, 3, 4, 5, or 6): ")
        if option == "1":
            display_contact()
        elif option == "2":
            insert_contact()
        elif option == "3":
            delete_contact()
        elif option == "4":
            sort_contact()
        elif option == "5":
            search_contact()
        elif option == "6":
            print("\nExiting the application.\n")
            break
        else:
            print("\nInvalid input, please try again.\n")

if __name__ == "__main__":
    my_phone_book_app()
```

<br>

Above code with following improvements:
 - **Naming:** Used snake_case for variable and function names.
 - **Docstrings:** Added docstrings for all functions to describe their purpose.
 - **Formatting:** Ensured consistent use of spaces and adherence to PEP 8 line length.
<br><br>

## Reflections
Reflecting on the assignment, I learned the importance of writing clean and Pythonic code by adhering to PEP 8 standards, using tools like black for formatting, and incorporating meaningful documentation. These practices not only enhance code readability and maintainability but also streamline collaboration in team settings. By consistently applying these techniques, I can produce more efficient and professional code in future assignments, making it easier to debug and extend as needed.

<br><br>

---

## Reference
Mertz, J. (2019) Writing Clean and Pythonic Code. Available from: https://docslib.org/doc/9751240/writing-clean-and-pythonic-code 

<br><br>

---

[Return to Module 5 Unit 9](SEPM_Unit09.md)
