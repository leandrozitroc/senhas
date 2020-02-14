#! Python
import sys, pyperclip
todas = {'hotmail': "brasil61241010", 'gmail1': 'brasil61241010', 'gmail2': 'brasil61241010' }

conta = input('Insira a conta: ')

if conta in todas:
    pyperclip.copy(todas[conta])
    print('Senha copiada')