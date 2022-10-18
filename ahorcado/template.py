from dataclasses import replace
import os
from curses.ascii import isalpha
from sklearn.utils import assert_all_finite
from ahorcado import read
from ahorcado import  AHORCADO


#Check what operative systtem is installed.
def clear(): 
    if os.name =='posix':
        os.system("clear")
    elif os.name ==("ce", "nt", "dos"):
        os.system("cls")

#Remove the accents of a string
def normalize():
    replacements = [
        ('á', 'a'),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ñ", "n"),
        ('"', "")
    ]

#Para imprimir el mono por cada fallo


secret_word = read()
secret_word = secret_word.upper()
secret_word_letter = [letter for letter in secret_word]


template = ['_ ' for i in range(len(secret_word_letter))]
word_dic = {i: secret_word_letter[i].upper() for i in range (len(secret_word_letter))}

lifes = 1
intentos_fallidos = set()

while lifes<=7:
    clear()  
    print("Adivina la siguiente palabra:  ", end='')
    print(*template, '\n')
    print(AHORCADO[len(intentos_fallidos)])
    print(intentos_fallidos)
    print(f"Tienes {8 - lifes} vidas. No las desperdicies!!!! ")

    if  '_ ' not in template:
            clear()
            print('La palabra es: ', *template)
            print(AHORCADO[len(intentos_fallidos)])
            print('G    A   N   A   S   T   E')            
            intentos_fallidos.clear()
            break 

            
    caracter = input('ingresa una letra: ').strip().upper()

    assert len(caracter) == 1, 'Ingresa un solo dígito a la vez.'
    if caracter.isalpha():         
        for i in range (len(secret_word_letter)):
            if word_dic[i] == caracter:
                template[i] = caracter
        if caracter not in  secret_word_letter:
            
            if caracter not in intentos_fallidos:
                intentos_fallidos.update(caracter)
                lifes += 1           
                
    else:
        print('Ingresa una letra, no números.') 
else:
    clear()    
    print("\n Has perdido, la palabra era: ", secret_word)
    print(AHORCADO[len(intentos_fallidos)])

