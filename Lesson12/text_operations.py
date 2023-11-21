# Task 2: Creating a module for working with text data, including a function to count the number of words in a text.

# Simulating the text_operations module
class TextOperations:
    @staticmethod
    def count_words(text):
        return len(text.split())