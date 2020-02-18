#! Python
import sys, pyperclip
todas = {'hotmail': "10", 'gmail1': '11', 'gmail2': '12' }

conta = input('Insira a conta: ')

if conta in todas:
    pyperclip.copy(todas[conta])
    print('Senha copiada')