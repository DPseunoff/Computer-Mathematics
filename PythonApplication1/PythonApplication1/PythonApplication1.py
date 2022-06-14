# Лаба 1
# [-5,-1,3,-2,5],             -1             ответ 6
# [-3,-2,0,-2,1],             1.3            ответ −14.562
# [-0.9,2.1,3.7,-2.4,0.8],     3             ответ 10.7
# Лаба 2
# [3,1,-8,0,8,7,6],                     -2      ответ [3,−5,2,−4,16,−25]
# [8,-7,28,-5,-40,10,-3,-28,-17,-9],     1      ответ [8,1,29,24,−16,−6,−9,−37,−54]
# [1,-1,-6,4,8],                         2      ответ [1,1,−4,−4]
# Лаба 3
# [1,-8,5,2,-7],               2               ответ [1,0,−19,−42,−31]
# [1,-3,-12,52,-48],           3               ответ [1,9,15,7,0]
# [1,13,57,83,-34,-120,0],    -1               ответ [1,7,7,−35,−56,28,48]
# Лаба 4
# [1,0,-12,-16,0]               ответ  -4  4
# [2,-13,1,103,-183,90]         ответ  -3  7
# [-2,-13,-13,28]               ответ  -7  1
# [0,0,5,-16,-45,0]             ответ  -2  5
# Лаба 5
# [1,-7,7,15,0,0,0]             ответ  5, 3, -1, 0, 0, 0
# [4,0,-95,75,226,-120]         ответ  -5, 4, -1.5, 2, 0.5
# [1,3,-14,-30,49,27,-36]       ответ  -4, -3, 3, -1, 1, 1

#Ввод полинома
def PolinomInput():
    print("Введите коэффициенты полинома: ")
    PolIn = list(map(float, input().split(',')))
    size = len(PolIn) - 1
    i = 0
    while PolIn[i] == 0: 
        size = size - 1
        i = i + 1
    print("Степень многочлена:", size)
    return PolIn


#Схема Горнера
def Scheme(polinom, a):
    output = [polinom[0]]
    for i in range(len(polinom) - 1):
        output.append(a * output[i] + polinom[i + 1])
    return output

#Вычисления лабы 1
def Lab_1(polinom, a):
    polinom = Scheme(polinom, a)
    return round(polinom[len(polinom) - 1], 3)

#Вычисления лабы 2
def Lab_2(polinom, a):
    polinom = Scheme(polinom, a)
    polinom.pop(len(polinom) - 1)
    return polinom

#Вычисления лабы 3
def Lab_3(polinom, a):
    polinom_out = []
    for j in range(len(polinom)):
        temp = Scheme(polinom, a)
        polinom_out.append(temp[-1])
        polinom = temp[0:len(temp) - 1]
    polinom_out.reverse()
    return polinom_out

#Вычисления лабы 4
def Lab_4(polinom):
    answer = [0, 0]
    #нахождение верхней границы
    if polinom[0] < 0: polinom = [i * -1 for i in polinom]
    for i in range(1000000):
        temp = Scheme(polinom, i)
        f = True
        for j in temp:
            if j < 0:
                f = False
                break
        if f == True:
            answer[1] = i
            break
    #нахождение нижней границы
    polinom = [i * (-1) ** (len(polinom) - 1) for i in polinom]
    for i in range(len(polinom)):
        polinom[i] = polinom[i] * (-1) ** (len(polinom) - i - 1)
    for i in range(1000000):
        temp = Scheme(polinom, i)
        f = True
        for j in temp:
            if j < 0:
                f = False
                break
        if f == True:
            answer[0] = -1 * i
            break

    return answer


#Проверка на наличие корней и нахождение нужного интервала
def CheckRoots(polinom, b):
    result = [0,0,0]
    result[1] = b[1]
    up = Lab_1(polinom, b[1])
    tmp2 = b[0]
    while tmp2 < b[1]:
        if (Lab_1(polinom, tmp2) * up > 0):
            tmp2 = tmp2 + 0.0001
        else:
            result[0] = tmp2
            result[2] = 1
            break
    return result

#Вычисления лабы 5
def Lab_5(polinom):
    result = []
    bs = Lab_4(polinom)
    int = CheckRoots(polinom, bs)
    while int[2] == 1:
        a = bs[0]
        b = bs[1]
        c = a
        eps = 0.00000001
        if abs(a) == abs(b):
            c = a
        if Lab_1(polinom, 0) == 0:
            result.append(0)
            polinom = Lab_2(polinom, 0)
            int = CheckRoots(polinom, bs)
            continue
        if Lab_1(polinom, int[0]) == 0:
            result.append(int[0])
            polinom = Lab_2(polinom, int[0])
            int = CheckRoots(polinom, bs)
            continue
        if Lab_1(polinom, int[1]) == 0:
            result.append(int[1])
            polinom = Lab_2(polinom, int[1])
            int = CheckRoots(polinom, bs)
            continue
        if int[2] != 1:
            break
    #метод дихотомии
        while abs(b - a) >= eps:
            c = (a + b) / 2
            if Lab_1(polinom, c) == 0:
                break
            elif (Lab_1(polinom, a) * Lab_1(polinom, c)) < 0:
                b = c
            else:
                a = c
        result.append(c)
        polinom = Lab_2(polinom, c)
        int = CheckRoots(polinom, bs)
    return result

#Вывод полинома
def PolinomOutput(polinom):
    s = ""
    for i in range(len(polinom)):

        if len(polinom)-1-i == 1:
            if polinom[i] == 1:
                s += " + " + "x"
            if polinom[i] == -1:
                s += " - " + "x"
            if polinom[i] < 0 and polinom[i] != -1:
                s += " - " + str(-1*polinom[i])+ "x"
            elif polinom[i] > 0 and polinom[i] != 1:
                s += " + " + str(polinom[i]) + "x"
            else: continue

        elif len(polinom)-1-i == 0:
            if polinom[i] < 0:
                s += " - " + str(-1*polinom[i])
            elif polinom[i] > 0:
                s += " + " + str(polinom[i])
            else: continue

        else:
            if polinom[i] == 1:
                s += " + " + "x" + degree(len(polinom)-1-i)
            if polinom[i] == -1:
                s += " - " + "x" + degree(len(polinom)-1-i)
            if polinom[i] < 0 and polinom[i] != -1:
                s += " - " + str(-1*polinom[i]) + "x" + degree(len(polinom)-1-i)
            elif polinom[i] > 0 and polinom[i] != 1:
                s += " + " + str(polinom[i]) + "x" + degree(len(polinom)-1-i)
            else: continue
    if s[1] == '+':
        print(s[3:])
    else: print(s[1:])

#Работа со степенями
indexes = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079",
           }
def degree(a: int):
    degrees = ""
    s = str(a)
    for char in s:
        degrees += indexes[char] or ""
    return degrees


#Запуск лабы 1
def Laba1():
    polinom = PolinomInput()
    print("Введенный полином: ", end='')
    PolinomOutput(polinom)
    a = float(input("Введите a: "))
    ans = Lab_1(polinom, a)
    print("Ответ:", ans)

#Запуск лабы 2
def Laba2():
    polinom = PolinomInput()
    print("Введенный полином: ", end='')
    PolinomOutput(polinom)
    a = float(input("Введите a: "))
    ans = Lab_2(polinom, a)
    print("Ответ: ", end='')
    PolinomOutput(ans)

#Запуск лабы 3
def Laba3():
    polinom = PolinomInput()
    print("Введенный полином: ", end='')
    PolinomOutput(polinom)
    a = float(input("Введите a: "))
    ans = Lab_3(polinom, a)
    print("Ответ: ", end='')
    PolinomOutput(ans)

#Запуск лабы 4
def Laba4():
    polinom = PolinomInput()
    print("Введенный полином: ", end='')
    PolinomOutput(polinom)
    answer = Lab_4(polinom)
    print("Вверхняя граница:", answer[1])
    print("Нижняя граница:", answer[0])

#Запуск лабы 5
def Laba5():
    polinom = PolinomInput()
    print("Введенный полином: ", end='')
    PolinomOutput(polinom)
    print("Корни: ")
    ans = Lab_5(polinom)
    if len(ans) == 0: print("Нет действительных корней")
    else:
        for i in ans:
            print(round(i,2))

#Мейн
while True:
    print("\nВведите номер задания:")
    a = input()
    if a == '1': Laba1()
    elif a == '2': Laba2()
    elif a == '3': Laba3()
    elif a == '4': Laba4()
    elif a == '5': Laba5()
    elif a == '0': break
    else: print("Неправильный номер.")
