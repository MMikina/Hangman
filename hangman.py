import random
import string

# Lista słów do zgadnięcia
WORDS = ["python", "komputer", "algorytm", "programowanie", "hangman"]

def choose_word(words):
    return random.choice(words)

def display_state(secret_word, guessed_letters):
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )

def hangman():
    secret_word = choose_word(WORDS)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    print("Witaj w Hangman!\n")
    while wrong_guesses < max_wrong:
        print(f"Słowo: {display_state(secret_word, guessed_letters)}")
        guess = input("Podaj literę: ").lower()

        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("Proszę podać jedną literę.")
            continue
        if guess in guessed_letters:
            print("Ta litera została już zgadnięta.")
            continue

        guessed_letters.add(guess)
        if guess not in secret_word:
            wrong_guesses += 1
            print(f"Zła litera. Pozostało prób: {max_wrong - wrong_guesses}")
        else:
            print("Dobra litera!")

        if all(letter in guessed_letters for letter in secret_word):
            print(f"Wygrałeś! Słowo to: {secret_word}")
            break
    else:
        print(f"Przegrałeś. Słowo to: {secret_word}")

if __name__ == "__main__":
    hangman()
