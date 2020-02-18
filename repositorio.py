#! Python
import sys, pyperclip
from senhas.luli import decript_senha

def repositorio():
    print('==='* 18)
    print('==='* 18)
    print('\33[1;34mBem vindo ao Repositorio de senhas\33[m'.center(20 *3))
    print('==='* 18)
    print('==='* 18)
    todas = {'hotmail': "gAAAAABeS-fw8uY9Ebbr8vHOSEP5LJZr4AU4otO-aZ_S_qn0TfKGLNO5AoFe41KE1L2oLYkFtzKPTUTHtixKIIBlC6oYIz-NGQ==",
             'gmail1': 'gAAAAABeS-fw8uY9Ebbr8vHOSEP5LJZr4AU4otO-aZ_S_qn0TfKGLNO5AoFe41KE1L2oLYkFtzKPTUTHtixKIIBlC6oYIz-NGQ==',
             'gmail2': 'gAAAAABeS-fw8uY9Ebbr8vHOSEP5LJZr4AU4otO-aZ_S_qn0TfKGLNO5AoFe41KE1L2oLYkFtzKPTUTHtixKIIBlC6oYIz-NGQ==' }

    print(f'As contas disponiveis neste repositório de senha são: ')
    print('==='* 18)

    for i,  key  in enumerate(todas.keys()):
        print(f'{i:<3} {key:<9} ')
    print('===' * 18)
    conta = input('Insira o nome da conta: ')

    if conta in todas:
        decript_senha(todas[conta], 'ccLmrWCJu7vpwaroDuSEjv6amtpLyiY9MI-PS-oWy_4=')

