import os

MESSAGES = {
        'MSG_LIN':'---===----=-- [   ]   --=----===---',
        'MSG_BIS': 'RESULTADO: BISIESTO',
        'MSG_NONBIS': 'RESULTADO: NO ES BISIESTO'
        }

def clear():
    os.system('cls')

def ageType(age):
    
    if (int(age)):

        if((age % 4 == 0 or age % 400 == 0) and (age % 100 == 0)):
            print(f'{MESSAGES['MSG_LIN']}\nAÑO: {age}\nDIAS: 366\n{MESSAGES['MSG_BIS']}')

        elif ((age % 4 == 0 or age % 400 == 0) and not (age % 100 == 0)):
            print(f'{MESSAGES['MSG_LIN']}\nAÑO: {age}\nDIAS: 366\n{MESSAGES['MSG_BIS']}')      
        else:
            print(f'{MESSAGES['MSG_LIN']}\nAÑO: {age}\nDIAS: 365\n{MESSAGES['MSG_NONBIS']}')

ageType(2023)
