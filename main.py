# -------------simple  Tic Toc Toe Game--------------------

from tkinter import *
import random


#  ---------------functions--------------------------

def next_move(row, column):
    global player


    if (buttons[row][column])['text'] == "" and check_winner()==False :
        (buttons[row][column])['text'] = player

        if check_winner() :
            label_player.config(text=player + ' win')
            counter_win()

        elif fill() == False:

            if player == players[0]:
                player = players[1]
            else:
                player = players[0]
            label_player['text'] = 'Player:' + player + " "

        elif fill():
            label_player['text'] = "Tie"
            count_tie = counter_tie.get()
            count_tie += 1
            counter_tie.set(count_tie)
            label_tie['text'] = 'tie:' + str(count_tie) + " "


def fill():
    for row in range(3):
        for column in range(3):

            if buttons[row][column]['text'] == "":
                return False

    else:
        return True

def counter_win():
    if player == players[0]:
        counter_o = counter_player_o.get()
        counter_o += 1
        counter_player_o.set(counter_o)
        label_player_o['text'] = 'o:' + str(counter_o) + " "

    else:
        counter_x = counter_player_x.get()
        counter_x += 1
        counter_player_x.set(counter_x)
        label_player_x['text'] = 'X:' + str(counter_x) + " "


def check_winner():
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            label_player.config(text=player + ' win')
            for row in range(3):
                buttons[row][column].configure(bg = "red")
            return True

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            label_player.config(text=player + ' win')
            for column in range(3):
                buttons[row][column].configure(bg = "red")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        label_player.config(text=player + ' win')
        for item in range(3):
            buttons[item][item].configure(bg="red")
        return True

    if buttons[2][0]['text'] == buttons[1][1]['text'] == buttons[0][2]['text'] != "":
        label_player.config(text=player + ' win')
        buttons[2][0].configure(bg="red")
        buttons[1][1].configure(bg="red")
        buttons[0][2].configure(bg="red")
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
window.config(background='#221122', pady=10)
window.title("Tic Toc Toe")

players = ['O', 'X']
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

counter_player_o = IntVar(value=0)
counter_player_x = IntVar(value=0)
counter_tie = IntVar(value=0)


# ------ Frame Turn ---------------------

frame_turn = Frame(window, padx=3)
frame_turn.pack(side='bottom')

label_player = Label(frame_turn, text='Player:' + player + " ", font=('consolas', 20))
label_player.grid(row=0,column=0)

reset_game = Button(frame_turn, text="play again", font=('consolas', 14),
                    command=play_again, border=3, highlightcolor="#ff8899", bg="#888888")
reset_game.grid(row=0,column=1, pady = 5)

# ----------- Frame Score _______________

frame_score = Frame(window )
frame_score.pack(side='bottom', pady=5)

label_player_x = Label(frame_score, text='X:0 ', font=('consolas', 20))
label_player_x.grid(row=0,column=0)

label_player_o = Label(frame_score, text='O:0 ', font=('consolas', 20))
label_player_o.grid(row=0,column=1)

label_tie = Label(frame_score, text='Tie:0 ', font=('consolas', 20))
label_tie.grid(row=0,column=2)


# ------------------ Frame Bottons ---------------------------

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", width=6, height=2, font=('consolas', 25),
                                      bg="#888888",
                                      command=lambda row=row, column=column: next_move(row, column))
        # lambda use pass row & column to next move function

        buttons[row][column].grid(row=row, column=column)

window.mainloop()
