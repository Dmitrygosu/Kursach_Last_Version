from threading import Thread

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import *
import time
import random

winner = [None]

tk = Tk()  # Создаём окно
tk.title('Фризские шашки')  # Заголовок окна
board = Canvas(tk, width=1400, height=1000, bg='#FFFFFF')
tk.resizable(width=False, height=False)
board.pack()
app_running = True
tk.update()


priorMoves = []
hod_igroka = True
vozmozhnost_belih_shodit = False
vozmozhnost_chernih_shodit = False
white_count = 20
black_count = 20
vozm_b_zabrat_vverh = False
vozm_b_zabrat_vniz = False
vozm_b_zabrat_vlevo = False
vozm_b_zabrat_vpravo = False
vozm_b_zabrat_vpravo_vverh = False
vozm_b_zabrat_vlevo_vverh = False
vozm_b_zabrat_vpravo_vniz = False
vozm_b_zabrat_vlevo_vniz = False
vozm_b_zabrat = False
vozm_b_d_zabrat_vverh = False
vozm_b_d_zabrat_vniz = False
vozm_b_d_zabrat_vlevo = False
vozm_b_d_zabrat_vpravo = False
vozm_b_d_zabrat = False
vozm_b_d_zabrat_vpravo_vverh = False
vozm_b_d_zabrat_vlevo_vverh = False
vozm_b_d_zabrat_vlevo_vniz = False
vozm_b_d_zabrat_vpravo_vniz = False
vozm_ch_zabrat_vniz = False
vozm_ch_zabrat_vlevo = False
vozm_ch_zabrat_vpravo = False
vozm_ch_zabrat_vverh = False
vozm_ch_zabrat_vpravo_vverh = False
vozm_ch_zabrat_vlevo_vverh = False
vozm_ch_zabrat_vpravo_vniz = False
vozm_ch_zabrat_vlevo_vniz = False
vozm_ch_zabrat = False
vozm_ch_d_zabrat_vverh = False
vozm_ch_d_zabrat_vniz = False
vozm_ch_d_zabrat_vlevo = False
vozm_ch_d_zabrat_vpravo = False
vozm_ch_d_zabrat_vpravo_vverh = False
vozm_ch_d_zabrat_vlevo_vverh = False
vozm_ch_d_zabrat_vlevo_vniz = False
vozm_ch_d_zabrat_vpravo_vniz = False
vozm_ch_d_zabrat = False
AI = True
WIDTH = 800
ROWS = 8
def izobrazheniya_figur():  # загружаем изображения фигур
    global figuri
    i1 = PhotoImage(file="src\\white_checkers.png")
    i2 = PhotoImage(file="src\\black_checkers.png")
    i3 = PhotoImage(file="src\\white_checkers_king.png")
    i4 = PhotoImage(file="src\\black_checkers_king.png")
    figuri = [0, i1, i2, i3, i4]

def button_press1():
    global AI
    if AI == False:
        AI = True
    else:
        AI = False
    vivod(-1,-1)

def novaya_igra():  # начинаем новую игру
    global pole

    pole =  [[0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
             [2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
             [0, 2, 0, 2, 0, 2, 0, 2, 0, 2],
             [2, 0, 2, 0, 2, 0, 2, 0, 2, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
             [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]]

def Start_new():
    global white_count
    global black_count
    global hod_igroka
    if askyesno("Игра закончена","Хотите начать новую?"):
        novaya_igra()
        vivod(-1,-1)
        hod_igroka = True
        white_count = 20
        black_count = 20

def vivod(x_poz_1, y_poz_1):  # рисуем игровое поле
    global figuri
    global pole
    k = 100
    x = 0
    board.delete('all')
    board.create_rectangle(1600, 0, 1000, 1100, fill="#505050")
    board.create_text(1150, 125, fill="white", font="Open 18 bold", text=f"Количество белых : {white_count}")
    board.create_text(1150, 865, fill="white", font="Open 18 bold",
                      text=f"Количество чёрных : {black_count}")

    #
    # if vozmozhnost_belih_shodit:
    #     board.create_text(1105, 500, fill="white", font="Open 16 bold", text="Ход белых")
    # if vozmozhnost_chernih_shodit is False:
    #     board.create_text(1150, 600, fill="white", font="Open 16 bold", text="Ход черных")
    b1 = Button(tk, text="Вкл/Выкл ИИ", command=button_press1)
    b1.place(x=1025, y=400, width=120, height=50)
    while x < 10 * k:  # рисуем доску
        y = k
        while y < 10 * k:
            board.create_rectangle(x, y, x + k, y + k, fill="Black")
            y += 2 *k
        x += 2 * k
    x = k
    while x < 10 * k:  # рисуем доску
        y = 0
        while y < 10 * k:
            board.create_rectangle(x, y, x + k, y + k, fill="Black")
            y += 2 * k
        x += 2 * k

    for y in range(10):  # рисуем стоячие пешки
        for x in range(10):
            z = pole[y][x]
            if z:
                if (x_poz_1, y_poz_1) != (x, y):  # стоячие пешки?
                    board.create_image(x * k, y * k, anchor=NW, image=figuri[z])


def vozmozhnost_belih_hodit(x, y): #метод, проверяющий белые шашки на доступность хода(что им ничего не преграждает путь)
    global vozmozhnost_belih_shodit
    global prev_b_coord_x
    global prev_b_coord_y
    if pole[x][y] == 1: # для белой не дамки
        if (pole[x - 1][y - 1] == 0 and x > 0 and y > 0) or (y < 9 and x > 0 and pole[x - 1][y + 1] == 0):
            vozmozhnost_belih_shodit = True
        else:
            vozmozhnost_belih_shodit = False
        prev_b_coord_x = x
        prev_b_coord_y = y
    elif pole[x][y] == 3: # для белой дамки
        if (pole[x - 1][y - 1] == 0 and x > 0 and y > 0) or (y < 9 and x > 0 and pole[x - 1][y + 1] == 0) or (pole[x + 1][y - 1] == 0 and x < 9 and y > 0) or (x < 9 and y < 9 and pole[x + 1][y + 1] == 0):
            vozmozhnost_belih_shodit = True
        else:
            vozmozhnost_belih_shodit = False
        prev_b_coord_x = x
        prev_b_coord_y = y


def vozmozhnost_chernih_hodit(x, y): #метод, проверяющий черные шашки на доступность хода(что им ничего не преграждает путь)
    global vozmozhnost_chernih_shodit
    global prev_ch_coord_x
    global prev_ch_coord_y

    if pole[x][y] == 2: # для черной не дамки
        if (pole[x + 1][y - 1] == 0 and x < 9 and y > 0) or (y < 9 and x < 9 and pole[x + 1][y + 1] == 0):
            vozmozhnost_chernih_shodit = True
        else:
            vozmozhnost_chernih_shodit = False
        prev_ch_coord_x = x
        prev_ch_coord_y = y
    elif pole[x][y] == 4: # для черной дамки
        if (pole[x - 1][y - 1] == 0 and x > 0 and y > 0) or (y < 9 and x > 0 and pole[x - 1][y + 1] == 0) or (pole[x + 1][y - 1] == 0 and x < 9 and y > 0) or (x < 9 and y < 9 and pole[x + 1][y + 1] == 0):
            vozmozhnost_chernih_shodit = True
        else:
            vozmozhnost_chernih_shodit = False
        prev_ch_coord_x = x
        prev_ch_coord_y = y

def belie_proverka():
    global vozm_b_zabrat_vverh
    global vozm_b_zabrat_vniz
    global vozm_b_zabrat_vlevo
    global vozm_b_zabrat_vpravo
    global vozm_b_zabrat_vpravo_vverh
    global vozm_b_zabrat_vlevo_vverh
    global vozm_b_zabrat_vlevo_vniz
    global vozm_b_zabrat_vpravo_vniz
    global vozm_b_zabrat
    global vozm_b_d_zabrat_vverh
    global vozm_b_d_zabrat_vniz
    global vozm_b_d_zabrat_vlevo
    global vozm_b_d_zabrat_vpravo
    global vozm_b_d_zabrat
    global vozm_b_d_zabrat_vpravo_vverh
    global vozm_b_d_zabrat_vlevo_vverh
    global vozm_b_d_zabrat_vlevo_vniz
    global vozm_b_d_zabrat_vpravo_vniz

    for i in range(10):      # ищем на поле возможность случая забирания
        for j in range(10):
            if (pole[i][j] == 1 and i > 3) and (pole[i - 2][j] == 2 or pole[i - 2][j] == 4) and pole[i - 4][j] == 0: # для белой шашки вверх
                vozm_b_zabrat_vverh = True
                vozm_b_zabrat = True

            if (pole[i][j] == 1 and i < 6) and (pole[i + 2][j] == 2 or pole[i+2][j] == 4) and pole[i+4][j] == 0:
                vozm_b_zabrat_vniz = True
                vozm_b_zabrat = True

            if (pole[i][j] == 1 and j > 3) and (pole[i][j - 2] == 2 or pole[i][j - 2] == 4) and pole[i][j - 4] == 0: # для белой шашки влево
                vozm_b_zabrat_vlevo = True
                vozm_b_zabrat = True

            if (pole[i][j] == 1 and j < 6) and (pole[i][j + 2] == 2 or pole[i][j+2] == 4) and pole[i][j + 4] == 0: # для белой шашки вправо
                vozm_b_zabrat = True
                vozm_b_zabrat_vpravo = True

            if (pole[i][j] == 1 and i > 1 and j < 8) and (pole[i - 1][j + 1] == 2 or pole[i - 1][j + 1] == 4) and pole[i - 2][j + 2] == 0:
                vozm_b_zabrat = True
                vozm_b_zabrat_vpravo_vverh = True

            if (pole[i][j] == 1 and i > 1 and j > 1) and (pole[i - 1][j - 1] == 2 or pole[i - 1][j - 1] == 4) and pole[i - 2][j - 2] == 0:
                vozm_b_zabrat = True
                vozm_b_zabrat_vlevo_vverh = True

            if (pole[i][j] == 1 and i < 8 and j < 8) and (pole[i + 1][j + 1] == 2 or pole[i + 1][j + 1] == 4) and pole[i + 2][j + 2] == 0:
                vozm_b_zabrat = True
                vozm_b_zabrat_vpravo_vniz = True

            if (pole[i][j] == 1 and i < 8 and j > 1) and (pole[i + 1][j - 1] == 2 or pole[i + 1][j - 1] == 4) and pole[i + 2][j - 2] == 0:
                vozm_b_zabrat = True
                vozm_b_zabrat_vlevo_vniz = True

            if i > 1 and pole[i][j] == 3:  # для белой дамки вверх
                for k in range(10):
                    zero_count = 0
                    ch_count = 0
                    count = 0
                    if pole[k][j] == 0 and ((k < 8 and pole[k + 2][j] == 2) or (k < 8 and pole[k + 2][j] == 4)) and (k < 6 and pole[k + 4][j] == 0 or k < 6 and pole[k + 4][j] == 3):
                        while pole[k][j] != 3:
                            if j < 9 and pole[i][j + 2] == 3:
                                vozm_b_d_zabrat_vverh = True
                                vozm_b_d_zabrat = True
                                break
                            ch_count += 1
                            if k < 8:
                                k += 2
                            else:
                                break
                            if pole[k][j] == 0:
                                zero_count += 1
                            if pole[k][j] == 2 or pole[k][j] == 4 and j > 0:
                                count += 1
                            if count == 2:
                                break
                            if zero_count == ch_count - 2 and pole[k][j] == 3 and k > 0:
                                vozm_b_d_zabrat_vverh = True
                                vozm_b_d_zabrat = True
                            else:
                                vozm_b_d_zabrat_vverh = False
                        break

            if i < 6 and pole[i][j] == 3:  # для белой дамки вниз
                for k in range(10):
                    zero_count = 0
                    ch_count = 0
                    if pole[k][j] == 0 and ((k > 2 and pole[k - 2][j] == 2) or (k > 1 and pole[k - 2][j] == 4)):
                        while pole[k][j] != 3:
                            ch_count += 1
                            k -= 2
                            if pole[k][j] == 0:
                                zero_count += 1
                            if zero_count == ch_count - 2 and pole[k][j] == 3:
                                vozm_b_d_zabrat_vniz = True
                                vozm_b_d_zabrat = True
                            else:
                                vozm_b_d_zabrat_vniz = True
                        break

            if j > 3 and pole[i][j] == 3:  # для белой дамки влево
                for k in range(10):
                    zero_count = 0
                    ch_count = 0
                    count = 0
                    if pole[i][k] == 0 and ((k < 8 and pole[i][k + 2] == 2) or (k < 8 and pole[i][k + 2] == 4)) and (k < 6 and pole[i][k + 4] == 0 or k < 6 and pole[i][k + 4] == 3):
                        while pole[i][k] != 3:
                            if k < 8 and pole[i + 2][j] == 3:
                                vozm_b_d_zabrat_vlevo = True
                                vozm_b_d_zabrat = True
                                break
                            ch_count += 1
                            if k < 8:
                                k += 2
                            else:
                                break
                            if pole[i][k] == 0:
                                zero_count += 1
                            if pole[i][k] == 2 or pole[i][k] == 4:
                                count += 1
                            if count == 2:
                                break
                            if zero_count == ch_count - 2 and pole[i][k] == 3:
                                vozm_b_d_zabrat_vlevo = True
                                vozm_b_d_zabrat = True
                            else:
                                vozm_b_d_zabrat_vlevo = False

            if j < 6 and pole[i][j] == 3:  # для белой дамки вправо
                for k in range(10):
                    zero_count = 0
                    ch_count = 0
                    if pole[i][k] == 0 and ((k > 2 and pole[i][k - 2] == 2) or (k > 2 and pole[i][k - 2] == 4)):
                        while pole[i][k] != 3:
                            ch_count += 1
                            k -= 2
                            if pole[i][k] == 0:
                                zero_count += 1
                            if zero_count == ch_count - 2 and pole[i][k] == 3:
                                vozm_b_d_zabrat_vpravo = True
                                vozm_b_d_zabrat = True
                            else:
                                vozm_b_zabrat_vpravo = False
                        break
            if j > 1 and i < 8 and pole[j][i] == 3:
                count = 0
                ch_count = 0
                if (pole[j - 1][i + 1] == 2 or pole[j - 1][i + 1] == 4) and pole[j - 2][i + 2] == 0:
                    vozm_b_d_zabrat = True
                    vozm_b_d_zabrat_vpravo_vverh = True
                else:
                    while j > 0 and i < 9:
                        j -= 1
                        i += 1
                        if pole[j][i] != 0:
                            ch_count += 1
                        if pole[j][i] == 2 or pole[j][i] == 4:
                            count += 1
                        if ch_count == 2:
                            break
                        if (pole[j][i] == 2 or pole[j][i] == 4) and pole[j - 1][i + 1] == 0 and count == 1:
                            vozm_b_d_zabrat = True
                            vozm_b_d_zabrat_vpravo_vverh = True
                            break
                        else:
                            vozm_b_d_zabrat_vpravo_vverh = False
            if j > 1 and i > 1 and pole[j][i] == 3:
                ch_count = 0
                count = 0
                if (pole[j - 1][i - 1] == 2 or pole[j - 1][i - 1] == 4) and pole[j - 2][i - 2] == 0:
                    vozm_b_d_zabrat = True
                    vozm_b_d_zabrat_vlevo_vverh = True
                else:
                    while j > 0 and i > 0:
                        j -= 1
                        i -= 1
                        if pole[j][i] != 0:
                            ch_count += 1
                        if pole[j][i] == 2 or pole[j][i] == 4:
                            count += 1
                        if ch_count == 2:
                            break
                        if (pole[j][i] == 2 or pole[j][i] == 4) and pole[j - 1][i - 1] == 0 and count == 1:
                            vozm_b_d_zabrat = True
                            vozm_b_d_zabrat_vlevo_vverh = True
                            break
                        else:
                            vozm_b_d_zabrat_vlevo_vverh = False
            if j < 8 and i > 1 and pole[j][i] == 3:
                ch_count = 0
                count = 0
                if (pole[j + 1][i - 1] == 2 or pole[j + 1][i - 1] == 4) and pole[j + 2][i - 2] == 0:
                    vozm_b_d_zabrat = True
                    vozm_b_d_zabrat_vlevo_vniz = True
                else:
                    while j < 9 and i > 0:
                        j += 1
                        i -= 1
                        if pole[j][i] != 0:
                            ch_count += 1
                        if pole[j][i] == 2 or pole[j][i] == 4:
                            count += 1
                        if ch_count == 2:
                            break
                        if (pole[j][i] == 2 or pole[j][i] == 4) and pole[j + 1][i - 1] == 0 and count == 1:
                            vozm_b_d_zabrat = True
                            vozm_b_d_zabrat_vlevo_vniz = True
                            break
                        else:
                            vozm_b_d_zabrat_vlevo_vniz = False

            if j < 8 and i < 8 and pole[j][i] == 3:
                ch_count = 0
                count = 0
                if (pole[j + 1][i + 1] == 2 or pole[j + 1][i + 1] == 4) and pole[j + 2][i + 2] == 0:
                    vozm_b_d_zabrat = True
                    vozm_b_d_zabrat_vpravo_vniz = True
                else:
                    while j < 9 and i < 9:
                        j += 1
                        i += 1
                        if pole[j][i] != 0:
                            ch_count += 1
                        if pole[j][i] == 2 or pole[j][i] == 4:
                            count += 1
                        if ch_count == 2:
                            break
                        if (pole[j][i] == 2 or pole[j][i] == 4) and pole[j + 1][i + 1] == 0 and count == 1:
                            vozm_b_d_zabrat = True
                            vozm_b_d_zabrat_vpravo_vniz = True
                            break
                        else:
                            vozm_b_d_zabrat_vpravo_vniz = False
def chernie_proverka(): # аналогично с тем что выше
    global vozm_ch_zabrat_vverh
    global vozm_ch_zabrat_vniz
    global vozm_ch_zabrat_vlevo
    global vozm_ch_zabrat_vpravo
    global vozm_ch_zabrat_vpravo_vverh
    global vozm_ch_zabrat_vlevo_vverh
    global vozm_ch_zabrat_vlevo_vniz
    global vozm_ch_zabrat_vpravo_vniz
    global vozm_ch_zabrat
    global vozm_ch_d_zabrat_vverh
    global vozm_ch_d_zabrat_vniz
    global vozm_ch_d_zabrat_vlevo
    global vozm_ch_d_zabrat_vpravo
    global vozm_ch_d_zabrat
    global vozm_ch_d_zabrat_vpravo_vverh
    global vozm_ch_d_zabrat_vlevo_vverh
    global vozm_ch_d_zabrat_vlevo_vniz
    global vozm_ch_d_zabrat_vpravo_vniz

    for i in range(10):
        for j in range(10):
            if (pole[i][j] == 2 and i > 3) and (pole[i - 2][j] == 1 or pole[i - 2][j] == 3) and pole[i - 4][
                j] == 0:  # для белой шашки вверх
                vozm_ch_zabrat_vverh = True
                vozm_ch_zabrat = True

            if (pole[i][j] == 2 and i < 6) and (pole[i + 2][j] == 1 or pole[i + 2][j] == 3) and pole[i + 4][j] == 0:
                vozm_ch_zabrat_vniz = True
                vozm_ch_zabrat = True

            if (pole[i][j] == 2 and j > 3) and (pole[i][j - 2] == 1 or pole[i][j - 2] == 3) and pole[i][
                j - 4] == 0:  # для белой шашки влево
                vozm_ch_zabrat_vlevo = True
                vozm_ch_zabrat = True

            if (pole[i][j] == 2 and j < 6) and (pole[i][j + 2] == 1 or pole[i][j + 2] == 3) and pole[i][
                j + 4] == 0:  # для белой шашки вправо
                vozm_ch_zabrat = True
                vozm_ch_zabrat_vpravo = True

            if (pole[i][j] == 2 and i > 1 and j < 8) and (pole[i - 1][j + 1] == 1 or pole[i - 1][j + 1] == 3) and \
                    pole[i - 2][j + 2] == 0:
                vozm_ch_zabrat = True
                vozm_ch_zabrat_vpravo_vverh = True

            if (pole[i][j] == 2 and i > 1 and j > 1) and (pole[i - 1][j - 1] == 1 or pole[i - 1][j - 1] == 3) and \
                    pole[i - 2][j - 2] == 0:
                vozm_ch_zabrat = True
                vozm_ch_zabrat_vlevo_vverh = True

            if (pole[i][j] == 2 and i < 8 and j < 8) and (pole[i + 1][j + 1] == 1 or pole[i + 1][j + 1] == 3) and \
                    pole[i + 2][j + 2] == 0:
                vozm_ch_zabrat = True
                vozm_ch_zabrat_vpravo_vniz = True

            if (pole[i][j] == 2 and i < 8 and j > 1) and (pole[i + 1][j - 1] == 1 or pole[i + 1][j - 1] == 3) and \
                    pole[i + 2][j - 2] == 0:
                vozm_ch_zabrat = True
                vozm_ch_zabrat_vlevo_vniz = True

            if i > 1 and pole[i][j] == 4:  # для черной дамки вверх
                for k in range(10):
                    zero_count = 0
                    ch_count = 0
                    count = 0
                    if pole[k][j] == 0 and ((k < 8 and pole[k + 2][j] == 1) or (k < 8 and pole[k + 2][j] == 3)) and (
                            k < 6 and pole[k + 4][j] == 0 or k < 6 and pole[k + 4][j] == 4):
                        while pole[k][j] != 4:
                            if j < 9 and pole[i][j + 2] == 4:
                                vozm_ch_d_zabrat_vverh = True
                                vozm_ch_d_zabrat = True
                                break
                            ch_count += 1
                            if k < 8:
                                k += 2
                            else:
                                break
                            if pole[k][j] == 0:
                                zero_count += 1
                            if pole[k][j] == 1 or pole[k][j] == 3 and j > 0:
                                count += 1
                            if count == 2:
                                break
                            if zero_count == ch_count - 2 and pole[k][j] == 4 and k > 0:
                                vozm_ch_d_zabrat_vverh = True
                                vozm_ch_d_zabrat = True
                            else:
                                vozm_ch_d_zabrat_vverh = False
                        break

            if i < 6 and pole[i][j] == 4:  # для белой дамки вниз
                for k in range(10):
                    zero_count = 0
                    ch_count = 0
                    if pole[k][j] == 0 and ((k > 2 and pole[k - 2][j] == 1) or (k > 1 and pole[k - 2][j] == 3)):
                        while pole[k][j] != 4:
                            ch_count += 1
                            k -= 2
                            if pole[k][j] == 0:
                                zero_count += 1
                            if zero_count == ch_count - 2 and pole[k][j] == 4:
                                vozm_ch_d_zabrat_vniz = True
                                vozm_ch_d_zabrat = True
                            else:
                                vozm_ch_d_zabrat_vniz = True
                        break

            if j > 3 and pole[i][j] == 4:  # для белой дамки влево
                for k in range(10):
                    zero_count = 0
                    ch_count = 0
                    count = 0
                    if pole[i][k] == 0 and ((k < 8 and pole[i][k + 2] == 1) or (k < 8 and pole[i][k + 2] == 3)) and (
                            k < 6 and pole[i][k + 4] == 0 or k < 6 and pole[i][k + 4] == 4):
                        while pole[i][k] != 4:
                            if k < 8 and pole[i + 2][j] == 4:
                                vozm_ch_d_zabrat_vlevo = True
                                vozm_ch_d_zabrat = True
                                break
                            ch_count += 1
                            if k < 8:
                                k += 2
                            else:
                                break
                            if pole[i][k] == 0:
                                zero_count += 1
                            if pole[i][k] == 1 or pole[i][k] == 3:
                                count += 1
                            if count == 2:
                                break
                            if zero_count == ch_count - 2 and pole[i][k] == 4:
                                vozm_ch_d_zabrat_vlevo = True
                                vozm_ch_d_zabrat = True
                            else:
                                vozm_ch_d_zabrat_vlevo = False

            if j < 6 and pole[i][j] == 4:  # для белой дамки вправо
                for k in range(10):
                    zero_count = 0
                    ch_count = 0
                    if pole[i][k] == 0 and ((k > 2 and pole[i][k - 2] == 1) or (k > 2 and pole[i][k - 2] == 3)):
                        while pole[i][k] != 4:
                            ch_count += 1
                            k -= 2
                            if pole[i][k] == 0:
                                zero_count += 1
                            if zero_count == ch_count - 2 and pole[i][k] == 4:
                                vozm_ch_d_zabrat_vpravo = True
                                vozm_ch_d_zabrat = True
                            else:
                                vozm_ch_zabrat_vpravo = False
                        break
            if j > 1 and i < 8 and pole[j][i] == 4:
                count = 0
                ch_count = 0
                if (pole[j - 1][i + 1] == 1 or pole[j - 1][i + 1] == 3) and pole[j - 2][i + 2] == 0:
                    vozm_ch_d_zabrat = True
                    vozm_ch_d_zabrat_vpravo_vverh = True
                else:
                    while j > 0 and i < 9:
                        j -= 1
                        i += 1
                        if pole[j][i] != 0:
                            ch_count += 1
                        if pole[j][i] == 1 or pole[j][i] == 3:
                            count += 1
                        if ch_count == 2:
                            break
                        if (pole[j][i] == 1 or pole[j][i] == 3) and pole[j - 1][i + 1] == 0 and count == 1:
                            vozm_ch_d_zabrat = True
                            vozm_ch_d_zabrat_vpravo_vverh = True
                            break
                        else:
                            vozm_ch_d_zabrat_vpravo_vverh = False
            if j > 1 and i > 1 and pole[j][i] == 4:
                ch_count = 0
                count = 0
                if (pole[j - 1][i - 1] == 1 or pole[j - 1][i - 1] == 3) and pole[j - 2][i - 2] == 0:
                    vozm_ch_d_zabrat = True
                    vozm_ch_d_zabrat_vlevo_vverh = True
                else:
                    while j > 0 and i > 0:
                        j -= 1
                        i -= 1
                        if pole[j][i] != 0:
                            ch_count += 1
                        if pole[j][i] == 1 or pole[j][i] == 3:
                            count += 1
                        if ch_count == 2:
                            break
                        if (pole[j][i] == 1 or pole[j][i] == 3) and pole[j - 1][i - 1] == 0 and count == 1:
                            vozm_ch_d_zabrat = True
                            vozm_ch_d_zabrat_vlevo_vverh = True
                            break
                        else:
                            vozm_ch_d_zabrat_vlevo_vverh = False
            if j < 8 and i > 1 and pole[j][i] == 4:
                ch_count = 0
                count = 0
                if (pole[j + 1][i - 1] == 1 or pole[j + 1][i - 1] == 3) and pole[j + 2][i - 2] == 0:
                    vozm_ch_d_zabrat = True
                    vozm_ch_d_zabrat_vlevo_vniz = True
                else:
                    while j < 9 and i > 0:
                        j += 1
                        i -= 1
                        if pole[j][i] != 0:
                            ch_count += 1
                        if pole[j][i] == 1 or pole[j][i] == 3:
                            count += 1
                        if ch_count == 2:
                            break
                        if (pole[j][i] == 1 or pole[j][i] == 3) and pole[j + 1][i - 1] == 0 and count == 1:
                            vozm_ch_d_zabrat = True
                            vozm_ch_d_zabrat_vlevo_vniz = True
                            break
                        else:
                            vozm_ch_d_zabrat_vlevo_vniz = False

            if j < 8 and i < 8 and pole[j][i] == 4:
                ch_count = 0
                count = 0
                if (pole[j + 1][i + 1] == 1 or pole[j + 1][i + 1] == 3) and pole[j + 2][i + 2] == 0:
                    vozm_ch_d_zabrat = True
                    vozm_ch_d_zabrat_vpravo_vniz = True
                else:
                    while j < 9 and i < 9:
                        j += 1
                        i += 1
                        if pole[j][i] != 0:
                            ch_count += 1
                        if pole[j][i] == 1 or pole[j][i] == 3:
                            count += 1
                        if ch_count == 2:
                            break
                        if (pole[j][i] == 1 or pole[j][i] == 3) and pole[j + 1][i + 1] == 0 and count == 1:
                            vozm_ch_d_zabrat = True
                            vozm_ch_d_zabrat_vpravo_vniz = True
                            break
                        else:
                            vozm_ch_d_zabrat_vpravo_vniz = False
def AI_hod():
    global hod_igroka
    global vozmozhnost_chernih_shodit
    global xx,yy,kk,jj,ii
    global vozm_ch_zabrat
    global black_count
    global white_count
    global vozm_ch_d_zabrat
    global vozm_ch_d_zabrat_vverh
    global vozm_ch_d_zabrat_vniz
    global vozm_ch_d_zabrat_vpravo
    global vozm_ch_d_zabrat_vlevo
    global vozm_ch_d_zabrat_vlevo_vniz
    global vozm_ch_d_zabrat_vlevo_vverh
    global vozm_ch_d_zabrat_vpravo_vniz
    global vozm_ch_d_zabrat_vpravo_vverh

    if AI:
        if black_count == 0:
            messagebox.showinfo(title='Победа черных', message='Победили черные.', icon='info')
            hod_igroka = None
            Start_new()

        vozm = True
        vozm_ch_zabrat = False
        vozm_ch_d_zabrat = False
        chernie_proverka()
        vozmozhnost_chernih_shodit = False
        pr_x = 0
        pr_y = 0
        xx, yy = 0, 0
        if vozm_ch_zabrat or vozm_ch_d_zabrat:
            vozm = False
        else:
            vozm = True
        while vozmozhnost_chernih_shodit != True:
            c = 0
            l = random.randint(1, str(pole).count('2'))
            for i in range(10):
                for j in range(10):
                    if pole[i][j] == 2 and c != l:
                        c += 1
                        if c == l:
                            pr_x = i
                            pr_y = j
                            vozmozhnost_chernih_hodit(i, j)

            chernie_proverka()
            if vozmozhnost_chernih_shodit and vozm_ch_zabrat == False and vozm_ch_d_zabrat == False and vozm:
                chernie_proverka()
                if pr_y < 9 and pr_x < 9 and pole[pr_x + 1][pr_y + 1] == 0 and pole[pr_x][pr_y] == 2 and vozm_ch_zabrat == False and vozm_ch_d_zabrat == False:
                    pole[pr_x][pr_y] = 0
                    if pr_x == 8:
                        pole[pr_x + 1][pr_y + 1] = 4
                    else:
                        pole[pr_x + 1][pr_y + 1] = 2
                    xx = pr_x + 1
                    yy = pr_y + 1
                elif pr_y > 0 and pr_x < 9 and pole[pr_x + 1][pr_y - 1] == 0 and pole[pr_x][pr_y] == 2 and vozm_ch_zabrat == False and vozm_ch_d_zabrat == False:

                    pole[pr_x][pr_y] = 0
                    if pr_x == 8:
                        pole[pr_x + 1][pr_y - 1] = 4
                    else:
                        pole[pr_x + 1][pr_y - 1] = 2
                    xx = pr_x + 1
                    yy = pr_y - 1
                vivod(-1, -1)
                vozmozhnost_chernih_shodit = False
                hod_igroka = True
                break
            chernie_proverka()
            if vozm_ch_d_zabrat:
                chernie_proverka()
                if vozm_ch_d_zabrat_vverh:
                    for i in range(10):
                        for j in range(10):
                            if i > 1 and pole[i][j] == 4:  # для черной дамки вверх
                                for k in range(10):
                                    zero_count = 0
                                    ch_count = 0
                                    count = 0
                                    if pole[k][j] == 0 and (
                                            (k < 8 and pole[k + 2][j] == 1) or (k < 8 and pole[k + 2][j] == 3)) and (
                                            k < 6 and pole[k + 4][j] == 0 or k < 6 and pole[k + 4][j] == 4):
                                        while pole[k][j] != 4:
                                            if j < 9 and pole[i][j + 2] == 4:
                                                vozm_ch_d_zabrat_vverh = True
                                                vozm_ch_d_zabrat = True
                                                break
                                            ch_count += 1
                                            if k < 8:
                                                k += 2
                                            else:
                                                break
                                            if pole[k][j] == 0:
                                                zero_count += 1
                                            if pole[k][j] == 1 or pole[k][j] == 3 and j > 0:
                                                count += 1
                                                kk = k
                                                jj = j
                                            if count == 2:
                                                break
                                            if zero_count == ch_count - 2 and pole[k][j] == 4 and k > 0:
                                                pole[k][j] = 0
                                                pole[kk][jj] = 0
                                                pole[kk + 2][jj] = 4
                                                white_count -= 1
                                                vivod(-1, -1)
                                                hod_igroka = True
                                                chernie_proverka()

                                        break
                chernie_proverka()
                if vozm_ch_d_zabrat_vniz:
                    for i in range(10):
                        for j in range(10):
                            if i < 6 and pole[i][j] == 4:  # для белой дамки вниз
                                for k in range(10):
                                    zero_count = 0
                                    ch_count = 0
                                    count = 0
                                    if pole[k][j] == 0 and ((k > 2 and pole[k - 2][j] == 1) or (k > 1 and pole[k - 2][j] == 3)):
                                        while pole[k][j] != 4:
                                            ch_count += 1
                                            k -= 2
                                            if pole[k][j] == 0:
                                                zero_count += 1
                                            if pole[k][j] == 1 or pole[k][j] == 3:
                                                count += 1
                                                kk = k
                                                jj = j
                                            if count == 2:
                                                break
                                            if zero_count == ch_count - 2 and pole[k][j] == 4:
                                                pole[k][j] = 0
                                                pole[kk][jj] = 0
                                                pole[kk - 2][jj] = 4
                                                white_count -= 1
                                                vivod(-1, -1)
                                                hod_igroka = True
                                                chernie_proverka()
                                        break
                chernie_proverka()
                if vozm_ch_d_zabrat_vlevo:
                    for i in range(10):
                        for j in range(10):
                            if j > 3 and pole[i][j] == 4:  # для белой дамки влево
                                for k in range(10):
                                    zero_count = 0
                                    ch_count = 0
                                    count = 0
                                    if pole[i][k] == 0 and (
                                            (k < 8 and pole[i][k + 2] == 1) or (k < 8 and pole[i][k + 2] == 3)) and (
                                            k < 6 and pole[i][k + 4] == 0 or k < 6 and pole[i][k + 4] == 4):
                                        while pole[i][k] != 4:
                                            if k < 8 and pole[i + 2][j] == 4:
                                                pole[i][k] = 0
                                                pole[ii][kk] = 0
                                                pole[ii][kk + 2] = 4
                                                white_count -= 1
                                                vivod(-1, -1)
                                                hod_igroka = True
                                                chernie_proverka()
                                                break
                                            ch_count += 1
                                            if k < 8:
                                                k += 2
                                            else:
                                                break
                                            if pole[i][k] == 0:
                                                zero_count += 1
                                            if pole[i][k] == 1 or pole[i][k] == 3:
                                                count += 1
                                                kk = k
                                                ii = i
                                            if count == 2:
                                                break
                                            if zero_count == ch_count - 2 and pole[i][k] == 4:
                                                pole[i][k] = 0
                                                pole[ii][kk] = 0
                                                pole[ii][kk + 2] = 4
                                                white_count -= 1

                                                vivod(-1, -1)
                                                hod_igroka = True
                                                chernie_proverka()
                                        break
                chernie_proverka()
                if vozm_ch_d_zabrat_vpravo:
                    for i in range(10):
                        for j in range(10):
                            if j < 6 and pole[i][j] == 4:  # для белой дамки вправо
                                for k in range(10):
                                    zero_count = 0
                                    ch_count = 0
                                    if pole[i][k] == 0 and ((k > 2 and pole[i][k - 2] == 1) or (k > 2 and pole[i][k - 2] == 3)):
                                        while pole[i][k] != 4:
                                            ch_count += 1
                                            k -= 2
                                            if pole[i][k] == 0:
                                                zero_count += 1
                                            if pole[i][k] == 1 or pole[i][k] == 3:
                                                kk = k
                                                ii = i
                                            if zero_count == ch_count - 2 and pole[i][k] == 4:
                                                pole[i][k] = 0
                                                pole[ii][kk] = 0
                                                pole[ii][kk - 2] = 4
                                                white_count -= 1
                                                vivod(-1, -1)
                                                hod_igroka = True
                                                chernie_proverka()
                                        break
                if vozm_ch_zabrat == False and vozm_ch_d_zabrat == False:
                    hod_igroka = True
                    vivod(-1, -1)
                    break
                vozm_ch_d_zabrat = False
                chernie_proverka()
            if white_count == 0:
                messagebox.showinfo(title='Победа белых', message='Победили белые.', icon='info')
                hod_igroka = None
                Start_new()
            chernie_proverka()
            if vozm_ch_zabrat == True and vozm_ch_d_zabrat == False:
                if vozm_ch_zabrat_vverh:
                    for i in range(10):
                        for j in range(10):
                            if (pole[i][j] == 2 and i > 3) and (pole[i - 2][j] == 1 or pole[i - 2][j] == 3) and pole[i - 4][
                                j] == 0:
                                pole[i][j] = 0
                                pole[i - 4][j] = 2
                                pole[i - 2][j] = 0
                                white_count -= 1
                                vivod(-1, -1)
                                chernie_proverka()
                                hod_igroka = True
                if vozm_ch_zabrat_vniz:
                    for i in range(10):
                        for j in range(10):
                            if (pole[i][j] == 2 and i < 6) and (pole[i + 2][j] == 1 or pole[i + 2][j] == 3) and pole[i + 4][j] == 0:
                                if i == 5:
                                    pole[i + 4][j] = 4
                                else:
                                    pole[i + 4][j] = 2
                                pole[i][j] = 0
                                pole[i + 2][j] = 0
                                white_count -= 1
                                vivod(-1, -1)
                                chernie_proverka()
                                hod_igroka = True
                if vozm_ch_zabrat_vlevo:
                    for i in range(10):
                        for j in range(10):
                            if (pole[i][j] == 2 and j > 3) and (pole[i][j - 2] == 1 or pole[i][j - 2] == 3) and pole[i][
                                j - 4] == 0:
                                pole[i][j] = 0
                                pole[i][j - 2] = 0
                                pole[i][j - 4] = 2
                                white_count -= 1
                                vivod(-1, -1)
                                chernie_proverka()
                                hod_igroka = True
                if vozm_ch_zabrat_vpravo:
                    for i in range(10):
                        for j in range(10):
                            if (pole[i][j] == 2 and j < 6) and (pole[i][j + 2] == 1 or pole[i][j + 2] == 3) and pole[i][
                                j + 4] == 0:
                                pole[i][j] = 0
                                pole[i][j + 2] = 0
                                pole[i][j + 4] = 2
                                white_count -= 1
                                vivod(-1, -1)
                                chernie_proverka()
                                hod_igroka = True
                if vozm_ch_zabrat_vpravo_vverh:
                    for i in range(10):
                        for j in range(10):
                            if (pole[i][j] == 2 and i > 1 and j < 8) and (pole[i - 1][j + 1] == 1 or pole[i - 1][j + 1] == 3) and \
                                    pole[i - 2][j + 2] == 0:
                                pole[i][j] = 0
                                pole[i - 1][j + 1] = 0
                                pole[i - 2][j + 2] = 2
                                white_count -= 1
                                vivod(-1, -1)
                                chernie_proverka()
                                hod_igroka = True
                if vozm_ch_zabrat_vlevo_vverh:
                    for i in range(10):
                        for j in range(10):
                            if (pole[i][j] == 2 and i > 1 and j > 1) and (
                                    pole[i - 1][j - 1] == 1 or pole[i - 1][j - 1] == 3) and \
                                    pole[i - 2][j - 2] == 0:
                                pole[i][j] = 0
                                pole[i - 1][j - 1] = 0
                                pole[i - 2][j - 2] = 2
                                white_count -= 1
                                vivod(-1, -1)
                                chernie_proverka()
                                hod_igroka = True
                if vozm_ch_zabrat_vpravo_vniz:
                    for i in range(10):
                        for j in range(10):
                            if (pole[i][j] == 2 and i < 8 and j < 8) and (
                                    pole[i + 1][j + 1] == 1 or pole[i + 1][j + 1] == 3) and \
                                    pole[i + 2][j + 2] == 0:
                                pole[i][j] = 0
                                pole[i + 1][j + 1] = 0
                                pole[i + 2][j + 2] = 2
                                white_count -= 1
                                vivod(-1, -1)
                                chernie_proverka()
                                hod_igroka = True
                if vozm_ch_zabrat_vlevo_vniz:
                    for i in range(10):
                        for j in range(10):
                            if (pole[i][j] == 2 and i < 8 and j > 1) and (
                                    pole[i + 1][j - 1] == 1 or pole[i + 1][j - 1] == 3) and \
                                    pole[i + 2][j - 2] == 0:
                                pole[i][j] = 0
                                pole[i + 1][j - 1] = 0
                                pole[i + 2][j - 2] = 2
                                white_count -= 1
                                vivod(-1, -1)
                                chernie_proverka()
                                hod_igroka = True
                if white_count == 0:
                    messagebox.showinfo(title='Победа черных', message='Победили черные.', icon='info')
                    hod_igroka = None
                    Start_new()
                chernie_proverka()
                if vozm_ch_zabrat == False and vozm_ch_d_zabrat == False:
                    hod_igroka = True
                    vivod(-1, -1)
                    break
def click_event(event):
    global hod_igroka
    global white_count
    global black_count
    global vozm_b_zabrat
    global vozm_b_zabrat_vverh
    global vozm_b_zabrat_vniz
    global vozm_b_zabrat_vlevo
    global vozm_b_zabrat_vpravo
    global vozm_b_zabrat_vpravo_vverh
    global vozm_b_zabrat_vlevo_vverh
    global vozm_b_zabrat_vlevo_vniz
    global vozm_b_zabrat_vpravo_vniz
    global vozm_b_d_zabrat_vverh
    global vozm_b_d_zabrat_vniz
    global vozm_b_d_zabrat_vlevo
    global vozm_b_d_zabrat_vpravo
    global vozm_b_d_zabrat
    global vozm_ch_zabrat_vverh
    global vozm_ch_zabrat_vniz
    global vozm_ch_zabrat_vlevo
    global vozm_ch_zabrat_vpravo
    global vozm_ch_zabrat_vpravo_vverh
    global vozm_ch_zabrat_vlevo_vverh
    global vozm_ch_zabrat_vlevo_vniz
    global vozm_ch_zabrat_vpravo_vniz
    global vozm_ch_zabrat
    global vozm_ch_d_zabrat_vverh
    global vozm_ch_d_zabrat_vniz
    global vozm_ch_d_zabrat_vlevo
    global vozm_ch_d_zabrat_vpravo
    global vozm_ch_d_zabrat
    global vozm_ch_d_zabrat_vpravo_vverh
    global vozm_ch_d_zabrat_vlevo_vverh
    global vozm_ch_d_zabrat_vlevo_vniz
    global vozm_ch_d_zabrat_vpravo_vniz

    global prev_b_coord_x
    global prev_b_coord_y
    global prev_ch_coord_x
    global prev_ch_coord_y
    global AI

    if 0 < event.x < 1000 and 0 < event.y < 1000:  # Если кликнули на доске
        x = event.y // 100  # Определяем строку на которую нажали
        y = event.x // 100  # Определяем столбец на который нажали

    if hod_igroka:
        if vozm_b_d_zabrat: # если у белых дамок есть возможность забрать черную шашку
            if vozm_b_d_zabrat_vverh:
                print("вверх")
                if pole[prev_b_coord_x][prev_b_coord_y] == 3 and prev_b_coord_x > 1 and pole[x][y] == 0 and prev_b_coord_y == y:
                    print("1")
                    print(x, prev_b_coord_x, pole[x + 1][y])
                    if x < prev_b_coord_x and x < 9 and pole[x + 2][y] == 2 or x < 9 and pole[x + 2][y] == 4:
                        print(x , prev_b_coord_x, pole[x+1][y])
                        print("2")
                        ch_count = 0
                        not_zero_count = 0
                        prev_x = prev_b_coord_x
                        for k in range(prev_b_coord_x, x, -1): # проверяем все ли клетки на пути пустые
                            ch_count += 1
                            if pole[prev_b_coord_x][y] != 0:
                                not_zero_count += 1
                            prev_b_coord_x -= 1
                        if not_zero_count == 2 and (pole[x + 2][y] == 2 or pole[x + 2][y] == 4): # если на пути ничего не мешает, то едим
                            print("3")
                            pole[x][y] = 3
                            pole[prev_x][prev_b_coord_y] = 0
                            pole[x + 2][y] = 0
                            black_count -= 1
                            vivod(-1, -1)

            if vozm_b_d_zabrat_vniz:
                if pole[prev_b_coord_x][prev_b_coord_y] == 3 and prev_b_coord_x < 9 and pole[x][y] == 0 and prev_b_coord_y == y:
                    if x > prev_b_coord_x and pole[x - 2][y] == 2 or pole[x - 2][y] == 4:
                        ch_count = 0
                        not_zero_count = 0
                        prev_x = prev_b_coord_x
                        for k in range(x, prev_b_coord_x, -1):
                            ch_count += 1
                            if pole[prev_b_coord_x][y] != 0:
                                not_zero_count += 1
                            prev_b_coord_x += 1
                        if not_zero_count == 2 and (pole[x - 2][y] == 2 or pole[x - 2][y] == 4):
                            pole[x][y] = 3
                            pole[prev_x][prev_b_coord_y] = 0
                            pole[x - 2][y] = 0
                            black_count -= 1
                            vivod(-1, -1)

            if vozm_b_d_zabrat_vlevo:
                if pole[prev_b_coord_x][prev_b_coord_y] == 3 and prev_b_coord_y > 1 and pole[x][y] == 0 and prev_b_coord_x == x:
                    if y < prev_b_coord_y and y < 9 and pole[x][y + 2] == 2 or y < 9 and pole[x][y + 2] == 4:
                        ch_count = 0
                        not_zero_count = 0
                        prev_y = prev_b_coord_y
                        for k in range(prev_b_coord_y, y, -1):
                            ch_count += 1
                            if pole[x][prev_b_coord_y] != 0:
                                not_zero_count += 1
                            prev_b_coord_y -= 1
                        if not_zero_count == 2 and (pole[x][y+2] == 2 or pole[x][y + 2] == 4):
                            pole[x][y] = 3
                            pole[prev_b_coord_x][prev_y] = 0
                            pole[x][y + 2] = 0
                            black_count -= 1
                            vivod(-1, -1)

            if vozm_b_d_zabrat_vpravo:
                if pole[prev_b_coord_x][prev_b_coord_y] == 3 and prev_b_coord_y < 8 and pole[x][y] == 0 and prev_b_coord_x == x:
                    if y > prev_b_coord_y and pole[x][y - 2] == 2 or pole[x][y - 2] == 4:
                        ch_count = 0
                        not_zero_count = 0
                        prev_y = prev_b_coord_y
                        for k in range(y, prev_b_coord_y, -1):
                            ch_count += 1
                            if pole[x][prev_b_coord_y] != 0:
                                not_zero_count += 1
                            prev_b_coord_y += 1
                        if not_zero_count == 2 and (pole[x][y-2] == 2 or pole[x][y - 2] == 4):
                            pole[x][y] = 3
                            pole[prev_b_coord_x][prev_y] = 0
                            pole[x][y - 2] = 0
                            black_count -= 1
                            vivod(-1, -1)
            if vozm_b_d_zabrat_vlevo_vverh:
                if prev_b_coord_x > x and prev_b_coord_y > y and (prev_b_coord_x - prev_b_coord_y == x - y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_b_coord_x
                    for k in range(prev_b_coord_x - x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_b_coord_x -= 1
                        if pole[prev_b_coord_x][prev_b_coord_y - l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 1 and (pole[x+1][y+1] == 2 or pole[x+1][y+1] == 4):
                        pole[x+1][y+1] = 0
                        pole[x][y] = 3
                        pole[prev_x][prev_b_coord_y] = 0
                        vivod(-1, -1)
                        black_count -= 1
            if vozm_b_d_zabrat_vpravo_vverh:
                if prev_b_coord_x > x and prev_b_coord_y < y and (prev_b_coord_x + prev_b_coord_y == x + y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_b_coord_x
                    for k in range(prev_b_coord_x - x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_b_coord_x -= 1
                        if pole[prev_b_coord_x][prev_b_coord_y + l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 1 and (pole[x+1][y-1] == 2 or pole[x+1][y-1] == 4):
                        pole[x+1][y-1] = 0
                        pole[x][y] = 3
                        pole[prev_x][prev_b_coord_y] = 0
                        vivod(-1, -1)
                        black_count -= 1
            if vozm_b_d_zabrat_vlevo_vniz:
                if prev_b_coord_x < x and prev_b_coord_y > y and (prev_b_coord_x + prev_b_coord_y == x + y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_b_coord_x
                    for k in range(x - prev_b_coord_x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_b_coord_x += 1
                        if pole[prev_b_coord_x][prev_b_coord_y - l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 1 and (pole[x-1][y+1] == 2 or pole[x-1][y+1] == 4):
                        pole[x-1][y+1] = 0
                        pole[x][y] = 3
                        pole[prev_x][prev_b_coord_y] = 0
                        vivod(-1, -1)
                        black_count -= 1
            if vozm_b_d_zabrat_vpravo_vniz:
                if prev_b_coord_x < x and prev_b_coord_y < y and (prev_b_coord_x - prev_b_coord_y == x - y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_b_coord_x
                    for k in range(x - prev_b_coord_x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_b_coord_x += 1
                        if pole[prev_b_coord_x][prev_b_coord_y + l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 1 and (pole[x-1][y-1] == 2 or pole[x-1][y-1] == 4):
                        pole[x-1][y-1] = 0
                        pole[x][y] = 3
                        pole[prev_x][prev_b_coord_y] = 0
                        vivod(-1, -1)
                        black_count -= 1
            vozm_b_d_zabrat = False
            belie_proverka()
            if vozm_b_d_zabrat == False:
                hod_igroka = False
                if black_count != 0:
                    AI_hod()
        if vozm_b_zabrat: # если возможность белых не дамок забрать
            if vozm_b_zabrat_vverh:
                if pole[prev_b_coord_x][prev_b_coord_y] == 1 and prev_b_coord_x > 3 and (pole[prev_b_coord_x - 2][y] == 2 or pole[prev_b_coord_x - 2][y] == 4) and pole[x][y] == 0 and pole[x + 4][y] == 1 and prev_b_coord_x == x + 4 and prev_b_coord_y == y:
                    if prev_b_coord_x == 4 and x == 0: # если прыгнули на поле, превращающее в дамку
                        pole[x][y] = 3
                    else:
                        pole[x][y] = 1
                    pole[x + 4][y] = 0
                    pole[x + 2][y] = 0
                    black_count -= 1
                    vivod(-1, -1)
            if vozm_b_zabrat_vniz:
                if pole[prev_b_coord_x][prev_b_coord_y] == 1 and prev_b_coord_x < 6 and (pole[prev_b_coord_x + 2][y] == 2 or pole[prev_b_coord_x + 2][y] == 4) and pole[x][y] == 0 and pole[x - 4][y] == 1 and prev_b_coord_x == x - 4 and prev_b_coord_y == y:
                    pole[x][y] = 1
                    pole[x-4][y] = 0
                    pole[x- 2][y] = 0
                    black_count -= 1
                    vivod(-1, -1)
            if vozm_b_zabrat_vlevo:
                if pole[prev_b_coord_x][prev_b_coord_y] == 1 and prev_b_coord_y > 3 and (pole[prev_b_coord_x][prev_b_coord_y - 2] == 2 or pole[prev_b_coord_x][prev_b_coord_y - 2] == 4) and pole[x][y] == 0 and pole[prev_b_coord_x][prev_b_coord_y - 4] == 0 and prev_b_coord_x == x and prev_b_coord_y == y + 4:
                    pole[prev_b_coord_x][y + 4] = 0
                    pole[x][y + 2] = 0
                    pole[x][y] = 1
                    black_count -= 1
                    vivod(-1, -1)

            if vozm_b_zabrat_vpravo:
                if pole[prev_b_coord_x][prev_b_coord_y] == 1 and prev_b_coord_y < 6 and (pole[prev_b_coord_x][prev_b_coord_y + 2] == 2 or pole[prev_b_coord_x][prev_b_coord_y + 2] == 4) and pole[x][y] == 0 and pole[prev_b_coord_x][prev_b_coord_y + 4] == 0 and prev_b_coord_x == x and prev_b_coord_y == y - 4:
                    pole[prev_b_coord_x][y - 4] = 0
                    pole[x][y - 2] = 0
                    pole[x][y] = 1
                    black_count -= 1
                    vivod(-1, -1)

            if vozm_b_zabrat_vlevo_vverh:
                if pole[prev_b_coord_x][prev_b_coord_y] == 1 and prev_b_coord_y > 1 and prev_b_coord_x > 1 and (pole[prev_b_coord_x - 1][prev_b_coord_y - 1] == 2 or pole[prev_b_coord_x - 1][prev_b_coord_y - 1] == 4) and pole[x][y] == 0 and pole[prev_b_coord_x - 2][prev_b_coord_y - 2] == 0 and prev_b_coord_x == x + 2 and prev_b_coord_y == y + 2:
                    pole[prev_b_coord_x][prev_b_coord_y] = 0
                    pole[prev_b_coord_x - 1][prev_b_coord_y - 1] = 0
                    if x == 0:
                        pole[x][y] = 3
                    else:
                        pole[x][y] = 1
                    black_count -= 1
                    vivod(-1, -1)

            if vozm_b_zabrat_vpravo_vverh:
                if pole[prev_b_coord_x][prev_b_coord_y] == 1 and prev_b_coord_y < 8 and prev_b_coord_x > 1 and (pole[prev_b_coord_x - 1][prev_b_coord_y + 1] == 2 or pole[prev_b_coord_x - 1][prev_b_coord_y + 1] == 4) and pole[x][y] == 0 and pole[prev_b_coord_x - 2][prev_b_coord_y + 2] == 0 and prev_b_coord_x == x + 2 and prev_b_coord_y == y - 2:
                    pole[prev_b_coord_x][prev_b_coord_y] = 0
                    pole[prev_b_coord_x - 1][prev_b_coord_y + 1] = 0
                    if x == 0:
                        pole[x][y] = 3
                    else:
                        pole[x][y] = 1
                    black_count -= 1
                    vivod(-1, -1)

            if vozm_b_zabrat_vlevo_vniz:
                if pole[prev_b_coord_x][prev_b_coord_y] == 1 and prev_b_coord_y > 1 and prev_b_coord_x < 8 and (pole[prev_b_coord_x + 1][prev_b_coord_y - 1] == 2 or pole[prev_b_coord_x + 1][prev_b_coord_y - 1] == 4) and pole[x][y] == 0 and pole[prev_b_coord_x + 2][prev_b_coord_y - 2] == 0 and prev_b_coord_x == x - 2 and prev_b_coord_y == y + 2:
                    pole[prev_b_coord_x][prev_b_coord_y] = 0
                    pole[prev_b_coord_x + 1][prev_b_coord_y - 1] = 0
                    pole[x][y] = 1
                    black_count -= 1
                    vivod(-1, -1)

            if vozm_b_zabrat_vpravo_vniz:
                if pole[prev_b_coord_x][prev_b_coord_y] == 1 and prev_b_coord_y < 8 and prev_b_coord_x < 8 and (pole[prev_b_coord_x + 1][prev_b_coord_y + 1] == 2 or pole[prev_b_coord_x + 1][prev_b_coord_y + 1] == 4) and pole[x][y] == 0 and pole[prev_b_coord_x + 2][prev_b_coord_y + 2] == 0 and prev_b_coord_x == x - 2 and prev_b_coord_y == y - 2:
                    pole[prev_b_coord_x][prev_b_coord_y] = 0
                    pole[prev_b_coord_x + 1][prev_b_coord_y + 1] = 0
                    pole[x][y] = 1
                    black_count -= 1
                    vivod(-1, -1)
            vozm_b_zabrat = False

            belie_proverka()
            if vozm_b_d_zabrat == False and vozm_b_zabrat == False:
                hod_igroka = False
                if black_count != 0:
                    AI_hod()
        belie_proverka()
        vozmozhnost_belih_hodit(x, y)
        if white_count == 0:
            messagebox.showinfo(title='Победа белыех', message='Победили белые.', icon='info')
            hod_igroka = None
            Start_new()
        belie_proverka()
        vivod(-1,-1)
        if vozmozhnost_belih_shodit: # если выбранная шашка может ходить(ей ничего не преграждает путь)
            vivod(-1, -1)
            if pole[x][y] == 1:
                board.create_rectangle(y * 100 + 100, x * 100 + 100, y * 100, x * 100, width=5, outline="Blue")
                if x > 0 and y > 0 and pole[x - 1][y - 1] == 0 and vozm_b_zabrat == False:
                    board.create_rectangle(y * 100 - 100, x * 100 - 100, y * 100, x * 100, width=5, outline="Green")
                if x > 0 and y < 9 and pole[x - 1][y + 1] == 0 and vozm_b_zabrat == False:
                    board.create_rectangle(y * 100 + 100, x * 100 - 100, y * 100 + 200, x * 100, width=5, outline="Green")
                if x > 3 and (pole[x-2][y] == 2 or pole[x-2][y] == 4) and pole[x-4][y] == 0:
                    board.create_rectangle(y * 100 + 100, x * 100 - 300, y * 100, x * 100 - 400, width=5, outline="Red")
                if x < 6 and (pole[x+2][y] == 2 or pole[x+2][y] == 4) and pole[x+4][y] == 0:
                    board.create_rectangle(y * 100 + 100, x * 100 + 500, y * 100, x * 100 + 400, width=5, outline="Red")
                if y < 6 and (pole[x][y + 2] == 2 or pole[x][y + 2] == 4) and pole[x][y + 4] == 0:
                    board.create_rectangle(y * 100 + 500, x * 100 + 100, y * 100 + 400, x * 100, width=5, outline="Red")
                if y > 3 and (pole[x][y - 2] == 2 or pole[x][y - 2] == 4) and pole[x][y - 4] == 0:
                    board.create_rectangle(y * 100 - 300, x * 100 + 100, y * 100 - 400, x * 100, width=5, outline="Red")
                if x > 1 and y > 1 and (pole[x-1][y-1] == 2 or pole[x-1][y-1] == 4) and pole[x-2][y-2] == 0:
                    board.create_rectangle(y * 100 - 200, x * 100 - 200, y * 100 - 100, x * 100 - 100, width=5, outline="Red")
                if x > 1 and y < 8 and (pole[x - 1][y + 1] == 2 or pole[x - 1][y + 1] == 4) and pole[x - 2][y + 2] == 0:
                    board.create_rectangle(y * 100 + 300, x * 100 - 200, y * 100 + 200, x * 100 - 100, width=5,outline="Red")
                if x < 8 and y > 1 and (pole[x + 1][y - 1] == 2 or pole[x + 1][y - 1] == 4) and pole[x + 2][y - 2] == 0:
                    board.create_rectangle(y * 100 - 200, x * 100 + 300, y * 100 - 100, x * 100 + 200, width=5,outline="Red")
                if x < 8 and y < 8 and (pole[x + 1][y + 1] == 2 or pole[x + 1][y + 1] == 4) and pole[x + 2][y + 2] == 0:
                    board.create_rectangle(y * 100 + 300, x * 100 + 300, y * 100 + 200, x * 100 + 200, width=5,outline="Red")

            if pole[prev_b_coord_x][prev_b_coord_y] != 0 and ((prev_b_coord_y == y + 1 and prev_b_coord_x == x + 1) or (prev_b_coord_y == y - 1 and prev_b_coord_x == x + 1)):  # Проверяем, сходили ли мы на одну клетку вертикально или горизонтально
                vivod(-1,-1)
                if pole[x][y] == 0 and vozm_b_zabrat == False and vozm_b_d_zabrat == False: # если эта клетка пустая и нету контроля для забирания(поедания)
                    if pole[prev_b_coord_x][prev_b_coord_y] == 1: # если сходили на поле, превращающее в дамку
                        if x == 0:
                            pole[x][y] = 3
                        else:
                            pole[x][y] = 1
                        pole[prev_b_coord_x][prev_b_coord_y] = 0
                        vivod(-1, -1)  # рисуем игровое поле
                        hod_igroka = False
                        if black_count != 0:
                            AI_hod()
            if pole[prev_b_coord_x][prev_b_coord_y] == 3 and pole[x][y] == 0 and vozm_b_zabrat == False and vozm_b_d_zabrat == False: # ходы для белой дамки
                if prev_b_coord_x > x and prev_b_coord_y > y and (prev_b_coord_x - prev_b_coord_y == x - y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_b_coord_x
                    for k in range(prev_b_coord_x - x): # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_b_coord_x -= 1
                        if pole[prev_b_coord_x][prev_b_coord_y - l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 0:
                        pole[x][y] = 3
                        pole[prev_x][prev_b_coord_y] = 0
                        vivod(-1,-1)
                        hod_igroka = False
                        if black_count != 0:
                            AI_hod()

                if prev_b_coord_x > x and prev_b_coord_y < y and (prev_b_coord_x + prev_b_coord_y == x + y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_b_coord_x
                    for k in range(prev_b_coord_x - x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_b_coord_x -= 1
                        if pole[prev_b_coord_x][prev_b_coord_y + l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 0:
                        pole[x][y] = 3
                        pole[prev_x][prev_b_coord_y] = 0
                        vivod(-1, -1)
                        hod_igroka = False
                        if black_count != 0:
                            AI_hod()
                if prev_b_coord_x < x and prev_b_coord_y > y and (prev_b_coord_x + prev_b_coord_y == x + y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_b_coord_x
                    for k in range(x - prev_b_coord_x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_b_coord_x += 1
                        if pole[prev_b_coord_x][prev_b_coord_y - l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 0:
                        pole[x][y] = 3
                        pole[prev_x][prev_b_coord_y] = 0
                        vivod(-1, -1)
                        hod_igroka = False
                        if black_count != 0:
                            AI_hod()
                if prev_b_coord_x < x and prev_b_coord_y < y and (prev_b_coord_x - prev_b_coord_y == x - y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_b_coord_x
                    for k in range(x - prev_b_coord_x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_b_coord_x += 1
                        if pole[prev_b_coord_x][prev_b_coord_y + l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 0:
                        pole[x][y] = 3
                        pole[prev_x][prev_b_coord_y] = 0
                        vivod(-1, -1)
                        hod_igroka = False
                        if black_count != 0:
                            AI_hod()
        else:
            vivod(-1,-1)
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################


    if not hod_igroka:

        if vozm_ch_d_zabrat:
            if vozm_ch_d_zabrat_vverh:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 4 and prev_b_coord_x > 1 and pole[x][
                    y] == 0 and prev_ch_coord_y == y:
                    if x < prev_ch_coord_x and x < 9 and pole[x + 1][y] == 1 or x < 9 and pole[x + 1][y] == 3:
                        ch_count = 0
                        not_zero_count = 0
                        prev_x = prev_ch_coord_x
                        for k in range(prev_ch_coord_x, x, -1):  # проверяем все ли клетки на пути пустые
                            ch_count += 1
                            if pole[prev_ch_coord_x][y] != 0:
                                not_zero_count += 1
                            prev_ch_coord_x -= 1
                        if not_zero_count == 2 and (pole[x + 2][y] == 1 or pole[x + 2][y] == 3):  # если на пути ничего не мешает, то едим
                            pole[x][y] = 4
                            pole[prev_x][prev_ch_coord_y] = 0
                            pole[x + 2][y] = 0
                            white_count -= 1
                            vivod(-1, -1)

            if vozm_ch_d_zabrat_vniz:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 4 and prev_ch_coord_x < 9 and pole[x][
                    y] == 0 and prev_ch_coord_y == y:
                    if x > prev_ch_coord_x and pole[x - 1][y] == 1 or pole[x - 1][y] == 3:
                        ch_count = 0
                        not_zero_count = 0
                        prev_x = prev_ch_coord_x
                        for k in range(x, prev_ch_coord_x, -1):
                            ch_count += 1
                            if pole[prev_ch_coord_x][y] != 0:
                                not_zero_count += 1
                            prev_ch_coord_x += 1
                        if not_zero_count == 2 and (pole[x + 2][y] == 1 or pole[x + 2][y] == 3):
                            pole[x][y] = 4
                            pole[prev_x][prev_ch_coord_y] = 0
                            pole[x - 2][y] = 0
                            white_count -= 1
                            vivod(-1, -1)

            if vozm_ch_d_zabrat_vlevo:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 4 and prev_ch_coord_y > 1 and pole[x][
                    y] == 0 and prev_ch_coord_x == x:
                    if y < prev_ch_coord_y and y < 9 and pole[x][y + 1] == 1 or y < 9 and pole[x][y + 1] == 3:
                        ch_count = 0
                        not_zero_count = 0
                        prev_y = prev_ch_coord_y
                        for k in range(prev_ch_coord_y, y, -1):
                            ch_count += 1
                            if pole[x][prev_ch_coord_y] != 0:
                                not_zero_count += 1
                            prev_ch_coord_y -= 1
                        if not_zero_count == 2 and (pole[x][y + 2] == 1 or pole[x][y + 2] == 3):
                            pole[x][y] = 3
                            pole[prev_ch_coord_x][prev_y] = 0
                            pole[x][y + 2] = 0
                            white_count -= 1
                            vivod(-1, -1)

            if vozm_ch_d_zabrat_vpravo:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 4 and prev_ch_coord_y < 8 and pole[x][
                    y] == 0 and prev_ch_coord_x == x:
                    if y > prev_ch_coord_y and pole[x][y - 1] == 1 or pole[x][y - 1] == 3:
                        ch_count = 0
                        not_zero_count = 0
                        prev_y = prev_ch_coord_y
                        for k in range(y, prev_ch_coord_y, -1):
                            ch_count += 1
                            if pole[x][prev_ch_coord_y] != 0:
                                not_zero_count += 1
                            prev_ch_coord_y += 1
                        if not_zero_count == 2 and (pole[x][y - 2] == 1 or pole[x][y - 2] == 3):
                            pole[x][y] = 3
                            pole[prev_b_coord_x][prev_y] = 0
                            pole[x][y - 2] = 0
                            white_count -= 1
                            vivod(-1, -1)
            if vozm_ch_d_zabrat_vlevo_vverh:
                if prev_ch_coord_x > x and prev_ch_coord_y > y and (prev_ch_coord_x - prev_ch_coord_y == x - y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_ch_coord_x
                    for k in range(prev_ch_coord_x - x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_ch_coord_x -= 1
                        if pole[prev_ch_coord_x][prev_ch_coord_y - l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 1 and (pole[x + 1][y + 1] == 1 or pole[x + 1][y + 1] == 3):
                        pole[x + 1][y + 1] = 0
                        pole[x][y] = 4
                        pole[prev_x][prev_ch_coord_y] = 0
                        vivod(-1, -1)
                        white_count -= 1
            if vozm_ch_d_zabrat_vpravo_vverh:
                if prev_ch_coord_x > x and prev_ch_coord_y < y and (prev_ch_coord_x + prev_ch_coord_y == x + y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_ch_coord_x
                    for k in range(prev_ch_coord_x - x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_ch_coord_x -= 1
                        if pole[prev_ch_coord_x][prev_ch_coord_y + l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 1 and (pole[x + 1][y - 1] == 1 or pole[x + 1][y - 1] == 3):
                        pole[x + 1][y - 1] = 0
                        pole[x][y] = 4
                        pole[prev_x][prev_ch_coord_y] = 0
                        vivod(-1, -1)
                        white_count -= 1
            if vozm_ch_d_zabrat_vlevo_vniz:
                if prev_ch_coord_x < x and prev_ch_coord_y > y and (prev_ch_coord_x + prev_ch_coord_y == x + y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_ch_coord_x
                    for k in range(x - prev_ch_coord_x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_ch_coord_x += 1
                        if pole[prev_ch_coord_x][prev_ch_coord_y - l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 1 and (pole[x - 1][y + 1] == 1 or pole[x - 1][y + 1] == 3):
                        pole[x - 1][y + 1] = 0
                        pole[x][y] = 4
                        pole[prev_x][prev_ch_coord_y] = 0
                        vivod(-1, -1)
                        white_count -= 1
            if vozm_ch_d_zabrat_vpravo_vniz:
                if prev_ch_coord_x < x and prev_ch_coord_y < y and (prev_ch_coord_x - prev_ch_coord_y == x - y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_ch_coord_x
                    for k in range(x - prev_ch_coord_x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_ch_coord_x += 1
                        if pole[prev_ch_coord_x][prev_ch_coord_y + l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 1 and (pole[x - 1][y - 1] == 1 or pole[x - 1][y - 1] == 3):
                        pole[x - 1][y - 1] = 0
                        pole[x][y] = 4
                        pole[prev_x][prev_ch_coord_y] = 0
                        vivod(-1, -1)
                        white_count -= 1

            vozm_ch_d_zabrat = False
            chernie_proverka()
            if vozm_ch_d_zabrat == False:
                hod_igroka = True
        if vozm_ch_zabrat:  # если возможность белых не дамок забрать
            if vozm_ch_zabrat_vverh:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 2 and prev_ch_coord_x > 3 and (
                        pole[prev_ch_coord_x - 2][y] == 1 or pole[prev_ch_coord_x - 2][y] == 3) and pole[x][y] == 0 and \
                        pole[x + 4][y] == 2 and prev_ch_coord_x == x + 4 and prev_ch_coord_y == y:

                    pole[x][y] = 2
                    pole[x + 4][y] = 0
                    pole[x + 2][y] = 0
                    white_count -= 1
                    vivod(-1, -1)
            if vozm_ch_zabrat_vniz:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 2 and prev_ch_coord_x < 6 and (
                        pole[prev_ch_coord_x + 2][y] == 1 or pole[prev_ch_coord_x + 2][y] == 3) and pole[x][y] == 0 and \
                        pole[x - 4][y] == 2 and prev_ch_coord_x == x - 4 and prev_ch_coord_y == y:
                    if prev_ch_coord_x == 5 and x - 2 == 7 and x == 9:
                        pole[x][y] = 4
                    else:
                        pole[x][y] = 2
                    pole[x - 4][y] = 0
                    pole[x - 2][y] = 0
                    white_count -= 1
                    vivod(-1, -1)
            if vozm_ch_zabrat_vlevo:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 2 and prev_ch_coord_y > 3 and (
                        pole[prev_ch_coord_x][prev_ch_coord_y - 2] == 1 or pole[prev_ch_coord_x][
                    prev_ch_coord_y - 2] == 3) and pole[x][y] == 0 and pole[prev_ch_coord_x][
                    prev_ch_coord_y - 4] == 0 and prev_ch_coord_x == x and prev_ch_coord_y == y + 4:
                    pole[prev_ch_coord_x][y + 4] = 0
                    pole[x][y + 2] = 0
                    pole[x][y] = 2
                    white_count -= 1
                    vivod(-1, -1)

            if vozm_ch_zabrat_vpravo:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 2 and prev_ch_coord_y < 6 and (
                        pole[prev_ch_coord_x][prev_ch_coord_y + 2] == 1 or pole[prev_ch_coord_x][
                    prev_ch_coord_y + 2] == 3) and pole[x][y] == 0 and pole[prev_ch_coord_x][
                    prev_ch_coord_y + 4] == 0 and prev_ch_coord_x == x and prev_ch_coord_y == y - 4:
                    pole[prev_ch_coord_x][y - 4] = 0
                    pole[x][y - 2] = 0
                    pole[x][y] = 2
                    white_count -= 1
                    vivod(-1, -1)

            if vozm_ch_zabrat_vlevo_vverh:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 2 and prev_ch_coord_y > 1 and prev_ch_coord_x > 1 and (
                        pole[prev_ch_coord_x - 1][prev_ch_coord_y - 1] == 1 or pole[prev_ch_coord_x - 1][
                    prev_ch_coord_y - 1] == 3) and pole[x][y] == 0 and pole[prev_ch_coord_x - 2][
                    prev_ch_coord_y - 2] == 0 and prev_ch_coord_x == x + 2 and prev_ch_coord_y == y + 2:
                    pole[prev_ch_coord_x][prev_ch_coord_y] = 0
                    pole[prev_ch_coord_x - 1][prev_ch_coord_y - 1] = 0
                    pole[x][y] = 2
                    white_count -= 1
                    vivod(-1, -1)

            if vozm_ch_zabrat_vpravo_vverh:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 2 and prev_ch_coord_y < 8 and prev_ch_coord_x > 1 and (
                        pole[prev_ch_coord_x - 1][prev_ch_coord_y + 1] == 1 or pole[prev_ch_coord_x - 1][
                    prev_ch_coord_y + 1] == 3) and pole[x][y] == 0 and pole[prev_ch_coord_x - 2][
                    prev_ch_coord_y + 2] == 0 and prev_ch_coord_x == x + 2 and prev_ch_coord_y == y - 2:
                    pole[prev_ch_coord_x][prev_ch_coord_y] = 0
                    pole[prev_ch_coord_x - 1][prev_ch_coord_y + 1] = 0
                    pole[x][y] = 2
                    white_count -= 1
                    vivod(-1, -1)

            if vozm_ch_zabrat_vlevo_vniz:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 2 and prev_ch_coord_y > 1 and prev_ch_coord_x < 8 and (
                        pole[prev_ch_coord_x + 1][prev_ch_coord_y - 1] == 1 or pole[prev_ch_coord_x + 1][
                    prev_ch_coord_y - 1] == 3) and pole[x][y] == 0 and pole[prev_ch_coord_x + 2][
                    prev_ch_coord_y - 2] == 0 and prev_ch_coord_x == x - 2 and prev_ch_coord_y == y + 2:
                    pole[prev_ch_coord_x][prev_ch_coord_y] = 0
                    pole[prev_ch_coord_x + 1][prev_ch_coord_y - 1] = 0
                    pole[x][y] = 2
                    white_count -= 1
                    vivod(-1, -1)

            if vozm_ch_zabrat_vpravo_vniz:
                if pole[prev_ch_coord_x][prev_ch_coord_y] == 2 and prev_ch_coord_y < 8 and prev_ch_coord_x < 8 and (
                        pole[prev_ch_coord_x + 1][prev_ch_coord_y + 1] == 1 or pole[prev_ch_coord_x + 1][
                    prev_ch_coord_y + 1] == 3) and pole[x][y] == 0 and pole[prev_ch_coord_x + 2][
                    prev_ch_coord_y + 2] == 0 and prev_ch_coord_x == x - 2 and prev_ch_coord_y == y - 2:
                    pole[prev_ch_coord_x][prev_ch_coord_y] = 0
                    pole[prev_ch_coord_x + 1][prev_ch_coord_y + 1] = 0
                    pole[x][y] = 2
                    white_count -= 1
                    vivod(-1, -1)

            vozm_ch_zabrat = False
            chernie_proverka()
            if vozm_ch_zabrat == False and vozm_ch_d_zabrat == False:
                hod_igroka = True
        vozmozhnost_chernih_hodit(x, y)
        if black_count == 0:
            messagebox.showinfo(title='Победа черных', message='Победили черные.', icon='info')
            hod_igroka = None
            Start_new()
        if vozmozhnost_chernih_shodit:
            if pole[prev_ch_coord_x][prev_ch_coord_y] != 0 and ((prev_ch_coord_y == y + 1 and prev_ch_coord_x == x - 1) or (prev_ch_coord_y == y - 1 and prev_ch_coord_x == x - 1)):  # Проверяем, сходили ли мы на одну клетку вертикально или горизонтально
                vivod(-1, -1)
                if pole[x][y] == 0 and vozm_ch_zabrat == False and vozm_ch_d_zabrat == False:
                    if pole[prev_ch_coord_x][prev_ch_coord_y] == 2:
                        if x == 8:
                            pole[x][y] = 4
                        else:
                            pole[x][y] = 2
                        pole[prev_ch_coord_x][prev_ch_coord_y] = 0
                        vivod(-1, -1)  # рисуем игровое поле
                        hod_igroka = True
            if pole[prev_ch_coord_x][prev_ch_coord_y] == 4 and pole[x][
                y] == 0 and vozm_ch_zabrat == False and vozm_ch_d_zabrat == False:  # ходы для белой дамки
                if prev_ch_coord_x > x and prev_ch_coord_y > y and (prev_ch_coord_x - prev_ch_coord_y == x - y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_ch_coord_x
                    for k in range(prev_ch_coord_x - x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_ch_coord_x -= 1
                        if pole[prev_ch_coord_x][prev_ch_coord_y - l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 0:
                        pole[x][y] = 4
                        pole[prev_x][prev_ch_coord_y] = 0
                        vivod(-1, -1)
                        hod_igroka = True

                if prev_ch_coord_x > x and prev_ch_coord_y < y and (prev_ch_coord_x + prev_ch_coord_y == x + y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_ch_coord_x
                    for k in range(prev_ch_coord_x - x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_ch_coord_x -= 1
                        if pole[prev_ch_coord_x][prev_ch_coord_y + l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 0:
                        pole[x][y] = 4
                        pole[prev_x][prev_ch_coord_y] = 0
                        vivod(-1, -1)
                        hod_igroka = True
                if prev_ch_coord_x < x and prev_ch_coord_y > y and (prev_ch_coord_x + prev_ch_coord_y == x + y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_ch_coord_x
                    for k in range(x - prev_ch_coord_x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_ch_coord_x += 1
                        if pole[prev_ch_coord_x][prev_ch_coord_y - l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 0:
                        pole[x][y] = 4
                        pole[prev_x][prev_ch_coord_y] = 0
                        vivod(-1, -1)
                        hod_igroka = True
                if prev_ch_coord_x < x and prev_ch_coord_y < y and (prev_ch_coord_x - prev_ch_coord_y == x - y):
                    l = 0
                    ch_count = 0
                    not_zero_count = 0
                    prev_x = prev_ch_coord_x
                    for k in range(x - prev_ch_coord_x):  # проверка на пустой путь до выбранной клетки
                        l += 1
                        ch_count += 1
                        prev_ch_coord_x += 1
                        if pole[prev_ch_coord_x][prev_ch_coord_y + l] != 0:
                            not_zero_count += 1
                    if not_zero_count == 0:
                        pole[x][y] = 4
                        pole[prev_x][prev_ch_coord_y] = 0
                        vivod(-1, -1)
                        hod_igroka = True









class Ui_Login(object):
    global cipher, p_cipher
    def Correct(self):
        global cipher, p_cipher
        cipher = ''
        p_cipher = ''
        def encryption(text):
            # Выбрать два простых различных числа
            p, q = 89, 107
            # Вычислить произведение
            n = p * q
            # Вычислить функцию Эйлера
            fi = (p - 1) * (q - 1)
            # Выбрать открытую экспоненту
            en = 3

            # Вычислить шифротекст
            def encrypt(val):
                cypher = (val ** en) % n
                return (cypher)

            # Итоговая функция шифрования
            def rsa_encrypt(text):
                global cipher,p_cipher
                global encrypte
                encrypte = []
                for i in range(len(text)):
                    encrypte.append(encrypt(ord(text[i])))
                return encrypte
            global cipher, p_cipher
            cipher = rsa_encrypt(text)
            cipher = ' '.join(map(str, cipher))
            p_cipher = rsa_encrypt(text)
            p_cipher = ' '.join(map(str, p_cipher))

        u_ind = 0
        p_ind = 0
        encryption(self.lineEdit.text())
        word = cipher

        with open(r'src/username.txt', 'r') as fp:
            # read all lines in a list
            lines = fp.readlines()
            for line in lines:
                line = ('\n'.join(filter(bool, line.split('\n'))))
                u_ind += 1
                if (word == line):
                    self.u_ind = u_ind
                    break
                if ((self.lineEdit_2.text() == "") or (self.lineEdit.text() == "")):
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Поле Username или Password не может быть пустым")
                    msg.setWindowTitle("Пустое поле")
                    msg.exec_()
                    break

        encryption(self.lineEdit_2.text())
        p_word = p_cipher

        with open(r'src/password.txt', 'r') as fp:
            # read all lines in a list
            p_lines = fp.readlines()
            for p_line in p_lines:
                p_line = ('\n'.join(filter(bool, p_line.split('\n'))))
                p_ind += 1
                if (p_word == p_line):
                    self.p_ind = p_ind

                    if self.p_ind == self.u_ind:
                        break

                if ((self.lineEdit_2.text() == "") or (self.lineEdit.text() == "")):
                    break

        try:
            if (p_word == p_line) and (word == line):
                print()
        except:
            line = ""
            p_line = ""
        if (p_word == p_line) and (word == line):
            if ((p_ind == u_ind) and ((p_ind or u_ind) != 0)):
                global Username
                Username = cipher
                LoginForm.close()
                LK.show()
                self.instance = Ui_LK()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(
                    "Вы успешно вошли")
                msg.setWindowTitle("Успешный вход")
                msg.exec_()
                li.label_12.setText("Username: " + ui.lineEdit.text())
                self.lineEdit.setText("")
                self.lineEdit_2.setText("")

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Такой Username или Password не существует")
                msg.setWindowTitle("Неправильные данные")
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Такой Username или Password не существует")
            msg.setWindowTitle("Неправильные данные")
            msg.exec_()

    def encryptUser(self):
        global cipher,p_cipher
        cipher = ''
        p_cipher = ''
        def encryption(text):
            global cipher, p_cipher
            # Выбрать два простых различных числа
            p, q = 89, 107
            # Вычислить произведение
            n = p * q
            # Вычислить функцию Эйлера
            fi = (p - 1) * (q - 1)
            # Выбрать открытую экспоненту
            en = 3

            # Вычислить шифротекст
            def encrypt(val):
                cypher = (val ** en) % n
                return (cypher)

            # Итоговая функция шифрования
            def rsa_encrypt(text):
                global encrypte
                encrypte = []
                for i in range(len(text)):
                    encrypte.append(encrypt(ord(text[i])))
                return encrypte
            cipher = rsa_encrypt(text)
            cipher = ' '.join(map(str, cipher))
            p_cipher = rsa_encrypt(text)
            p_cipher = ' '.join(map(str, p_cipher))
        encryption(self.lineEdit.text())
        word = cipher

        if self.lineEdit.text() == "" or self.lineEdit_2.text() == "" :
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(
                "Присутствуют пустые поля")
            msg.setWindowTitle("Неправильные данные")
            msg.exec_()
        else:
            with open(r'src/username.txt', 'r') as fp:
                # read all lines in a list
                lines = fp.readlines()
                for line in lines:
                    line = ('\n'.join(filter(bool, line.split('\n'))))
                    if word == line:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText(
                            "Такой пользователь уже существует")
                        msg.setWindowTitle("Неправильные данные")
                        msg.exec_()
                        break
                else:

                    with open("src/username.txt", 'a', encoding='utf-8') as file:
                        file.write(f'{cipher}\n')
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setText("Вы успешно зарегистрировались")
                        msg.setWindowTitle("Успешная регистрация")
                        msg.exec_()


            encryption(self.lineEdit_2.text())
            p_word = ' '.join(map(str, p_cipher))
            with open(r'src/password.txt', 'r') as fp_file:
                # read all lines in a list
                p_lines = fp_file.readlines()
                for p_line in p_lines:
                    p_line = ('\n'.join(filter(bool, p_line.split('\n'))))
                    if word == line or word == "" or self.lineEdit.text() == "" or self.lineEdit_2.text() == "":
                        break;
                else:

                    with open("src/password.txt", 'a', encoding='utf-8') as p_file:
                        p_file.write(f'{p_cipher}\n')
            return cipher

    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(1120, 880)
        LoginForm.setStyleSheet("background-color: rgb(172,183,142);\n"
"border-radius: 50px;")
        self.label = QtWidgets.QLabel(LoginForm)
        self.label.setGeometry(QtCore.QRect(530, 130, 91, 101))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("src/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(LoginForm)
        self.frame.setGeometry(QtCore.QRect(160, 270, 800, 511))
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("\n"
"background-color: rgb(236,234,190);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(190, 50, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setMouseTracking(False)
        self.label_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_2.setAcceptDrops(False)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setIndent(25)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(190, 160, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setStyleSheet("background-color: rgb(255,255,255);\n"
"padding-left: 8px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 220, 421, 41))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255,255,255);\n"
"padding-left: 8px;\n"
"\n"
"")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(190, 370, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(179,159,122);")
        self.pushButton.setObjectName("pushButton")
#################################Button Event#######################
        self.pushButton.clicked.connect(self.encryptUser)
####################################################################
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 300, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(179,159,122);")
        self.pushButton_2.setObjectName("pushButton_2")
#################################Button Event#######################
        self.pushButton_2.clicked.connect(self.Correct)
####################################################################
        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "LoginForm"))
        self.label_2.setText(_translate("LoginForm", "    Авторизация"))
        self.lineEdit.setPlaceholderText(_translate("LoginForm", "Имя пользователя"))
        self.lineEdit_2.setPlaceholderText(_translate("LoginForm", "Пароль"))
        self.pushButton.setText(_translate("LoginForm", "Зарегистрироваться"))
        self.pushButton_2.setText(_translate("LoginForm", "Войти"))

############################Другой класс###########################################

class Ui_LK(object):
    def start_game(self):
        LK.hide()

        self.label_13.setText(winner[0])

    def ToLoginForm(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Вы действительно хотите вернуться на главную страницу? ")
        msg.setWindowTitle("Выход")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()
        result = msg.standardButton(msg.clickedButton())
        if result == 1024:
            LK.close()
            LoginForm.show()
    def setupUi(self, LK):
        LK.setObjectName("LK")
        LK.resize(750, 550)
        LK.setStyleSheet("background-color: rgb(172,183,142);\n"
"\n"
"border-radius: 10px;")

        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton = QtWidgets.QPushButton(LK)
        self.pushButton.setGeometry(QtCore.QRect(100, 230, 180, 35))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("background-color: rgb(179,159,122);")
        self.pushButton.setObjectName("pushButton")
#######################################################################################################################################

#######################################################################################################################################
        self.pushButton_2 = QtWidgets.QPushButton(LK)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 230, 180, 35))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(179,159,122);")
        self.pushButton_2.setObjectName("pushButton_2")
#######################################################################################################################################
        self.pushButton_2.clicked.connect(self.ToLoginForm)
        self.label_12 = QtWidgets.QLabel(LK)
        self.label_12.setGeometry(QtCore.QRect(50, 20, 701, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(0,0,0);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(LK)
        self.label_13.setGeometry(QtCore.QRect(50, 320, 701, 351))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(19)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(255,255,255);")
        self.label_13.setObjectName("label_13")
        self.pushButton.clicked.connect(self.start_game_in_lk)
        self.pushButton.clicked.connect(self.OpenClick2)


        self.retranslateUi(LK)
        QtCore.QMetaObject.connectSlotsByName(LK)

    def start_game_in_lk(self):
        LK.hide()
        izobrazheniya_figur()  # здесь загружаем изображения пешек
        novaya_igra()  # начинаем новую игру
        vivod(-1, -1)  # рисуем игровое поле
        board.bind("<Button-1>", click_event)  # нажатие левой кнопки
        mainloop()


    def retranslateUi(self, LK):
        _translate = QtCore.QCoreApplication.translate
        LK.setWindowTitle(_translate("LK", "Личный кабинет"))
        self.pushButton.setText(_translate("LK", "Играть"))
        self.pushButton_2.setText(_translate("LK", "Выход"))
        self.label_12.setText(_translate("LK", "Username: "))
        self.label_13.setText(_translate("Dialog", ""))

    def OpenClick2(self):
        LK.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    LoginForm = QtWidgets.QDialog()
    LK = QtWidgets.QDialog()

    ui = Ui_Login()
    li = Ui_LK()

    ui.setupUi(LoginForm)
    li.setupUi(LK)
    LoginForm.show()

    sys.exit(app.exec_())
#значимых строк 2056
