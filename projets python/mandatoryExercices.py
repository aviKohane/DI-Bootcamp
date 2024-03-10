# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers={5,7,8,99,24}
my_fav_numbers.add(2)
my_fav_numbers.add(12)
print(my_fav_numbers)
my_fav_numbers.pop()

friend_fav_numbers={45,58,66,1,8}
our_fav_numbers=my_fav_numbers.union(friend_fav_numbers)

#Given a tuple which value is integers, it's not possible to add more integers to the tuple.


# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove('Banana')
basket.remove('Blueberries')
basket.append('Kiwi')
basket.insert(0, 'Apples')
counter=0
for i in basket:
    if i == "Apples":
        counter+=1

basket.clear()
print(basket)

# ---------------------------------------------------------------------------------------------------------------------------------

#🌟 Exercise 4: Floats
#Recap – What is a float? What is the difference between an integer and a float?
#Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
#Can you think of another way to generate a sequence of floats?

#float stores floating-point values, that is, values that have potential decimal places
#int only stores integral values, that is, whole numbers
#To create a list containing the sequence without hard-coding it, you can use a loop to generate the numbers in the sequence:
sequence1 = []
for i in range(1, 5):
    sequence1.append(i + 0.5)
    sequence1.append(i + 1.0)
    print(sequence1)
#Another way to generate a sequence of floats is :
sequence2 = [x / 2 + 0.5 for x in range(2, 10, 1)]
print(sequence2)

# ---------------------------------------------------------------------------------------------------------------------------------


#🌟 Exercise 5: For Loop
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
num_list=[]
for x in range(1,21):
    num_list.append(x)
   
print(num_list)  

for i in range(1, 21):
    if i % 2 == 0:
        print(i)
        
#---------------------------------------------------------------------------------------------------------------------------------

# Write a while loop that will continuously ask the user for their name, 
# unless the input is equal to your name.
# my_name = "jeremy berrebi"
# user_name = ""
# while user_name != my_name:
#     user_name = input("Please enter your name: ")
#     if user_name != my_name:
#         print("That's not my name. Please try again.")
# print("Welcome, jeremy berrebi!")

# Ask the user to input their favorite fruit(s)
favorite_fruits_str = input("Please enter your favorite fruit(s), separated by a single space: ")

# Convert the string of words into a list of words
favorite_fruits_list = favorite_fruits_str.split()

# Ask the user to input a name of any fruit
chosen_fruit = input("Now, please enter the name of any fruit: ")

# Check if the user's input is in the favorite fruits list
if chosen_fruit in favorite_fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy!")

#---------------------------------------------------------------------------------------------------------------------------------

# Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings,
# when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message 
# saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings 
# on the pizza pie and what the total price is (10 + 2.5 for each topping).

toppings = []
total_price = 10  # Base price for the pizza

# Loop to ask the user for pizza toppings
while True:
    topping = input("Enter a pizza topping (or 'quit' to finish): ")
    
    if topping.lower() == 'quit':
        break
    
    toppings.append(topping)
    total_price += 2.5  # Add $2.5 for each additional topping
    print("Adding", topping, "to your pizza.")

# Print all the toppings on the pizza
print("\nYour pizza toppings:")
for topping in toppings:
    print("- " + topping)

# Print the total price of the pizza
print("\nTotal price of your pizza: $", total_price)

#---------------------------------------------------------------------------------------------------------------------------------

# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.
# A group of teenagers are coming to your movie theater 
# and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, 
# if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

# Initialize variables to store ticket prices and total cost
ticket_price_under_3 = 0
ticket_price_3_to_12 = 10
ticket_price_over_12 = 15
total_cost = 0

# Ask the family the age of each person who wants a ticket
num_people = int(input("How many people are there in the family? "))
for person in range(1, num_people + 1):
    age = int(input(f"What is the age of person {person}? "))
    
    # Calculate ticket price based on age
    if age < 3:
        ticket_price = ticket_price_under_3
    elif 3 <= age <= 12:
        ticket_price = ticket_price_3_to_12
    else:
        ticket_price = ticket_price_over_12
    
    # Add ticket price to the total cost
    total_cost += ticket_price

# Print the total cost of all the family's tickets
print("Total cost of all tickets for the family:", total_cost)

# Given list of names
names_list=['jason','avi','levana','dan','lise']

# Initialize an empty list to store the names of teenagers permitted to watch the movie
allowed_names = []

# Ask each teenager for their age and check if they are permitted to watch the movie
for name in names_list:
    age = int(input(f"What is the age of {name}? "))
    
    # Check if the age is between 16 and 21 (inclusive)
    if 16 <= age <= 21:
        allowed_names.append(name)

# Print the final list of names of teenagers permitted to watch the movie
print("Final list of teenagers permitted to watch the movie:")
print(allowed_names)

# -----------------------------------------------------------------------------------


# Given list of sandwich orders
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# Remove all occurrences of "Pastrami sandwich" from sandwich_orders using a while loop
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

# Create an empty list to store finished sandwiches
finished_sandwiches = []

# Prepare the orders of the clients
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    finished_sandwiches.append(sandwich)
    print("I made your", sandwich.lower())

# Print a message listing each sandwich that was made
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print("- " + sandwich.lower())
