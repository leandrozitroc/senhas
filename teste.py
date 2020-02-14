from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", 'wb') as key_file:
        key_file.write(key)
write_key()


def cript_arquivo(filename, key):
    f = Fernet(key)
    with open (filename, 'rb') as file:
        file_data = file.read()
        data_encripitada = f.encrypt(file_data)
    with open(filename, 'wb') as file:
        file.write(data_encripitada)


caraio('key', 'hbZuAGdHuwnYKk-Y8gR2B05ADqwRdh4C3AZlYsI5DJI=')
