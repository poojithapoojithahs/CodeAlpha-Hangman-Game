import random
words = ["python", "computer", "science", "student", "program"]
word = random.choice(words)

guessed_letters = []
max_attempts = 6
attempts_left = max_attempts

print("===================================")
print("       HANGMAN GAME")
print("===================================")
print("Guess the word one letter at a time.")
print(f"You have {max_attempts} wrong guesses.\n")

while attempts_left > 0:

    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)

    if "_" not in display_word:
        print("\n Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print(" correct!\n")
    else:
        attempts_left -= 1
        print("Wrong!")
        print("Remaining wrong guesses:", attempts_left, "\n")
        
if attempts_left == 0:
    print(" Game Over!")
    print("The correct word was:", word)

print("\nThank you for playing Hangman!")