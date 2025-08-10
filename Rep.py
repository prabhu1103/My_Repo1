# text = "Python"
# print (text[2:-1:2])

import random

# Word list
words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

# Step 1: Pick a random word
original_word = random.choice(words)

# Step 2: Scramble the word
scrambled_word = ''.join(random.sample(original_word, len(original_word)))

print(original_word)
print("Welcome to the Word Unscramble Game!")
print(f"Your scrambled word is: {scrambled_word}")

# Step 3: Loop for multiple attempts
while True:
    guess = input("Enter your guess (or type 'quit' to exit): ").strip().lower()
    
    if guess == 'quit':
        print(f"You quit! The word was: {original_word}")
        break
    elif guess == original_word:
        print("🎉 Correct! Well done.")
        break
    else:
        print("❌ Wrong guess, try again!")