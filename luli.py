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
            print('Arquivo Inexistente!')
    else:
        with open(filename, 'wb') as file:
            file.write(data_encripitada)


def decript_arquivo(filename , key):
    f= Fernet(key)
    try:
        with open(filename, 'rb') as file:
            file_data = file.read()
            data_decripitada = f.decrypt(file_data)
    except:
        print('Arquivo Inexistente!')

    else:
        with open(filename, 'wb') as file:
            file.write(data_decripitada)

def gerarsenha():
    pwo= PasswordGenerator()
    pwo.minlen =8
    pwo.maxlen = 12

    pw = pwo.generate()
    print(f'\33[1;35m A senha segura que o sistema gerou foi:\33[m \33[1;33m{pw} \33[m')
    colar = input('Deseja mandar a senha gerada a área de transferencia? S ou N :').lower()
    if colar == 'n':
        print('Ok')
    elif colar == 's':
        pyperclip.copy(pw)
        print('Senha copiada com sucesso!')
    else:
        print('Digita S para sim e N para não')


