# A. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# B. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]
from random import randint

# Создаем словарь для степеней многочлена
def RandomPolynomial(): 
        dictionary = {}
        k = int(input('Введите число степени многочлена-> '))
        for i in range(k, -1, -1):
            dictionary[i] = randint(-100, 100)
        return dictionary  

# Словарь пишем в строку для красивого оформления многочленов 
def StringBeautiful(dictionary: dict):
    my_str = ' '
    keys = dictionary.keys()
    max = 0
    for i in keys: 
        if i > max:
            max = i 
    if dictionary.get(max, 0) < 0:
        my_str = ' -'

    for step in range(max,-1, -1):
        znachenie = dictionary.get(step, 0)
        if znachenie == 0:
            my_str += ''
        else: 
            if step == 0: 
                my_str += f'{abs(znachenie)}'
            elif step == 1:
                if abs(znachenie) == 1:
                    my_str += 'x'
                else:
                    my_str += f'{abs(znachenie)}x'
            else:
                if abs(znachenie) == 1:
                    my_str += f'x^{step}'
                else:
                    my_str += f'{abs(znachenie)}x^{step}'
        if step != 0 and dictionary.get(step - 1) != 0:
            if dictionary.get(step - 1, 0) > 0:
                my_str += ' + '
            elif dictionary.get(step - 1, 0) < 0:
                my_str += ' - '
    my_str += f' = 0'
    return my_str


# Строку с примерами многочленов делаем в список удаляя лишние знаки
def ReplacePolynomial(data):
    for line in data:
        stroka = line
    yravnenieOne = stroka.replace(' - x ',' -1 ^1 ').replace(' x ',' 1 ^1 ').replace('-x','-1')
    yravnenieOne = yravnenieOne.replace('- x','-1').replace(' x','1').replace(' ','').replace('=0','')
    yravnenieOne = yravnenieOne.replace('+',' ').replace('-',' -').replace('x^',' .')
    yravnenieOne = yravnenieOne.replace('^',' .').replace('x',' .1 ')
    my_list = yravnenieOne.split()
    data.close() 
    return my_list        

# запись в открытый файл строки и его закрытие, возвращаем словарь многочленов строки который записали в файл
def OpenAndWriteFile(data):    
    polynomialOne = RandomPolynomial()
    data.write(StringBeautiful(polynomialOne))
    data.close() 
    return polynomialOne

#  перезаписываем в словарь, список 
def ListvSlovar(my_list: list):
    polynomialOnev1 = {}
    tochka = 0
    num = ''
    peremennay = 0
    one = 0
    count = 0
    for i in my_list:
        for j in i: 
            if j == '.':
                tochka = 1
            elif tochka == 1:
                num += str(j)      
        if count == len(my_list)-1 and tochka != 1:
            peremennay = i
            polynomialOnev1[0] = polynomialOnev1.get(0, 0) + int(peremennay)
        if tochka == 0: 
            peremennay = i
        elif tochka == 1:
            polynomialOnev1[int(num)] = polynomialOnev1.get(int(num), 0) + int(peremennay)
            num = ''
            tochka = 0
        count += 1
    return polynomialOnev1

polynomialOne = OpenAndWriteFile(open(r'C:\Users\Acer\Desktop\python_dopolnitelnoe_zadanie\polynomialOne.txt', 'w'))
polynomialTwo = OpenAndWriteFile(open(r'C:\Users\Acer\Desktop\python_dopolnitelnoe_zadanie\polynomialTwo.txt', 'w'))
# Печать словарей которые мы записали в файлы
print(f'Словарь первого многочлена \n{polynomialOne}\n')
print(f'Словарь второго многочлена \n{polynomialTwo}\n')
my_list = ReplacePolynomial(open(r'C:\Users\Acer\Desktop\python_dopolnitelnoe_zadanie\polynomialOne.txt', 'r'))
my_listTwo = ReplacePolynomial(open(r'C:\Users\Acer\Desktop\python_dopolnitelnoe_zadanie\polynomialTwo.txt', 'r'))
polynomialOnev2 = ListvSlovar(my_list)
polynomialTwov2 = ListvSlovar(my_listTwo)
# Печать словарей которые мы вытащили из файла
print(f'Словарь первого многочлена из файла \n{polynomialOnev2}\n')
print(f'Словарь второго многочлена из файла \n{polynomialTwov2}\n')

polynomialThree = {}
polynomialThree.update(polynomialOnev2)
polynomialThree.update(polynomialTwov2)
for step in polynomialThree:
    polynomialThree[step] = polynomialOnev2.get(step, 0) + polynomialTwov2.get(step, 0)

print(f'Словарь сложения многочленов\n{polynomialThree}\n')
print(f'Запись сложения многочленов\n{StringBeautiful(polynomialThree)}')
data = open(r'C:\Users\Acer\Desktop\python_dopolnitelnoe_zadanie\polynomialThree.txt', 'w')
data.write(StringBeautiful(polynomialThree))
data.close() 
