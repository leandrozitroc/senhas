from senhas.valida import valida
from senhas.luli import *
print('==='* 18)
print('==='* 18)
print('\33[1;34mBem vindo ao sistema Athena\33[m'.center(20 *3))
print('==='* 18)
print('==='* 18)

while True:
      print('==='* 18)
      print('[1] Gerar Senha: \n'                         
            '[2] Criptografar Arquivo: \n'                
            '[3] Criptografar Senha: \n'              
            '[4] Descriptografar Senha: \n'   
            '[5] Descriptografar Arquivo: \n'
            '[6] Sair')
      print('==='* 18)
      escolha = valida('Digite uma opção: ')
      if escolha == 1:
            print('==='* 18)
            gerarsenha()

      elif escolha == 2:
            cript_arquivo(input('digite o nome do arquivo que será Encriptado: '), "ccLmrWCJu7vpwaroDuSEjv6amtpLyiY9MI-PS-oWy_4=")
      elif escolha == 3:
            'cript_senha'
      elif escolha == 4:
            'decript_senha'
      elif escolha == 5:
            decript_arquivo(input('Digite o Arquivo que será Decriptado: '), "ccLmrWCJu7vpwaroDuSEjv6amtpLyiY9MI-PS-oWy_4=" )
      elif escolha ==6:
            print('==='* 18)
            print('\33[4;36mObrigado por usar o sistema Athena\33[m ')
            break


