# -------------simple  Tic Toc Toe Game--------------------

from tkinter import *
import random


#  ---------------functions--------------------------


def next_move(row, column):
    global player

    if check_winner():

        label_player.config(text=player + ' win')

    elif (buttons[row][column])['text'] == "" and fill() == False:
        (buttons[row][column])['text'] = player

        if check_winner() == False and fill() == False:

            if player == players[0]:
                player = players[1]
            else:
                player = players[0]
            label_player['text'] = 'Player:' + player + " "

        elif check_winner() == False and fill() == True:
            label_player['text'] = "Tie"


def fill():
    for row in range(3):
        for column in range(3):

            if buttons[row][column]['text'] == "":
                return False

    else:
        return True


def check_winner():
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            label_player.config(text=player + ' win')
            return True

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            label_player.config(text=player + ' win')
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        label_player.config(text=player + ' win')
        return True

    if buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != "":
        label_player.config(text=player + ' win')
        return True

    return False


def play_again():
    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, text="", width=6, height=2, font=('consolas', 25),
                                          command=lambda row=row, column=column: next_move(row, column))
            # lambda use pass row & column to next move function

            buttons[row][column].grid(row=row, column=column)


#  ----------------------window--------------------------

window = Tk()

window.geometry('450x450')
window.config(background='black')
window.title("Tic Toc Toe")

players = ['O', 'X']
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label_player = Label(window, text='Player:' + player + " ", font=('consolas', 25))
label_player.pack(side='bottom')

reset_game = Button(window, text="play again", font=('consolas', 15), command=play_again)
reset_game.pack(side='bottom')

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", width=6, height=2, font=('consolas', 25),
                                      command=lambda row=row, column=column: next_move(row, column))
        # lambda use pass row & column to next move function

        buttons[row][column].grid(row=row, column=column)

window.mainloop()
