

```python
# Exercise 16.2

"""Use the datetime module to write a program that gets the current date and prints the day of the week."""

import datetime

# Get the current date
current_date = datetime.date.today()

# Print the day of the week
day_of_week = current_date.strftime("%A")
print("Today is", day_of_week)


"""Write a program that takes a birthday as input and 
prints the user's age and the number of days, hours, minutes and seconds until their next birthday."""

# Get the user's birthday
birthday_str = input("Enter your birthday (YYYY-MM-DD): ")
birthday = datetime.datetime.strptime(birthday_str, "%Y-%m-%d").date()

# Calculate the age
age = current_date.year - birthday.year

# Check if the birthday has passed this year
if current_date.month < birthday.month or (current_date.month == birthday.month and current_date.day < birthday.day):
    age -= 1

# Calculate the next birthday
next_birthday = datetime.date(current_date.year, birthday.month, birthday.day)
if current_date > next_birthday:
    next_birthday = datetime.date(current_date.year + 1, birthday.month, birthday.day)

# Calculate the time until the next birthday
time_until_next_birthday = next_birthday - current_date

# Print the age and time until the next birthday
print("Age:", age)
print("Time until next birthday:", time_until_next_birthday)

"""For two people born on different days, there is a day when one is twice as old as the other. 
That's their Double Day. Write a program that takes two birthdays and computes their Double Day."""

# Get the first person's birthday
birthday1_str = input("Enter the first person's birthday (YYYY-MM-DD): ")
birthday1 = datetime.datetime.strptime(birthday1_str, "%Y-%m-%d").date()

# Get the second person's birthday
birthday2_str = input("Enter the second person's birthday (YYYY-MM-DD): ")
birthday2 = datetime.datetime.strptime(birthday2_str, "%Y-%m-%d").date()

# Initialize the start date
start_date = max(birthday1, birthday2)

# Find the Double Day
while True:
    age1 = start_date.year - birthday1.year
    age2 = start_date.year - birthday2.year
    if age1 == 2 * age2 or age2 == 2 * age1:
        double_day = start_date
        break
    start_date += datetime.timedelta(days=1)

# Print the Double Day
print("The Double Day is:", double_day)

```

    Today is Wednesday
    Enter your birthday (YYYY-MM-DD): 1980-01-01
    Age: 44
    Time until next birthday: 259 days, 0:00:00
    Enter the first person's birthday (YYYY-MM-DD): 1985-06-30
    Enter the second person's birthday (YYYY-MM-DD): 1970-01-01
    The Double Day is: 2000-01-01



```python

```
