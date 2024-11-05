# Imports
import os

# Strings
def Messages(message, value=0):
        if (message == 'message_error'):
             message = 'No es un valor numerico'

        if (message == 'message_lin'):
               message = '========================='
        
        if (message == 'message_input'):
               message = 'Ingrese un valor numerico: '
        
        if (message == 'message_par'):
               message = (f'Numero Ingresado: {value}\nResultado: Par')
        
        if (message == 'message_impar'):
               message = (f'Numero Ingresado: {value}\nResultado: Impar')
        
        return message

def clear():
       os.system('cls')

def comparador():
      clear()
      while True:

        try:
            valueInput = int(input(f'{Messages('message_lin')}\n{Messages('message_input')}'))

            if (valueInput % 2 == 0):
                  clear()
                  print(f'{Messages('message_lin')}\n{Messages('message_par', valueInput)}')
            else:
                  clear()
                  print(f'{Messages('message_lin')}\n{Messages('message_impar', valueInput)}')

            print(Messages('message_lin'))
            break
        except:
              clear()
              print(f'{Messages('message_lin')}\n{Messages('message_error')}')
    

comparador()
