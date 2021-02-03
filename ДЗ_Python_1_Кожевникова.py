print("___While___")

"""1.Каждый день я пробегаю «следующую степень двойки» км.
Сколько дней пройдет, пока я в сумме пробегу 1000 км? 10000 км?"""

print("Task 1.1:")

def s1t1(x):
    sumkm = 0
    scope = 2
    i = 0
    while (sumkm < x):
        sumkm = sumkm + scope
        i = i + 1
        scope = scope * 2
    return i
print("Result task 1.1:")
print("For 1000km:", s1t1(1000), "days")
print("For 10000km:", s1t1(10000), "days")


"""3.Начав тренировки, спортсмен в первый день пробежал 10 км. Для увеличения
выносливости ему необходимо повышать норму бега через одну тренировку на 15% от
нормы предыдущей тренировки. Спортсмен тренируется каждый день. Какой
суммарный путь он пробежит за 30 дней."""

print("Task 1.3:")

def s1t3(days):
    km = 10
    sumkm = 0
    day = 1
    while day <= days:
        if day % 2 == 0:
            km *= 1.15
        sumkm += km
        day += 1
    return sumkm


print(s1t3(30), "km fot 30 days")

"""4.Начав тренировки, спортсмен в первый день пробежал 10 км. Каждый следующий день
он увеличивал дневную норму на 10% от нормы предыдущего дня. Через сколько дней:
а) спортсмен будет пробегать в день больше 20 км;
b) пробежит суммарный путь 100 км."""

print("Task 1.4a")

start=10
percent=1.1
i=0
while(start<20):
    i=i+1
    start=start*percent
print(i, "days")

print("Task 1.4a")

start=10
percent=1.1
sum=0
i=0
while(sum<100):
    sum=sum+ (start*percent)*2
    i=i+1
    start=start*percent
print(i, "days")


print ("___For___")

# Найти N-й член последовательности 1, 1, 2, 3, 5, 8, 13...

print("Task 2.1:")

def s2t1(n):
    a = 1
    b = 0
    A = 0
    for _ in range (n):
        A = a + b
        a = b
        b = A
    return A


print("Ninth term in the sequence =", s2t1(9))


# Найти N-й член последовательности 1, 1, 1, 3, 5, 9, 17…

print("Task 2.2:")

def s2t2(n):
    a = 1
    b = 1
    c = 1
    if n == 1 or n == 2 or n == 3:
        return 1
    for i in range(4, n + 1):
        n = a + b + c
        a = b
        b = c
        c = n
    return n

    return A


print("Ninth term in the sequence =", s2t2(9))


# Вывести квадраты нечетных чисел до N. (генератором списков)

print("Task 2.3:")

def s2t3(n):
    l = [i**2 for i in range(1, n + 1, 2)]
    return l

print(s2t3(17))


# Вычислить сумму и произведение всех натуральных чисел от А до В включительно.

print("Task 2.4:")

def s2t4(a,b):
    l = [i for i in range(a, b+1)]
    sum = 0
    prod = 1
    for i in l:
        sum += i
        prod *= i
    return sum, prod


print(s2t4(1, 7))


"""Даны натуральные числа А и В.
Вывести сначала все чётные числа, заключённые между ними, 
потом все нечётные (генератором/ами списков)"""

print("Task 2.5:")


def s2t5(a, b):
    if a % 2 == 0:
        even = [i for i in range(a, b+1, 2)]
        odd = [i for i in range(a+1, b, 2)]
    else:
        even = [i for i in range(a+1, b, 2)]
        odd = [i for i in range(a, b+1, 2)]
    return even, odd

print(s2t5(3, 14))


"""Исходный список содержит положительные и отрицательные числа.
Требуется положительные поместить в один список, 
а отрицательные - в другой (генератором/ами списков)"""

print("Task 2.6")

def s2t6():
    l = [11, 5, -9, 6, -13, -5, 71, 23, -4]
    positive = [i for i in l if i>0]
    negative = [i for i in l if i<0]
    return positive, negative

print(s2t6())

print("___Рисовашки___")

# Нарисовать рамочку шириной w символов и высотой h символов


print("Task 3.1:")


def s3t1(w, h):
    print(w * "*")
    for i in range(2, h):
        print("*" + (w - 2) * " " + "*")
    print(w * "*")


s3t1(10, 5)


# Пускай символ, которым рисуется рамочка – тоже входной параметр.

print("Task 3.2:")

def s3t2(w, h, s):
    print(w * s)
    for i in range(2, h):
        print(s + (w - 2) * " " + s)
    print(w * s)

s3t2(7, 6, "@")


"""Нарисовать рамочку шириной w символов и высотой h символов, 
# и толщиной f символов. (оформить в виде функции)"""

print("Task 3.3:")

def s3t3(w, h, f, s):
    for i in range(f):
        print(w * s)
    for i in range(0, h - f * 2):
        print(f * s + (w - 2 * f) * " " + f * s)
    for i in range(0, f):
        print(w * s)


s3t3(10, 7, 2, "~")


print("___По вариантам___")
#Имя Полина => вариант 3

"""Создайте программу для перевода из одной системы мер в другую
(Цельсий - Фаренгейт, мили - километры, унции - граммы и т.д.). """


def lbs_to_kg(value):
    res = round(value * 0.453, 1)
    print(value, 'lbs is', res, ' kg')


def oz_to_grams(value):
    res = round(value * 28.35, 1)
    print(value, 'oz is ', res, 'g')


def celsius_to_fahrenheit(value):
    res = round(value * (9 / 5) + 32, 1)
    print(value, '°C is ', res, '°F')


def celsius_to_kelvin(value):
    res = value + 273
    print(value, '°C is', res, 'K')


def meters_to_yards(value):
    res = round(value * 1.09, 1)
    print(value, 'm is', res, 'yd')


def km_to_miles(value):
    res = round(value * 0.62, 1)
    print(value, 'km is', res, 'mi')


def centimeters_to_inches(value):
    res = round(value * 0.393, 1)
    print(value, 'cm is', res, 'in')


def converter(i, value):
    dict = {1: lbs_to_kg, 2: oz_to_grams, 3: celsius_to_fahrenheit, 4: celsius_to_kelvin, 5: meters_to_yards,
            6: km_to_miles, 7: centimeters_to_inches}
    return dict[i](value)


choice = int(input('Press 1 to convert lbs to kilograms\n'
                   'Press 2 to convert ounces to grams\n'
                   'Press 3 to convert Celsius to Fahrenheit\n'
                   'Press 4 to convert Celsius to Kelvin\n'
                   'Press 5 to convert meters to yards\n'
                   'Press 6 to convert kilometers to miles\n'
                   'Press 7 to convert centimeters to inches\n'))
value = int(input('Enter the value to convert\n'))
try:
    converter(choice, value)
except KeyError:
    print('Please enter a number from 1 to 7 before entering the value to convert')

