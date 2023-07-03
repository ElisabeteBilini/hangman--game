'''Template exchange, originally written by the link:
https://elisabetebilini.github.io/hangman-game/
'''
import random
from art import body_pieces, hang
from words import word_list

print(hang)

select_word = random.choice(word_list).upper()
'''choosing random word
print(select_word)'''

BOARD = []
BLANKS = '_'
CHANCES = 6
GAME_OVER = False

for letter in range(len(select_word)):
    BOARD += BLANKS

choice = input("Choose the game mode: 1 Single Player or 2 Two Players. \n")

print("Number of letters in the secret word: ", len(select_word))

if choice == '1':
    player = input("Player, enter your name: \n").upper()

# identifying player
    while not GAME_OVER:
        print('Secret Word: ' + ''.join(BOARD))

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
            if CHANCES == 0:
                GAME_OVER = True
                print("Beware, words can also kill!")
                print(f'{player}, you lost the game.')
                print(f'The secret word was: {select_word}.')
                break
            print(body_pieces[CHANCES])

        if BLANKS not in BOARD:
            GAME_OVER = True
            print("Congratulation, you survive!")
else:
    player_01 = input("Player 1, enter your name: \n").upper()
    player_02 = input("Player 2, enter your name: \n").upper()

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
