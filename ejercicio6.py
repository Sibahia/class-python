import os
import math

MESSAGES = {
        'MSG_LIN':'---===----=-- [   ]   --=----===---',
        'MSG_INPUT_CANT': 'Ingrese la cantidad de valores de la lista: ',
        'MSG_INPUT_NUMS': 'Ingrese el numero: ',
        'MSG_INPUT_TARGET': 'Ingrese el numero a seleccionar: ',
        'MSG_ERROR_MENU': 'La opcion no existe en la lista',
        'MSG_ERROR_MENU_NUMS': 'Indique la opcion de manera numerica',
        'MSG_ERROR_INPUT_NUMS': 'Indique el valor de manera numerica',
        'MSG_MENU': '1) Introducir el primer vector\n2) Introducir el segundo vector\n3) Calcular la suma\n4) Calcular la diferencia\n5) Calcular el producto escalar\n6) Calcular el producto vectorial\n7) Calcular el angulo (en grados) entre ellos\n8) Calcular la longitud\n9) Finalizar',
        'MSG_MENU_INPUT': 'Seleccione una opcion del menu: ',
        'MSG_MENU_INPUT_VECTOR': 'Selecione el vector: '
    }

def clear():
    os.system('cls')

def vector(vector=None):
    clear()
    vector1 = []
    while True:
        if (len(vector1) == 3):
            break

        label_vector1 = input(f'{MESSAGES['MSG_LIN']}\n{MESSAGES['MSG_INPUT_NUMS']}')
        try:
            label_int = int(label_vector1)
            clear()

            vector1.append(label_int)
            print(f'{MESSAGES['MSG_LIN']}\nCALCULADORA\nOPCION: Introducir Vector - ({len(vector1)}/3)\n{MESSAGES['MSG_LIN']}\nLISTA: {vector1}\n')

        except:
            print(f'{MESSAGES['MSG_ERROR_INPUT_NUMS']}')

    return vector1

def sumaVector(vector1, vector2):
    clear()
    suma = []

    for x in range(3):
        suma.append(vector1[x] + vector2[x])

    while True:
        clear()
        print(f'{MESSAGES['MSG_LIN']}\nCALCULADORA\nOPCION: Sumar Vectores\nVECTORES: {vector1} {vector2}\nRESULTADO: {suma}\n{MESSAGES['MSG_LIN']}\nPulse ENTER para salir')

        getOut = input()
        if not getOut:
            break

def diferVector(vector1, vector2):
    clear()
    resta = []

    for x in range(3):
        resta.append(vector1[x] - vector2[x])

    while True:
        clear()
        print(f'{MESSAGES['MSG_LIN']}\nCALCULADORA\nOPCION: Diferencia de Vectores\nVECTORES: {vector1} {vector2}\nRESULTADO: {resta}\n{MESSAGES['MSG_LIN']}\nPulse ENTER para salir')

        getOut = input()
        if not getOut:
            break
    
def escalVector2(vector1, vector2):
    mult = []
    escal = 0

    for x in range(3):
        mult.append(vector1[x] * vector2[x])

    for y in mult:
        escal += y

    return escal

def escalVector(vector1, vector2):
    clear()
    mult = []
    escal = 0

    for x in range(3):
        mult.append(vector1[x] * vector2[x])

    for y in mult:
        escal += y

    while True:
        clear()
        print(f'{MESSAGES['MSG_LIN']}\nCALCULADORA\nOPCION: Escalar de Vectores\nVECTORES: {vector1} {vector2}\nRESULTADO: {escal}\n{MESSAGES['MSG_LIN']}\nPulse ENTER para salir')

        getOut = input()
        if not getOut:
            break

def vecVector(vector1, vector2):
    producto = [
        vector1[1] * vector2[2] - vector1[2] * vector2[1],
        vector1[2] * vector2[0] - vector1[0] * vector2[2],
        vector1[0] * vector2[1] - vector1[1] * vector2[0]
    ]

    while True:
        clear()
        print(f'{MESSAGES['MSG_LIN']}\nCALCULADORA\nOPCION: Vectorial de Vectores\nVECTORES: {vector1} {vector2}\nRESULTADO: {producto}\n{MESSAGES['MSG_LIN']}\nPulse ENTER para salir')

        getOut = input()
        if not getOut:
            break

def angVector(vector1, vector2):
    escal = escalVector2(vector1, vector2)

    magVector1 = math.sqrt(sum(vector1[i] ** 2 for i in range(3)))
    magVector2= math.sqrt(sum(vector2[i] ** 2 for i in range(3)))
    
    cos = escal / (magVector1 * magVector2)

    rad = math.acos(cos)
    grad = math.degrees(rad)

    while True:
        clear()
        print(f'{MESSAGES['MSG_LIN']}\nCALCULADORA\nOPCION: Angulo Vectores\nVECTORES: {vector1} {vector2}\nRESULTADO: {grad}\n{MESSAGES['MSG_LIN']}\nPulse ENTER para salir')

        getOut = input()
        if not getOut:
            break

def longVector(vector1, vector2):
    while True:
        clear()
        getLong = input(f'{MESSAGES['MSG_LIN']}\nCALCULADORA\nOPCION: Longitud de Vector\n{MESSAGES['MSG_LIN']}\nLISTA: {vector1} {vector2}\n{MESSAGES['MSG_LIN']}\nSelecione una lista: ')

        if not getLong:
            break

        try:
            getLongNums = int(getLong)

            if getLong in "12":
                if (getLong == '1'):
                    long = math.sqrt(sum(vector1[x] ** 2 for x in range(3)))
                    while True:
                        clear()
                        print(f'{MESSAGES['MSG_LIN']}\nCALCULADORA\nOPCION: Longitud Vector 1\nVECTORES: {vector1}\nRESULTADO: {long}\n{MESSAGES['MSG_LIN']}\nPulse ENTER para salir')

                        getOut = input()
                        if not getOut:
                            break

                if (getLong == '2'):
                    long = math.sqrt(sum(vector2[x] ** 2 for x in range(3)))
                    while True:
                        clear()
                        print(f'{MESSAGES['MSG_LIN']}\nCALCULADORA\nOPCION: Longitud Vector 2\nVECTORES: {vector2}\nRESULTADO: {long}\n{MESSAGES['MSG_LIN']}\nPulse ENTER para salir')

                        getOut = input()
                        if not getOut:
                            break
        except:
            print(f'{MESSAGES['MSG_LIN']}\nERROR: {MESSAGES["MSG_ERROR_MENU_NUMS"]}')

def vectorCalculador():
    clear()

    vector1 = []
    vector2 = []

    while True:
        clear()
        print(f'{MESSAGES['MSG_LIN']}\n{MESSAGES['MSG_MENU']}')

        if (len(vector1) == 3):
            print(f'{MESSAGES['MSG_LIN']}\nVector 1 - {vector1}')
        if (len(vector2) == 3):
            print(f'Vector 2 - {vector2}')

        label = input(f'{MESSAGES['MSG_LIN']}\n{MESSAGES["MSG_MENU_INPUT"]}')

        try:
            inpt = int(label)

            if label in "123456789":
                if (label == '1'):
                    clear()

                    vector1 = vector()

                if (label == '2'):
                    clear()
                    
                    vector2 = vector()

                if (label == '3'):
                    clear
                    sumaVector(vector1, vector2)
                
                if (label == '4'):
                    clear
                    diferVector(vector1, vector2)

                if (label == '5'):
                    clear
                    escalVector(vector1, vector2)
                
                if (label == '6'):
                    clear
                    vecVector(vector1, vector2)

                if (label == '7'):
                    clear()
                    angVector(vector1, vector2)
                
                if (label == '8'):
                    clear()
                    longVector(vector1, vector2)
                
                if (label == '9'):
                    break
            else:
                clear()
                print(f'{MESSAGES['MSG_LIN']}\nERROR: {MESSAGES["MSG_ERROR_MENU"]}')
        except:
            clear()
            print(f'{MESSAGES['MSG_LIN']}\nERROR: {MESSAGES["MSG_ERROR_MENU_NUMS"]}')

vectorCalculador()
# print(sumaVector([5,6,7],[2,1,3]))

# longVector([5,6,7],[2,1,3])