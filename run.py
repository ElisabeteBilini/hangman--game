'''Template exchange, originally written by the link:
https://elisabetebilini.github.io/hangman-game/
'''
import random
import re
from art import body_pieces, hang
from words import word_list_easy, word_list_intermediate, word_list_hard

print(hang)

select_word = ""
difficulty = ""

# difficulty level
while difficulty not in ('1', '2', '3'):
    difficulty = input(
      "Choose the difficulty level: \n1 - Easy\n2 - Intermediate\n3 - Hard\n")

if difficulty == '1':
    select_word = random.choice(word_list_easy).upper()
elif difficulty == '2':
    select_word = random.choice(word_list_intermediate).upper()
else:
    select_word = random.choice(word_list_hard).upper()

BOARD = []
BLANKS = '_'
CHANCES = 7
GAME_OVER = False

for letter in range(len(select_word)):
    BOARD += BLANKS

choice = input("Choose the game mode: 1 Single Player or 2 Two Players. \n")

print("Number of letters in the secret word: ", len(select_word))

if choice == '1':
    while True:
        player = input("Player, enter your name: \n").upper()
        if re.match(r'^[A-Z]{3,}$', player):
            break
        else:
            print("Invalid name. Please enter a name with at least 3 letters and containing only letters.")

# identifying player
    while not GAME_OVER:
        print('Secret Word: ' + ''.join(BOARD))

        while True:
            letter_player = input("Type one letter: \n").upper()
            if len(letter_player) == 1 and letter_player.isalpha():
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
            print(body_pieces[CHANCES])

            if CHANCES == 0:
                GAME_OVER = True
                print("Beware, words can also kill!")
                print(f'{player}, you lost the game.')
                print(f'The secret word was: {select_word}.')
                break
            
        if BLANKS not in BOARD:
            GAME_OVER = True
            print("Congratulation, you survive!")
else:
    while True:
        player_01 = input("Player 1, enter your name: \n").upper()
        if re.match(r'^[A-Z]{3,}$', player_01):
            break
        else:
            print("Invalid name. Please enter a name with at least 3 letters and containing only letters.")
    while True:
        player_02 = input("Player 2, enter your name: \n").upper()
        if re.match(r'^[A-Z]{3,}$', player_02):
            break
        else:
            print("Invalid name. Please enter a name with at least 3 letters and containing only letters.")

    atual_player = player_01

# identifying player
    while not GAME_OVER:
        print('Secret Word: ' + ''.join(BOARD))
        print(f"{atual_player}'s turn.")

# request letter to player
        letter_player = input("Type one letter: \n").upper()

# Checking Letter and spaces
        HAS_LETTER = False
        for letter_position in range(len(select_word)):
            letter = select_word[letter_position]
            if letter == letter_player:
                BOARD[letter_position] = letter
                HAS_LETTER = True

        if not HAS_LETTER:
            CHANCES -= 1
            print(body_pieces[CHANCES])
            
            if CHANCES == 0:
                GAME_OVER = True
                print("Beware, words can also kill!")
                print(f'{atual_player} lost the game.')
                print(f'The secret word was: {select_word}.')
                break

        if BLANKS not in BOARD:
            GAME_OVER = True
            print("Congratulation, you survive!")
            print(f'{atual_player} won the game.')
        if atual_player == player_01:
            atual_player = player_02
        else:
            atual_player = player_01
        print(body_pieces[CHANCES])
