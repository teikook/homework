# Интерпретатор языка COW.

import numpy as np
import re


file = open('hello.cow', 'r')
res = file.read()
r = re.sub(r'\n', r' ', res)
r = r.split(' ')

stack=[]
d = {}
ind = 0
result = np.zeros(1000)


for item in r:
    if item == 'MOO': #конец цикла 
        stack.append(ind)
    if item == 'moo': #начало цикла 
        d[ind]=stack[len(stack)-1]
        d[stack.pop()]=ind
    ind+=1
index = 0
i = 0


while(i!= len(r)):
    if r[i] == 'MoO': #значение текущей ячейки увеличить на 1 
        result[index] += 1
    if r[i] == 'MOo': #значение ​текущей ячейки уменьшить на 1
        result[index] -= 1
    if r[i] == 'moO':
        index += 1 #следующая ячейка
    if r[i] == 'mOo':
        index -= 1 # предыдущая ячейка
    if r[i] == 'OOM': # вывод значения текущей ячейки
        print(chr(int(result[index])))
    if r[i] == 'Moo': #если значение в ячейке равно 0, то ввести с клавиатуры, если значение не 0,
                       #то вывести на экран
        if r[index] != 0:
            print(chr(int(result[index])))
    if r[i] == 'OOO': #обнулить значение в ячейке
        r[index] = 0
    if r[i] == 'moo': 
        i = d[i]-1
    if r[i] == 'MOO':
        if result[index] == 0:
            i = d[i]
    if r[i] == '':
        pass
    else:
        i += 1
        continue
    i += 1
