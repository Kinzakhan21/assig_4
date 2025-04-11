import random

# List of words
words = ["python", "flower", "hangman", "sunshine", "program", "apple", "keyboard"]

# Randomly choose a word
word = random.choice(words)
guessed = "_" * len(word)
tries = 6
guessed_letters = []

print("🎉 Welcome to Hangman!")
print("Word:", guessed)

while tries > 0 and guessed != word:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        guessed = "".join([letter if letter in guessed_letters else "_" for letter in word])
        print("✅ Correct!")
    else:
        tries -= 1
        print("❌ Wrong! Tries left:", tries)

    print("Word:", guessed)

if guessed == word:
    print("🎉 Congratulations! You guessed the word:", word)
else:
    print("😞 Game Over! The word was:", word)
