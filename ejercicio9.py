import os

MESSAGES = {
        'MSG_LIN':'---===----=-- [   ]   --=----===---',
        'MSG_INPUT': 'Ingrese una cantidad: ',
        'MSG_ERROR_INPUT': 'Indique un valor numerico'
        }

def clear():
    os.system('cls')

def listaCuadrado():
    clear()
    lista = []
    cuadrado = []

    while True:
        cantidad = input(f'{MESSAGES['MSG_LIN']}\n{MESSAGES['MSG_INPUT']}')

        try:
            clear()
            num = int(cantidad)

            for x in range(1, num):
                lista.append(x)
                cuadrado.append(x ** 2)

            print(f'{MESSAGES['MSG_LIN']}\nLISTA: {lista}\nLISTA CUADRADO: {cuadrado}')
            break
        except:
            print(f'{MESSAGES['MSG_ERROR_INPUT']}')

listaCuadrado()