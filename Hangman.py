import random
from Face_detector import word_list


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    name = input("Welcome to hangman, What is your name?")
    print("Hi, " + name + "lets play hangman")
    print(hangman_display(tries))
    print(word_completion)
    print("You have 6 chances!!!")
    while not guessed and tries > 0:
        guess = input("Enter a letter or a word here: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter!!")
            elif guess not in word:
                print("This letter in not in the word :(")
                tries -= 1
                print(hangman_display(tries))
                guessed_letters.append(guess)
            else:
                print("Great!! You found one letter ")
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(guess) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed this word")

            elif guess != word:
                print("That is not the word")
                guessed_words.append(guess)

            else:
                guessed = True
                word_completion = word
        else:
            print("Wrong guess!!")
            print(hangman_display(tries))
            print(word_completion + "\n")
            if guessed:
                print("CONGRATULATIONS YOU WIN!!!")
            else:
                print("sorry you ran out of tries")



def hangman_display(tries):
    stages = [
        " - - - -\n"
        " |      |\n"
        " |      0\n"
        " |\n"
        " |\n"
        " |\n"
        "___",
        " - - - -\n"
        " |      |\n"
        " |      0\n"
        " |      |\n"
        " | \n"
        " | \n"
        "___",
        " - - - -\n"
        " |      |\n"
        " |      0\n"
        " |      |\n"
        " |      |\n"
        " | \n"
        "___",
        " - - - -\n"
        " |      |\n"
        " |      0\n"
        " |      |\n"
        " |      |\n"
        " |     / \n"
        "___",
        " - - - -\n"
        " |      |\n"
        " |      0\n"
        " |      |\n"
        " |      |\n"
        " |     / \\\n"
        "___",
        " - - - -\n"
        " |      |\n"
        " |      0\n"
        " |     \|\n"
        " |      |\n"
        " |     / \\\n"
        "___",
        " - - - -\n"
        " |      |\n"
        " |      0\n"
        " |     \|/\n"
        " |      |\n"
        " |     / \\\n"
        "___"
    ]
    stages.reverse()
    return stages[tries]


def event():
    word = get_word()
    play(word)
    while input("Would you want to play again").upper() == "yes":
        word = get_word()
        play(word)


if __name__ == "__main__":
   event()



