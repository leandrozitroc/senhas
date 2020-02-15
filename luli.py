from cryptography.fernet import Fernet
from password_generator import PasswordGenerator
import pyperclip


def write_key():
    key = Fernet.generate_key()
    with open("key.key", 'wb') as key_file:
        key_file.write(key)
write_key()


def cript_arquivo(filename, key):
    f = Fernet(key)
    try:
        with open(filename, 'rb') as file:
            file_data = file.read()
            data_encripitada = f.encrypt(file_data)
    except:
            print('\33[1;31m Arquivo Inexistente!\33[m')
    else:
        with open(filename, 'wb') as file:
            file.write(data_encripitada)
            print('\33[1;32m Arquivo encriptado com sucesso!\33[m')

def decript_arquivo(filename , key):
    f = Fernet(key)
    try:
        with open(filename, 'rb') as file:
            file_data = file.read()
            data_decripitada = f.decrypt(file_data)
    except:
        print('\33[1;31m Arquivo Inexistente!\33[m')

    else:
        with open(filename, 'wb') as file:
            file.write(data_decripitada)
            print('\33[1;32m Arquivo decriptado com sucesso!\33[m')

def gerarsenha():
    pwo= PasswordGenerator()
    pwo.minlen = 8
    pwo.maxlen = 12

    pw = pwo.generate()
    print(f'\33[1;35m A senha segura que o sistema gerou foi:\33[m \33[1;33m{pw} \33[m')
    colar = input('\33[1;34m Deseja mandar a senha gerada a área de transferencia? S ou N :\33[m').lower()
    if colar == 'n':
        print('Ok')
    elif colar == 's':
        pyperclip.copy(pw)
        print('\33[1;32m Senha copiada com sucesso!\33[m')
    else:
        print('\33[1;31m Digita S para sim e N para não\33[m')


def encript_senha(pwd , key):
    f = Fernet(key)
    senha_cript = f.encrypt(pwd.encode())
    print(senha_cript.decode())
    colar = input('\33[1;34m Deseja mandar a senha encriptada para a área de transferencia? S ou N :\33[m').lower()
    if colar == 'n':
        print('Ok')
    elif colar == 's':
        pyperclip.copy(senha_cript.decode())
        print('\33[1;32m Senha copiada com sucesso!\33[m')
    else:
        print('\33[1;31m Digita S para sim e N para não\33[m')

def decript_senha(pwd, key):
    f = Fernet(key)
    senha_decript = f.decrypt(pwd.encode())
    print(senha_decript.decode())
    colar = input('\33[1;34m Deseja mandar a senha decriptada para área de transferencia? S ou N :\33[m').lower()
    if colar == 'n':
        print('Ok')
    elif colar == 's':
        pyperclip.copy(senha_decript.decode())
        print('\33[1;32m Senha copiada com sucesso!\33[m')
    else:
        print('\33[1;31m Digita S para sim e N para não\33[m')
