# The goal of the exercise is to create a class that will help you analyze a specific text. A text can be just a simple string,
# like “Today, is a happy day” or it can be an external text file.

# Part I
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.
# Hint: You need to manually copy-paste the text, straight into the code

# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace) return None or a meaningful message.
# a method that returns the most common word in the text.
# a method that returns a list of all the unique words in the text.


# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.

# Implement a classmethod that returns a Text instance but with a text file:

#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.


# Now, use the provided the_stranger.txt file and try using the class you created above.



# Bonus:
# Create a class called TextModification that inherits from Text.

# Implement the following methods:
# a method that returns the text without any punctuation.
# a method that returns the text without any english stop-words (check out what this is !!).
# a method that returns the text without any special characters.
# Note: Instead of creating a child class, you could also implements those methods as static methods in the Text class.

# Note: Feel free to implement/create any attribute, method or function needed to make this work, be creative :)

import string
from collections import Counter
# import nltk
# from nltk.corpus import stopwords

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        words = self.text.lower().split()
        word_count = Counter(words)
        return word_count.get(word, "Word not found")

    def most_common_word(self):
        words = self.text.lower().split()
        word_count = Counter(words)
        return word_count.most_common(1)[0][0]

    def unique_words(self):
        words = self.text.lower().split()
        return list(set(words))

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as file:
            text = file.read()
        return cls(text)

# class TextModification(Text):
#     def remove_punctuation(self):
#         translator = str.maketrans('', '', string.punctuation)
#         return self.text.translate(translator)

#     def remove_stopwords(self):
#         nltk.download('stopwords', quiet=True)
#         stop_words = set(stopwords.words('english'))
#         words = self.text.lower().split()
#         filtered_words = [word for word in words if word not in stop_words]
#         return ' '.join(filtered_words)

#     def remove_special_characters(self):
#         return ''.join(char for char in self.text if char.isalnum() or char.isspace())

# Test with a simple string
simple_text = "A good book would sometimes cost as much as a good house."
simple_text_analysis = Text(simple_text)
print("Frequency of 'good':", simple_text_analysis.word_frequency('good'))
print("Most common word:", simple_text_analysis.most_common_word())
print("Unique words:", simple_text_analysis.unique_words())

# Test with an external text file
stranger_text_analysis = Text.from_file("c:/Users/97258/OneDrive - Université de Franche-Comté (univ-fcomte.fr)/Bureau/DI-Bootcamp/Week3/Day4/DailyChallenge/the_stranger.txt")
print("Frequency of 'the':", stranger_text_analysis.word_frequency('the'))
print("Most common word:", stranger_text_analysis.most_common_word())
print("Unique words:", stranger_text_analysis.unique_words())

# Test text modification methods
# modified_text = "This is a test text! It contains some punctuation, stopwords like 'is' and 'a', and some special characters %$#@"
# text_modification = TextModification(modified_text)
# print("Text without punctuation:", text_modification.remove_punctuation())
# print("Text without stopwords:", text_modification.remove_stopwords())
# print("Text without special characters:", text_modification.remove_special_characters())


# import os


# def file_exists(filename, path=os.getcwd()):
#     print(path)
#     """
#     Check if the specified file exists at the specified directory
#     """
#     files = os.listdir(path)
#     return filename in files

# print(file_exists('the_stranger.txt'))
