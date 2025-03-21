#!/user/bin/env.python3
# Created by: Enoch Amedjrovi
# Created on: March 18
# This program creates a guessing game
import constants


def main():
    # guess the correct number
    user_number = int(input("Choose a number (1-9): "))
    print("")

    # check if it's correct
    if user_number == constants.CORRECT_NUMBER:
        print("Correct number!")
    # check if it's wrong
    if user_number != constants.CORRECT_NUMBER:
        print("Wrong number!")


if __name__ == "__main__":
    main()
