This lab will focus on using polymorphism while interacting with a contact list. 
There will be a main class Contacts that controls the “view” the user sees and responds to user input. 
The contact information (personal and work) will be an instance of the Information class.

```python

# Polymorphism Tutorial Lab 1

# The Contacts Class
class Contacts:
  def __init__(self):
    self.view = 'quit'
    self.contact_list = []
    self.choice = None
    self.index = None

  # The Display Method
  def display(self):
    while True:
      if self.view == 'list':
        self.show_list()
      elif self.view == 'info':
        self.show_info()
      elif self.view == 'add':
        print()
        self.add_contact()
      elif self.view == 'quit':
        print('\nClosing the contact list...\n')
        break

  # Starting the Other Methods
  def show_list(self):
    pass

  def show_info(self):
    pass

  def add_contact(self):
    pass

#Testing Your Code
contacts = Contacts()
contacts.display()
```

Polymorphism Tutorial Lab 1 Output

<img src="OOP_Unit08_RecursiveTree.jpg" alt="Recursive Tree" width="500"/>

---

```python
# Polymorphism Tutorial Lab 2

# Adding a Contact
class Contacts:
  def __init__(self):
    self.view = 'list'
    self.contact_list = []
    self.choice = None
    self.index = None
  
  def display(self):
    while True:
      if self.view == 'list':
        self.show_list()
      elif self.view == 'info':
        self.show_info()
      elif self.view == 'add':
        print()
        self.add_contact()
      elif self.view == 'quit':
        print('\nClosing the contact list...\n')
        break

  def show_list(self):
    print()
    if len(self.contact_list) == 0:
      self.choice = input('(A)dd a new contact \n(Q)uit \n> ').lower()
    else:
      self.view = 'quit'
    self.handle_choice()

  def show_info(self):
    pass

  #Adding a Contact
  def __add__(self, new_contact):
    self.contact_list.append(new_contact)

  def add_contact(self):
    self + Information()
    self.view = 'list'

  # Handling User Choices
  def handle_choice(self):
    if self.choice == 'q':
      self.view = 'quit'
    elif self.choice == 'a' and self.view == 'list':
      self.view = 'add'

#  The Information Class
class Information:
  def __init__(self):
    self.first_name = input('Enter their first name: ')
    self.last_name = input('Enter their last name: ')
    self.personal_phone = input('Enter their personal phone number: ')
    self.personal_email = input('Enter their personal email address: ')
    self.work_phone = input('Enter their work phone number: ')
    self.work_email = input('Enter their work email address: ')
    self.title = input('Enter their work title: ')

contacts = Contacts()
contacts.display()
print(len(contacts.contact_list))
```

Polymorphism Tutorial Lab 2 Output

<img src="OOP_Unit08_RecursiveTree.jpg" alt="Recursive Tree" width="500"/>

---

[Return to Module 2 Unit 8](OOP_Unit08.md)
