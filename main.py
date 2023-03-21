from vstavki import *
from puzir import *
from wiborka import *
from qsort import *
array = [12, 11, 13, 5, 6]
N=5
print(insertion_sort(N,array))#вставки
print(puzir(N,array))#пузырьком
print(sel_sort(N,array))#выборка
print(shaker_sort(N,array))#Шейкерная(быстрая)

import PySimpleGUI as sg
mda=[]
layout = [
          [sg.Text("Массив")],
          [sg.Input(key='-INPUT3-')],
          [sg.Button('Пузырьком'), sg.Button('Перемешиванием'),sg.Button('Вставками'), sg.Button('Шелла'),
          [sg.Text("Отсортированный массив")],
          [sg.Input(key='-INPUT-')],          
          
          ]]

window = sg.Window('Богачук', layout)
while True:
    event, values = window.read()
    type_of_sort=int(values['-INPUT3-'])
    N=int(values['-INPUT-'])
    print(values['-INPUT-'])
    mda.append(int(values['-INPUT2-']))
 
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('Ваш массив ' + str(mda))
    if len(mda)==N:
        if type_of_sort==1:
            window['-OUTPUT2-'].update(insertion_sort(10,mda))
        if type_of_sort==2:
            window['-OUTPUT2-'].update(bubble(10,mda))
        if type_of_sort==3:
            window['-OUTPUT2-'].update(sel_sort(10,mda))
        if type_of_sort==4:
            window['-OUTPUT2-'].update(shaker_sort(10,mda))

window.close()