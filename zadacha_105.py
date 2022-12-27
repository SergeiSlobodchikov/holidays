# Задача 105 Напишите программу, удаляющую из текста все слова, содержащие ""абв"
def DeleteAbV():
    text = str(input(f'Введите текст или вставьте его и мы удалим все слова имеющие букву А, б и в \n'))
    mass = text.split()
    index_element = 0
    dell = 0
    for word in mass:
        for char in word:
            if char == 'а' or char == 'A' or char == 'a' or char == 'A':
                dell = 1
            elif char == 'б' or char == 'Б' or char == 'b' or char == 'B':
                dell = 1
            elif char == 'в' or char == 'В' or char == 'v' or char == 'V':
                dell = 1
        if dell == 1:
            mass.pop(index_element)
            mass.insert(index_element, '')
            dell = 0
        index_element = index_element + 1

    text = ' '.join(mass)
    text = ' '.join(text.split())
    print(text)

DeleteAbV()