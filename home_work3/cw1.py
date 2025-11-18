'''
a=[0,1,2,3]
x for x in iter
s=[x**2 for x in range()]
1. генераторы выражения
    s=(x**2 for x in range())
2.генераторы коллекций
    [] - list

Ветвление (условия)
    s=[x**3 if x<0 else x**2 -- х
        for x in a -- итер
        if x%2==0 ---фильтр]
'''
'''
    двумерный список
    1. собирать предметы
        append / extend
    2. выбрасывать предметы
        remove / pop
    3. сортировать инвентарь
        sort / reverse  *lambda
    4. поиск ключевых элементов
        index / in / not in
    5. копировать и модифицировать списки
        copy / slicing
    6. list comp
    7. rooms
        пустая / сундук / монстр / ключ / портал / ловушка 
    8. команды
        clear()
        print()
        random()

'''
import random 
import os
life=9
i=0
print ("0 - пусто / $ - сундук / @ - монстр / ! - ключ / ( ) - портал / # - ловушка")
if i==0:
    print ("ИНВЕНТАРЬ --- ПУСТО :(")
print ("ЖИЗНИ -- ", life)
print ( "ВЫБЕРИТЕ РАЗМЕР ЛАБИРИНТА")
n= int(input())
X=[' 0 ',' $ ',' @ ','( )',' # ']
x=0
y=0

P0=[[' * ' for x in range(n)] for x in range (n)]
P0[x][y]=' Я '

def cl():
    os.system('cls' if os.name == 'nt' else 'clear')
    print ("0 - пусто / $ - сундук / @ - монстр / ! - ключ / ( ) - портал / # - ловушка")
    if i==0:
        print ("ИНВЕНТАРЬ --- ПУСТО :(")
    if i==1:
        print ("ИНВЕНТАРЬ --- КЛЮЧ")
    print ("ЖИЗНИ -- ", life)

def p0():
    print(*P0 , sep ="\n")

def key():
    s1=random.choice([x for x in range (n)])
    s2=random.choice([x for x in range (n)])
    return [s1,s2]

P=[[random.choice(X) for x in range (n)] for x in range (n)]
c=1;
while c>0:
    a=key()[0]
    b=key()[1]
    if (a!=0 and b!=0):
        P[a][b]=' ! '
        c=c-1

c=1;
while c>0:
    a=key()[0]
    b=key()[1]
    if P[a][b]!=' ! ' and (a+b!=0):
        P[a][b]='( )'
        c=c-1
P[0][0]=' 0 '


def p():
    print(*P , sep ="\n")

def vn(x,y):
    P0[x][y]=P[x][y]
    x=x+1
    y=y
    if x>=n: 
        x=x-1
        P0[x][y]='Я'
        cl()
        p0()
        print("СТЕНА :( ПОПРОБУЙ ПОЙТИ В ДРУГУЮ СТОРОНУ")
        return x
    else:
        P0[x][y]=' Я '
        cl()
        p0()
        return x
def vv(x,y):
    P0[x][y]=P[x][y]
    x=x-1
    y=y
    if x<0: 
        x=x+1
        P0[x][y]='Я'
        cl()
        p0()
        print("СТЕНА :( ПОПРОБУЙ ПОЙТИ В ДРУГУЮ СТОРОНУ")
        return x
    else:
        P0[x][y]=' Я '
        cl()
        p0()
        return x
def vp(x,y):
    P0[x][y]=P[x][y]
    x=x
    y=y+1
    if y>=n: 
        y=y-1
        P0[x][y]=' Я ' 
        cl()
        p0()
        print("СТЕНА :( ПОПРОБУЙ ПОЙТИ В ДРУГУЮ СТОРОНУ")
        return y
    else:
        P0[x][y]=' Я '
        cl()
        p0()
        return y
def vl(x,y):
    P0[x][y]=P[x][y]
    x=x
    y=y-1
    if x<0: 
        y=y+1
        P0[x][y]='Я'
        cl()
        p0()
        print("СТЕНА :( ПОПРОБУЙ ПОЙТИ В ДРУГУЮ СТОРОНУ")
        return y
    else:
        P0[x][y]=' Я '
        cl()
        p0()
        return y

cl()
p0()

while life>0:
    s=input()
    if (s=='s'): 
        vn(x,y)
        x=vn(x,y)
        y=y  
    if (s=='w'): 
        vv(x,y)
        x=vv(x,y)
        y=y
    if (s=='d'): 
        vp(x,y)
        x=x
        y=vp(x,y)
    if (s=='a'): 
        vl(x,y)
        x=x
        y=vl(x,y)
    if P[x][y]==' @ ': 
        print('МОНСТР!!!!! МИНУС 3 ЖИЗНИ')
        life=life-3
    if P[x][y]==' 0 ':
        print('ТУТ НИЧЕГО')
    if P[x][y]==' # ': 
        print('ЛОВУШКА!!!!! МИНУС 1 ЖИЗНЬ')
        life=life-1
    if P[x][y]==' $ ': 
        print('УРАА СУНДУК!!! ПЛЮС 1 ЖИЗНЬ')
        life=life+1
        P[x][y]=' 0 '
    if P[x][y]==' ! ': 
        print('УРАА КЛЮЧ!!! ТЕПЕРЬ У ТЕБЯ ЕСТЬ КЛЮЧ')
        i=i+1
        P[x][y]=' 0 '
    if P[x][y]=='( )': 
        if i==0:
            print('ПОРТАЛ. ЧЕГО-ТО НЕ ХВАТАЕТ')
        else:
            break

        
if life <=0: 
    cl()
    print('ТЫ НАВСЕГДА ОСТАЛСЯ В ЛАБИРИНТЕ')
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    print ("УРА ТЫ ВЫБРАЛСЯ ИЗ ЛАБИРИНТА")

    


