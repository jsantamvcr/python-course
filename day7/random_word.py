import random
    
word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

def get_random_word():
    return random.choice(word_list)

word = get_random_word()
print(f"The random word is: {word}")