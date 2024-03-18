# 🌟 Exercise 1 – Random Sentence Generator
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user 
# how long the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.

# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. 
# What is the correct data type to store the words?

# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), the sentence should be lower case.

# Create a function called main which will:

# Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.

# import random

# def get_words_from_file(filename):
#     with open(filename, 'r') as file:
#         words = file.read().splitlines()
#     return words

# def get_random_sentence(length, words):
#     sentence = ' '.join(random.choices(words, k=length))
#     return sentence.lower()

# def main():
#     print("Welcome to the Random Sentence Generator!")
#     print("This program generates a random sentence based on the words from a file.")
#     try:
#         length = int(input("How long do you want the sentence to be? (Enter a number between 2 and 20): "))
#         if length < 2 or length > 20:
#             raise ValueError("Sentence length must be between 2 and 20")
#     except ValueError as ve:
#         print("Error:", ve)
#         return

#     words = get_words_from_file("word_list.txt")
#     sentence = get_random_sentence(length, words)
#     print("Random sentence:", sentence)

# if __name__ == "__main__":
#     main()
    
# 🌟 Exercise 2: Working With JSON
# Instructions
import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""


# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.
import json

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Load JSON string to dictionary
data = json.loads(sampleJson)

# Access the nested "salary" key
salary = data['company']['employee']['payable']['salary']
print("Salary:", salary)

# Add a key called "birth_date" at the same level as the "name" key
data['company']['employee']['birth_date'] = "1998-07-18"

birthDate=data['company']['employee']['birth_date']
print("BirthDate:", birthDate)
# Save the dictionary as JSON to a file
with open("output.json", "w") as outfile:
    json.dump(data, outfile, indent=4)

print("Data saved to output.json")
