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


