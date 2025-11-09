from glob import glob
from tkinter import *
import random 


def next_turn(row, col):
    global player
    if games_btns[row][col]['text'] == "" and check_winner() == False:
        if player == players[0]:
            #put player 1 sympol
            games_btns[row][col]['text'] = player
            games_btns[row][col]['fg'] = "#3498db"

            if check_winner() == False:
                #switch player
                player = players[1]
                label.config(text=(players[1] + " turn"))

            elif check_winner() == True:
                label.config(text=(players[0] + " wins "))

            else:
                label.config(text=(" Tie, No Winner! "))

        elif player == players[1]:
            #put player 2 sympol
            games_btns[row][col]['text'] = player
            games_btns[row][col]['fg'] = "#e74c3c"

            if check_winner() == False:
                #switch player
                player = players[0]
                label.config(text=(players[0] + " turn"))

            elif check_winner() == True:
                label.config(text=(players[1] + " wins "))

            else:
                label.config(text=(" Tie, No Winner! "))

def check_winner():
    #check all 3 horizental conditions
    for row in range(3):
        if games_btns[row][0]['text'] == games_btns[row][1]['text'] == games_btns[row][2]['text'] != "":
             games_btns[row][0].config(bg="#58D68D")
             games_btns[row][1].config(bg="#58D68D")
             games_btns[row][2].config(bg="#58D68D")
             return True

    #check all 3 vertical conditions
    for col in range(3):
        if games_btns[0][col]['text'] == games_btns[1][col]['text'] == games_btns[2][col]['text'] != "":
            games_btns[0][col].config(bg="#58D68D")
            games_btns[1][col].config(bg="#58D68D")
            games_btns[2][col].config(bg="#58D68D")
            return True  

    #check diagonals conditions
    if games_btns[0][0]['text'] == games_btns[1][1]['text'] == games_btns[2][2]['text'] != "":
        games_btns[0][0].config(bg="#58D68D")
        games_btns[1][1].config(bg="#58D68D")
        games_btns[2][2].config(bg="#58D68D")
        return True
    elif games_btns[0][2]['text'] == games_btns[1][1]['text'] == games_btns[2][0]['text'] != "":
        games_btns[0][2].config(bg="#58D68D")
        games_btns[1][1].config(bg="#58D68D")
        games_btns[2][0].config(bg="#58D68D")
        return True

    #if there are no empty spaces left
    if check_empty_spaces() == False:
        for row in range(3):
            for col in range(3):
                games_btns[row][col].config(bg = '#F9E79F')
        
        return ' Tie'

    else:
        return False


def check_empty_spaces():
    spaces = 9

    for row in range(3):
        for col in range(3):
            if games_btns[row][col]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def start_new_game():
    global player
    player = random.choice(players)

    label.config(text=(player + " turn"))

    for row in range(3):
        for col in range(3):
            games_btns[row][col].config(text="", bg="#F0F0F0")



window = Tk()
window.title("Tic-Tac-Toe")

players = ["x", "o"]
player = random.choice(players)

games_btns = [
     [0,0,0],
     [0,0,0],
     [0,0,0]
]

label = Label(text=(player + " turn"), font=('consloas', 40))
label.pack(side="top")

restart_btn = Button(text="restart", font=('consolas', 20), command=start_new_game)
restart_btn.pack(side="top")

btns_frame = Frame(window)
btns_frame.pack()

for row in range(3):
    for col in range(3):
        games_btns[row][col] = Button(btns_frame, text="", font=('consolas', 50), width=4, height=1,
                            command=lambda row=row, col=col: next_turn(row,col))
        games_btns[row][col].grid(row=row, column=col)



window.mainloop()