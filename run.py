'''Template exchange, originally written by the link:
https://elisabetebilini.github.io/hangman-game/
'''
import random
import re
from art import body_pieces, hang, positive
from words import word_list_easy, word_list_intermediate, word_list_hard
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_PLAYER = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_PLAYER.open('Hangman--game-project')

game_difficulty = ""


def update_scores(player_name, score, difficulty):
    worksheet = SHEET.worksheet("Scores")
    data = [player_name, score, difficulty]
    worksheet.append_row(data)


def display_scores():
    worksheet = SHEET.worksheet("Scores")
    scores = worksheet.get_all_values()[1:]
    scores.sort(key=lambda x: int(x[1]), reverse=True)
    print("\nPlayer Scores:")
    print("\nPlayer Name | Score | Difficulty")
    print("-" * 30)
    for row in scores:
        print(f"{row[0]:<11} | {row[1]:<5} | {row[2]:<10}")

    while input("\nPress Enter to return to the main menu.") != "":
        pass


print('Welcome to')
print(hang)


def display_instructions():
    print("\n----------------Instructions for Hangman:-----------------\n")
    print("→ The player can play alone or against another player.")
    print("→ The player can choose the difficulty level of the words.")
    print("→ The player(s) have 7 chances to discover the word.")
    print("→ The player must provide a name with at least 3 letters.")
    print("→ The number of letters in the word drawn is displayed.")
    print("→ At the end of the game, the secret word is revealed.")

    while input("\nPress Enter to return to the main menu.") != "":
        pass


select_word = ""
player_01 = ""
player_02 = ""


while True:
    print("\n1 - Instructions")
    print("2 - Player Scores")
    print("3 - Start Game")
    print("4 - Quit\n")

    while True:
        choice = input("Enter your choice: ")

        if choice.isdigit() and 1 <= int(choice) <= 4:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    if choice == '1':
        display_instructions()
    elif choice == '2':
        display_scores()
    elif choice == '3':
        while True:
            choice = input("Choose the game mode:\n1 - Single Player\n2 - Two Players\n")  # noqa
            if choice == '1' or choice == '2':
                break
            else:
                print("Invalid choice. Please enter '1' for Single Player or '2' for Two Players.")  # noqa

        if choice == '1':
            while True:
                game_difficulty = input("Choose the difficulty level:\n1 - Easy\n2 - Intermediate\n3 - Hard\n")  # noqa
                if game_difficulty == '1' or game_difficulty == '2' or game_difficulty == '3':  # noqa
                    break
                else:
                    print("Invalid option. Please choose 1, 2, or 3.")

            if game_difficulty == '1':
                select_word = random.choice(word_list_easy).upper()
            elif game_difficulty == '2':
                select_word = random.choice(word_list_intermediate).upper()
            else:
                select_word = random.choice(word_list_hard).upper()

            BOARD = []
            BLANKS = '_'
            CHANCES = 7
            GAME_OVER = False
            used_letters = []

            for letter in range(len(select_word)):
                BOARD += BLANKS

            # get player's name
            while True:
                player = input("Player, enter your name: \n").upper()
                if re.match(r'^[A-Z]{3,}$', player):
                    break
                else:
                    print("Invalid name. Please enter a name with at least 3 letters and containing only letters.")  # noqa

            print("Number of letters in the secret word: ", len(select_word))

            atual_player = player

            # identifying player
            while not GAME_OVER:
                print('Secret Word: ' + ''.join(BOARD))
                print("Used Letters:", ', '.join(used_letters))

                while True:
                    letter_player = input("Type one letter: \n").upper()
                    if len(letter_player) == 1 and letter_player.isalpha():
                        if re.match(r'^[A-Z]{3,}$', letter_player):
                            break
                        if letter_player in used_letters:
                            print("You've already used this letter.")
                        else:
                            used_letters.append(letter_player)
                        break
                    else:
                        print("Invalid input. Please enter a single letter.")
                        CHANCES -= 1
                        print(body_pieces[CHANCES])

                        if CHANCES == 0:
                            GAME_OVER = True
                            print("Beware, words can also kill!")
                            print(f'{player}, you lost the game.')
                            print(f'The secret word was: {select_word}.')
                            break

                # Checking Letter and spaces
                HAS_LETTER = False
                for letter_position in range(len(select_word)):
                    letter = select_word[letter_position]
                    if letter == letter_player:
                        BOARD[letter_position] = letter
                        HAS_LETTER = True

                if not HAS_LETTER:
                    CHANCES -= 1
                    if CHANCES < 0:
                        CHANCES = 0
                    print(body_pieces[CHANCES])

                    if CHANCES == 0:
                        GAME_OVER = True
                        print("Beware, words can also kill!")
                        print(f'{player}, you lost the game.')
                        print(f'The secret word was: {select_word}.')
                        break

                if BLANKS not in BOARD:
                    GAME_OVER = True
                    print("Congratulations, you survived!")
                    print(f'{atual_player} won the game.')
                    print(f'The secret word was: {select_word}.')
                    update_scores(player, CHANCES, game_difficulty)

        elif choice == '2':
            while True:
                game_difficulty = input("Choose the difficulty level:\n1 - Easy\n2 - Intermediate\n3 - Hard\n")  # noqa
                if game_difficulty == '1' or game_difficulty == '2' or game_difficulty == '3':  # noqa
                    break
                else:
                    print("Invalid option. Please choose 1, 2, or 3.")

            if game_difficulty == '1':
                select_word = random.choice(word_list_easy).upper()
            elif game_difficulty == '2':
                select_word = random.choice(word_list_intermediate).upper()
            else:
                select_word = random.choice(word_list_hard).upper()

            BOARD = []
            BLANKS = '_'
            CHANCES = 7
            GAME_OVER = False
            used_letters = []

            # Initialize the game
            for letter in range(len(select_word)):
                BOARD += BLANKS

            while True:
                player_01 = input("Player 1, enter your name: \n").upper()
                if re.match(r'^[A-Z]{3,}$', player_01):
                    break
                else:
                    print("Invalid name. Please enter a name with at least 3 letters and containing only letters.")  # noqa

            while True:
                player_02 = input("Player 2, enter your name: \n").upper()
                if re.match(r'^[A-Z]{3,}$', player_02):
                    break
                else:
                    print("Invalid name. Please enter a name with at least 3 letters and containing only letters.")  # noqa

            print("Number of letters in the secret word: ", len(select_word))

            atual_player = player_01

            while not GAME_OVER:
                print('Secret Word: ' + ''.join(BOARD))
                print(f"{atual_player}'s turn.")
                print("Used Letters:", ', '.join(used_letters))

                while True:
                    letter_player = input("Type one letter: \n").upper()
                    if len(letter_player) == 1 and letter_player.isalpha():
                        if letter_player in used_letters:
                            print("You've already used this letter.")
                        else:
                            used_letters.append(letter_player)
                            break
                    else:
                        print("Invalid input. Please enter a single letter.")
                        CHANCES -= 1
                        print(body_pieces[CHANCES])

                        if CHANCES == 0:
                            GAME_OVER = True
                            print("Beware, words can also kill!")
                            print(f'{atual_player} lost the game.')
                            print(f'The secret word was: {select_word}.')
                            break

                # Checking letter and spaces
                HAS_LETTER = False
                for letter_position in range(len(select_word)):
                    letter = select_word[letter_position]
                    if letter == letter_player:
                        BOARD[letter_position] = letter
                        HAS_LETTER = True

                if not HAS_LETTER:
                    CHANCES -= 1
                    if CHANCES < 0:
                        CHANCES = 0
                    if CHANCES == 0:
                        GAME_OVER = True
                        print("Beware, words can also kill!")
                        print(f'{atual_player} lost the game.')
                        print(f'The secret word was: {select_word}.')
                        print(body_pieces[CHANCES])
                        break

                if BLANKS not in BOARD:
                    GAME_OVER = True
                    print("Congratulations, you survived!")
                    print(f'{atual_player} won the game.')
                    print(f'The secret word was: {select_word}.')
                    update_scores(atual_player, CHANCES, game_difficulty)

                if not GAME_OVER:
                    if atual_player == player_01:
                        atual_player = player_02
                    else:
                        atual_player = player_01
                    if 0 < CHANCES < len(body_pieces):
                        print(body_pieces[CHANCES])

    elif choice == '4':
        while True:
            confirm_exit = input("Are you sure you want to quit? (y/n): ")
            if confirm_exit.lower() == 'y':
                print("\nThanks for playing Hangman!")
                print(positive)
                print("\n")
                break
            elif confirm_exit.lower() == 'n':
                break
            else:
                print("Invalid input. Please enter 'y' to quit or 'n' to cancel.")  # noqa

        if confirm_exit.lower() == 'y':
            break
    else:
        input("\nPress Enter to return to the main menu.")
