from copy import copy
#Ввод полинома
def PolinomInput():
    print("Введите коэффициенты полинома: ")
    PolIn = list(map(float, input().split(',')))
    size = len(PolIn) - 1
    i = 0
    if size != 0:
        while PolIn[i] == 0:
            size = size - 1
            i = i + 1
    print("Степень многочлена:", size)
    return PolIn

#Вывод полинома
def PolinomOutput(polinom):
    s = ""
    if len(polinom) == 1:
        print(polinom[0])
    elif len(polinom) < 1:
        print("0")
    else:
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
        if len(s) == 0:
            print("0")
            return
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

#Значение полинома в точке (Лаб 1, п1)
def Scheme(polinom, x):
    output = [polinom[0]]
    for i in range(len(polinom) - 1):
        output.append(x * output[i] + polinom[i + 1])
    return output
def Gorner(polinom, x):
    polinom = Scheme(polinom, x)
    return polinom[len(polinom) - 1]
def GornerFloat(polinom, x):
    polinom = Scheme(polinom, float(x))
    return polinom[len(polinom) - 1]
def Gorner_pol(polinom, x):
    polinom = Scheme(polinom, x)
    polinom.pop(len(polinom) - 1)
    return polinom

#Создание float range
def FloatR(start, stop, step):
    while start > stop-0.01:
        yield float(start)
        start += step

#Производная полинома (Лаб 2, п1)
def Deriv(polinom):
    return [polinom[i] * (len(polinom)-i-1) for i in range(0, len(polinom)-1)]


#Границы корней (Лаб 1, п4)
def B_Search(polinom):
    answer = [0, 0]
    #нахождение верхней границы
    if polinom[0] < 0: polinom = [i * -1 for i in polinom]
    for i in range(1000000):
        temp = Scheme(polinom, float(i))
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

#Метод Хорд нахождения корня (Лаб 2, п2)
def FindR(polinom, a, b):
    while abs(a - b) >= 0.00001:
        h = ((-1) * (b - a) * Gorner(polinom, a)) / (Gorner(polinom, b) - Gorner(polinom, a))
        res = a + h
        if Gorner(polinom, a) * Gorner(polinom, res) < 0:
            b = res
        else:
            a = res

        if abs(Gorner(polinom, res)) < 0.001:
            break
    return round(res, 4)

#Пункт 1
def Ring(polinom):
    #Избавиться от нулевых коэффициентов полинома
    while polinom[0] == 0 and len(polinom) > 1:
        polinom = polinom[1:]
    while polinom[len(polinom) - 1] == 0 and len(polinom) > 1:
        polinom = polinom[:-1]
    #Проверка на то, что все коэффициенты были нулевые
    if len(polinom) <= 1:
        return

    res = []
    #Нахождние верхней границы
    A = -1
    for i in range(1, len(polinom)):
        if abs(polinom[i]) >= A:
            A = abs(polinom[i])
    res.append(round(1 + A / abs(polinom[0]), 5))
    #Нахождение нижней границы
    B = -1
    for i in range(len(polinom)-1):
        if abs(polinom[i]) >= B:
            B = abs(polinom[i])
    res.append(round(1 / (1 + B / abs(polinom[len(polinom)-1])), 5))

    return res

#Пункт 2
def Lagranzh(polinom):
    j = -1
    B = -1
    #Убедимся, что первый коэфф полинома неотрицательный
    if polinom[0] < 0:
        for i in range(len(polinom)-1):
            polinom[i] *= -1
    #Находим первый из отрицательных коэффициентов полинома и B 
    for i in range(len(polinom) - 1):
        if polinom[i] < 0:
            if j == -1 and i >= 1:
                j = i
            if abs(polinom[i]) > B:
                B = abs(polinom[i])
    # Теорема Лагранжа
    return round(1 + (B / polinom[0]) ** (1 / j), 4)

#Пункт 3
def Newton(polinom):
    #Убедимся, что первый коэфф полинома неотрицательный
    if polinom[0] < 0:
        for i in range(len(polinom)-1):
            polinom[i] *= -1
    k = 0
    while k < 25:
        k += 1
        #Проверяем, что Pk(с) > 0
        if Gorner(polinom, k) < 0:
            continue
        #Проверяем, что значения всех производных > 0
        polinomD = Deriv(polinom)
        f = 1
        for i in range(len(polinom) - 1):
            if Gorner(polinomD, k) < 0:
                f = 0
                break
            polinomD = Deriv(polinomD)
        #Возвращаем k
        if f == 1:
            return k

#Пункт 4
def Synthetic(polinom1, polinom2):
    res = []
    #Подготавливаем делитель к синтетическому делению
    delitel = polinom2[0]
    for i in range(len(polinom2)):
        polinom2[i] = polinom2[i] * (-1)
    polinom2.pop(0)
    #Процесс деления
    res.append(polinom1[0] / delitel)
    for i in range(1, len(polinom1) - len(polinom2)):
        add = 0
        if i < len(polinom2):
            for j in range(i):
                add += res[j] * polinom2[i - j - 1]
        else:
            for j in range(len(polinom2)):
                add += res[len(res) - j - 1] * polinom2[j]
        res.append((polinom1[i] + add) / delitel)
    for i in range(len(polinom2)):
        add = 0
        t = 1
        for j in range(i, len(polinom2)):
            if len(polinom1) - len(polinom2) - t >= 0:
                add += res[len(polinom1) - len(polinom2) - t] * polinom2[j]
            t += 1
        res.append(polinom1[len(polinom1) - len(polinom2) + i] + add)
    return [res[0:len(polinom1) - len(polinom2)], res[len(polinom1) - len(polinom2): len(res)]]

#Пункт 5
def Shturm(polinom, a, b):
    #Находим границы корней
    if a == 0.0 and b == 0.0:
        tmp = B_Search(copy(polinom))
        a = tmp[0]
        b = tmp[1]
    #Составляем систему Штурма
    s = []
    s.append(polinom)
    s.append(Deriv(polinom))
    k = 1
    while len(s[k]) > 1:
        #записываем остаток от деления полиномов
        ost = Synthetic(copy(s[k - 1]), copy(s[k]))[1]
        #избавляемся от нулей
        while ost[0] == 0 and len(ost) > 1:
            ost.pop(0)
        #умножаем на -1
        for i in range(len(ost)):
            ost[i] *= -1
        s.append(ost)
        k += 1
    #Выявляем количество перемен знаков
    N_a = 0
    N_b = 0
    N_0 = 0
    for i in range(len(s) - 1):
        c_Na1 = Gorner(copy(s[i]), a)
        c_Na2 = Gorner(copy(s[i + 1]), a)
        c_Nb1 = Gorner(copy(s[i]), b)
        c_Nb2 = Gorner(copy(s[i + 1]), b)
        c_N01 = Gorner(copy(s[i]), 0)
        c_N02 = Gorner(copy(s[i + 1]), 0)
    
        if c_Na1 * c_Na2 < 0:
            N_a += 1
        if c_Nb1 * c_Nb2 < 0:
            N_b += 1
        if c_N01 * c_N02 < 0:
            N_0 += 1
    return (N_0 - N_b) + (N_a - N_0)

#Пункт 6
def AllRoots(polinom, up, down, interval):
    roots = []
    bounds = []
    k = 0
    while (up > down):
        k = Shturm(copy(polinom), up - interval, up)
        if k == 1:
            roots.append(FindR(copy(polinom), up - interval, up))
            bounds.append([up - interval, up])
        elif k > 1:
            foundR, foundB = AllRoots(polinom, up, up - interval, interval / 2)
            for j in range(len(foundR)):
                roots.append(foundR[j])
            for j in range(len(foundB)):
                bounds.append(foundB[j])
        up -= interval
    return roots, bounds

#Запуск задания 1
def Laba1():
    polinom = PolinomInput()
    print("Введенный полином: ", end = '')
    PolinomOutput(polinom)
    ans = Ring(polinom)
    print("Верхняя граница: ", ans[0])
    print("Нижняя граница: ", ans[1])

#Запуск задания 2
def Laba2():
    polinom = PolinomInput()
    print("Введенный полином: ", end = '')
    PolinomOutput(polinom)
    frontier = Lagranzh(polinom)
    print("Верхняя граница положительных действительных корней: ", frontier)

#Запуск задания 3
def Laba3():
    polinom = PolinomInput()
    print("Введенный полином: ", end = '')
    PolinomOutput(polinom)
    frontier = Newton(polinom)
    print("Верхняя граница положительных действительных корней: ", frontier)

#Запуск задания 4
def Laba4():
    polinom1 = PolinomInput()
    polinom2 = PolinomInput()
    print("Введенные полиномы: ")
    PolinomOutput(polinom1)
    PolinomOutput(polinom2)
    ans = Synthetic(polinom1, polinom2)
    print("Их частное: ", end = '')
    PolinomOutput(ans[0])
    print("Остаток: ", end = '')
    PolinomOutput(ans[1])

#Запуск задания 5
def Laba5():
    polinom = PolinomInput()
    print("Введенный полином: ", end = '')
    PolinomOutput(polinom)
    a = 0.0
    b = 0.0
    ans = Shturm(polinom, a, b)
    print("Количество корней: ", ans)

#Запуск задания 6
def Laba6():
    polinom = PolinomInput()
    print("Введенный полином: ", end = '')
    PolinomOutput(polinom)
    bounds = B_Search(polinom)
    a = round(bounds[0])
    b = round(bounds[1])
    roots, bounds = AllRoots(polinom, b, a, 1.0)
    for i in range(len(roots)):
        print("Корень: ", roots[i], "Интервал", bounds[i])


#Мейн
while True:
    print("\nВведите номер задания:")
    a = input()
    if a == '1': Laba1()
    elif a == '2': Laba2()
    elif a == '3': Laba3()
    elif a == '4': Laba4()
    elif a == '5': Laba5()
    elif a == '6': Laba6()
    elif a == '0': break
    else: print("Неправильный номер.")
