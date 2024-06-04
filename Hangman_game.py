import random

def generate_word(alphabet, length):
    """Generates a random word of the specified length from the given alphabet."""
    word = ""
    for _ in range(length):
        index = random.randint(0, len(alphabet) - 1)
        word += alphabet[index]
    return word

def play_game(word):
    """Plays a hangman game with the given word."""
    guessed_letters = set()
    max_guesses = len(word) // 2
    game_over = False

    print("Le nombre de guess que vous avez sont :", max_guesses)

    while not game_over:
        print("\nEntrez une lettre : ")
        guess = input().lower()

        if guess in guessed_letters:
            print("Vous avez déjà deviné cette lettre.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Mot :", end=" ")
            for letter in word:
                if letter in guessed_letters:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")

            if word == "".join(guessed_letters):
                print("\nBravo, vous avez trouvé le mot !")
                game_over = True
        else:
            max_guesses -= 1
            print("Lettre incorrecte. Il vous reste", max_guesses, "essais.")

            if max_guesses == 0:
                print("Vous avez perdu. Le mot était", word)
                game_over = True

if __name__ == "__main__":
    alphabet = "abcdefjhigklmnopqrstuvwxyz"
    word_length = int(input("Entrez le nombre de lettres dans le mot : "))
    word = generate_word(alphabet, word_length)
    play_game(word)