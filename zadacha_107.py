# Задача 107 Создайте программу для игры в ""Крестики-нолики"" (Добавьте игру против бота)
# Инициализация карты
from random import randint
pole = [7, 8, 9,
        4, 5, 6,
        1, 2, 3]

# Инициализация победных линий
victories = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]

# Вывод карты на экран
def print_pole():
    print(f'╔═══╦═══╦═══╗')
    print(f'║ {pole[0]}', end=" ")
    print(f'║ {pole[1]} ║', end=" ")
    print(f'{pole[2]} ║')
    print(f'╠═══╬═══╬═══╣')
    print(f'║ {pole[3]}', end=" ")
    print(f'║ {pole[4]} ║', end=" ")
    print(f'{pole[5]} ║')
    print(f'╠═══╬═══╬═══╣')
    print(f'║ {pole[6]}', end=" ")
    print(f'║ {pole[7]} ║', end=" ")
    print(f'{pole[8]} ║')
    print(f'╚═══╩═══╩═══╝\n')

# Сделать ход в ячейку
def step_pole(step, symbol):
    ind = pole.index(step)
    pole[ind] = symbol

# Получить текущий результат игры
def get_result():
    win = ""
    for i in victories:
        if pole[i[0]] == "X" and pole[i[1]] == "X" and pole[i[2]] == "X":
            win = "X"
        if pole[i[0]] == "O" and pole[i[1]] == "O" and pole[i[2]] == "O":
            win = "O"

    return win

# Поиск линии с нужным количеством X и O на победных линиях
def check_line(sum_O, sum_X):

    step = ""
    for line in victories:
        o = 0
        x = 0

        for j in range(0, 3):
            if pole[line[j]] == "O":
                o = o + 1
            if pole[line[j]] == "X":
                x = x + 1

        if o == sum_O and x == sum_X:
            for j in range(0, 3):
                if pole[line[j]] != "O" and pole[line[j]] != "X":
                    step = pole[line[j]]
    return step

# Искусственный интеллект: выбор хода
def AI(side_0):
    # сжалится компьютер или нет зависит от удачи
    luck = randint(0, 6)
    step = ""
    if side_0 == 1:
        step = check_line(0, 2)
        # если на какой либо из победных линий 2 чужие фигуры и 0 своих - ставим
        if step == "" and luck == 1:
            step = check_line(2, 0)
        # если 1 фигура своя и 0 чужих - ставим
        if step == "":
            step = check_line(0, 1)
        # центр пуст, то занимаем центр
        if step == "":
            if pole[4] != "X" and pole[4] != "O" and luck == 1:
                step = 5
        # если центр занят, то занимаем ячейку
        if step == "":
            for i in range(10):
                if pole[i] != "X" and pole[i] != "O":
                    step = i+1
                    break
    else:
        step = check_line(2, 0)
        # если на какой либо из победных линий 2 чужие фигуры и 0 своих - ставим
        if step == "" and luck != 1:
            step = check_line(0, 2)
        # если 1 фигура своя и 0 чужих - ставим
        if step == "":
            step = check_line(1, 0)
        # центр пуст, то занимаем центр
        if step == "":
            if pole[4] != "X" and pole[4] != "O"  and luck == 1:
                step = 5
        # если центр занят, то занимаем ячейку
        if step == "":
            for i in range(9):
                if pole[i] != "X" and pole[i] != "O":
                    step = i+1
                    break

    return step


# Основная программа
game_over = False
side = input(f"За кого играете введите х или 0??\n").lower()
if side == 0 or side == '0' or side == 'o' or side == 'о':
    side_0 = 1
    human = False
else:
    side_0 = 0
    human = True

shag = 0
while game_over == False:
    print_pole()

    if human == True:
        if side_0 == 1:
            symbol = "O"
        else:
            symbol = "X"
        step = int(input("Человек, ваш ход: "))
    else:
        print("Компьютер делает ход: ")
        if side_0 == 1:
            symbol = "X"
        else:
            symbol = "O"
        step = AI(side_0)
    shag +=1
    # Если компьютер нашел куда сделать ход, то играем. Если нет, то ничья.
    print(shag)
    if shag != 9:
        if step != "":
            step_pole(step, symbol)  # делаем ход в указанную ячейку
            win = get_result()  # определим победителя
            if win != "":
                game_over = True
            else:
                game_over = False
 
    else:
        print("Ничья!")
        game_over = True
        win = "дружба"

    human = not (human)

# Игра окончена. Покажем карту. Объявим победителя.
print_pole()
print("Победил", win)

