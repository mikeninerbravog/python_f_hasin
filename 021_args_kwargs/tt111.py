# Example 2: Join Strings

# Define a function that joins a variable number of words into a sentence.
def join_strings(*words):
    sentence = ' '.join(words)  # Using the ' '.join() method to concatenate words with spaces.
    return sentence  # Return the created sentence.


# Call the join_strings() function with a sequence of words as arguments.
result = join_strings('Hello', 'world', 'from', 'Python!')

# Print the result of the string concatenation.
print(result)  # Output: Hello world from Python!
