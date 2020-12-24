from tkinter import *
from random import randint
from functools import partial
from constants import *

# UI
window = None
frame = None

# Game
mines = None
rows = None
columns = None

# Game in progress
board = None


# def player_win():
#     for y in range(len(w)):
#         for x in range(len(w[0])):
#             if m[y][x] == 0 and w[y][x]["text"] == "F":
#                 return False
#             if w[y][x]["text"] == " ":
#                 return False
#     return True


# def restart_game():
#     global m, w, label, mine, row, column
#     m = make_matrix(mine, row, column)
#     for y in range(len(w)):
#         for x in range(len(w[0])):
#             w[y][x]["text"] = " "
#             w[y][x]["state"] = "normal"
#     label.pack_forget()


# def create_right_button_click(b):
#     def right_button_click(e):
#         global label
#         if player_win():
#             label = Label(t, text="Ви виграли!", bg='green')
#             label.pack()
#         if b["text"] == " ":
#             b["text"] = "F"
#         elif b["text"] == "F":
#             b["text"] = " "
#     return right_button_click


# def make_matrix(z, width, height):
#     global m, w, mine
#     mi = mine
#     h = []
#     for i in range(height):
#         d = []
#         for j in range(width):
#             d = d+[0]
#         h = h+[d]
#     while mi != 0:
#         y = randint(0, len(h)-1)
#         x = randint(0, len(h[0])-1)
#         h[y][x] = 1
#         mi -= 1
#     return h


# def open_cell(y, x):
#     if y >= len(w) or y < 0 or x >= len(w[0]) or x < 0:
#         return
#     else:
#         if w[y][x]['text'] == ' ':
#             w[y][x]['text'] = count(y, x)
#             w[y][x]["state"] = "disabled"
#             if count(y, x) == 0:
#                 open_cell(y, x+1)
#                 open_cell(y, x-1)
#                 open_cell(y+1, x)
#                 open_cell(y-1, x)
#                 open_cell(y+1, x+1)
#                 open_cell(y-1, x-1)
#                 open_cell(y-1, x+1)
#                 open_cell(y+1, x-1)


# def get(y, x):
#     if y >= len(m) or x >= len(m[0]) or y < 0 or x < 0:
#         return 0
#     else:
#         return m[y][x]


# def count(y, x):
#     return get(y, x+1) +\
#         get(y, x-1) +\
#         get(y+1, x) +\
#         get(y-1, x) +\
#         get(y+1, x+1) +\
#         get(y-1, x-1) +\
#         get(y-1, x+1) +\
#         get(y+1, x-1)


# def create_sapor(y, x, b):
#     def sapor():
#         global label
#         if player_win():
#             label = Label(t, text="Ви виграли!", bg='green')
#             label.pack()
#         else:
#             if m[y][x] == 1:
#                 b['text'] = '*'
#                 label = Label(t, text="Ви програли!!", bg='red')
#                 label.pack()
#                 for y1 in range(len(m)):
#                     for x1 in range(len(m[0])):
#                         w[y1][x1]["state"] = "disabled"
#                         if m[y1][x1] == 1:
#                             w[y1][x1]["text"] = "*"
#             else:
#                 open_cell(y, x)
#     return sapor


def on_tile_click(x, y):
    global board
    tile = board[y][x]
    print('tile: {} {}'.format(x, y))


def start_game(difficulty):
    global frame, board, mines, rows, columns

    mines, rows, columns = difficulty.value

    frame.destroy()
    frame = Frame()
    frame.pack()

    Button(frame, text='Back', command=select_difficulty).pack()
    frm_board = Frame(frame)
    frm_board.pack()

    board = [[0 for j in range(columns)] for i in range(rows)]

    for y in range(rows):
        for x in range(columns):
            tile = {
                'x': x,
                'y': y,
                'opened': False,
                'is_mine': None,
                'mines_around': None,
                'btn': Button(frm_board, command=partial(on_tile_click, x, y))
            }
            tile['btn'].grid(column=x, row=y)
            board[y][x] = tile


def select_difficulty():
    global frame

    if frame is not None:
        frame.destroy()
    frame = Frame()
    frame.pack()

    Label(frame, text="Оберіть складність:").pack()

    Button(frame, text="EASY",
           command=lambda: start_game(DifficultyLevel.EASY)).pack()
    Button(frame, text="MEDIUM",
           command=lambda: start_game(DifficultyLevel.MEDIUM)).pack()
    Button(frame, text="HARD",
           command=lambda: start_game(DifficultyLevel.HARD)).pack()


if __name__ == '__main__':
    window = Tk()
    window.title('Minesweeper')
    window.geometry('500x300')

    select_difficulty()

    window.mainloop()
