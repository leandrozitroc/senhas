def valida(msg):
    while True:
        try:
            n=int(input(msg))
        except (ValueError, TypeError):
            print('Favor Insira um numero inteiro valido: ')
        else:
            if n <= 6:
                return n
            else:
                print('Digite uma das opções acima: ')

