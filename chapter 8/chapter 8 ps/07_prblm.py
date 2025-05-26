
# 7. Write a python function to remove a given word from a list ad strip it at the same 
# time. 
# Function to remove a given word from a list and strip all items
def remove_word_and_strip(words_list, word_to_remove):
    # Strip each word and exclude the one that matches the word_to_remove
    return [word.strip() for word in words_list if word.strip() != word_to_remove]



   
    # Original list with extra spaces
words = ["  apple", "banana  ", "  orange ", "banana", "grape  "]
    
    # Word to remove
word_to_remove = "banana"

    # Get the cleaned list
cleaned_list = remove_word_and_strip(words, word_to_remove)

    # Display the result
print("Original list:", words)
print(f"List after removing '{word_to_remove}':", cleaned_list)
