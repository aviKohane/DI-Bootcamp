
# Using the code , implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}{'s' if self.amount>1 else ''}"

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f"{self.amount} {self.currency}{'s' if self.amount>1 else ''}"

    def __add__(self, other):
        if isinstance(other, int):
            return Currency(self.currency, self.amount + other)
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return Currency(self.currency, self.amount + other.amount)
        else:
            raise TypeError("Unsupported operand type for +")

    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
            return self
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
            return self
        else:
            raise TypeError("Unsupported operand type for +")

# Test cases
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))  # Output: '5 dollars'
print(int(c1))  # Output: 5
print(repr(c1))  # Output: '5 dollars'
print(c1 + 5)   # Output: 10
print(c1 + c2)  # Output: 15
print(c1)       # Output: 5 dollars
c1 += 5
print(c1)       # Output: 10 dollars
c1 += c2
print(c1)       # Output: 20 dollars
# print(c1 + c3)  # Output: TypeError: Cannot add between Currency type <dollar> and <shekel>


# 🌟 Exercise 3: String Module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module
import random
import string

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

random_string = generate_random_string(5)
print("Random string of length 5:", random_string)


# 🌟 Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.
import datetime

def display_current_date():
    current_date = datetime.datetime.now().date()
    print("Current date:", current_date)

# Call the function to display the current date
display_current_date()

# Exercise 5 : Amount Of Time Left Until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).
import datetime
def time_until_january_first():
    current_date = datetime.datetime.now()
    january_first = datetime.datetime(current_date.year + 1, 1, 1)
    time_left = january_first - current_date
    days_left = time_left.days
    hours_left, remainder = divmod(time_left.seconds, 3600)
    minutes_left, seconds_left = divmod(remainder, 60)

    print(f"The 1st of January is in {days_left} days and {hours_left}:{minutes_left}:{seconds_left} hours.")

# Call the function to display the time left until January 1st
time_until_january_first()


# Exercise 6 : Birthday And Minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), 
# then displays a message stating how many minutes the user lived in his life.
import datetime

def minutes_lived(birthdate):
    current_date = datetime.datetime.now()
    difference = current_date - birthdate
    minutes = difference.total_seconds() / 60
    print(f"You have lived for {int(minutes)} minutes.")

# Example usage:
birthdate = datetime.datetime(1998, 7, 18)  # Example birthdate
minutes_lived(birthdate)

# Exercise 7 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. 
# Use faker to populate them with fake data.

from faker import Faker

# Initialize Faker
fake = Faker()

# Create an empty list called users
users = []

# Create a function to add new dictionaries to the users list
def add_user():
    user = {
        'name': fake.name(),
        'address': fake.address(),
        'language_code': fake.language_code()
    }
    users.append(user)

# Call the add_user function to populate the users list
for _ in range(5):  # Add 5 users for example
    add_user()

# Print the populated users list
print(users)
# I can't get the faker module to work even though I installed it as indicated in the documentation.
# I ll enjoy help to make my faker module work. 