l=int(input("выберите уровень(1-5): "))
s = str(input("Введите строку: "))
def l_1(s: str):
    command=int(input("Выберите команду(1-делает все буквы строчными; 2- делает все буквы заглавными; 3- делает первую букву заглавной): "))
    if command==1: return s.lower()
    if command ==2: return s.upper()
    if command==3: return s.capitalize()
def l_2(s: str):
    command=int(input("Выберите команду(1-находит индекс первого необходимого символа в строке;2-заменяет что-то одно в строке на другое;3-считает сколько раз что-то встречается в строке): "))
    if command==1:
        nz=str(input("Напишите символ, индекс которого вы хотите найти: "))
        return s.find(nz)
    elif command==2:
        z=str(input("Что вы хотите заменить: "))
        hz=str(input("На что вы хотите заменить: "))
        return s.replace(z,hz)
    elif command==3:
        num=str(input("Что вы хотите посчитать: "))
        return s.count(num)
def l_3(s: str):
    command=int(input("Выберите команду:1-вставляет данный вами символ между всеми символами строки; 2- делить вашу строку на несколько относительно данных вами символами): "))
    if command==1:
        sim=str(input("Ведите символ, который необходимо вставить: "))
        return sim.join(s)
    if command ==2:
        raz=str(input("Введите символ по которому будем делить строку: "))
        return s.split(raz)
def l_4(s:str):
    command=int(input("Выберите команду:1-определяет все ли символы числа; 2-определяет все ли символы буквы; 3- удаляет символ, который вы выбираете;4-меняет формат строки): "))
    if command==1:
        if s.isdigit():return "Да"
        return "Нет"
    if command==2:
        if s.isalpha(): return "Да"
        return "Нет"
    if command==3:
        sim=str(input("Введите символ, который надо убрать: "))
        return s.strip(sim)
    if command==4:
        return s.format()
if l==1:
    print(l_1(s))
elif l==2:
    print(l_2(s))
elif l==3:
    print(l_3(s))
elif l==4:
    print(l_4(s))