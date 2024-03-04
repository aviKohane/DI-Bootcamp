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

