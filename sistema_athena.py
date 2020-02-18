from senhas.valida import valida
from senhas.luli import *
from senhas.repositorio import *
print('==='* 18)
print('==='* 18)
print('\33[1;34mBem vindo ao sistema Athena\33[m'.center(20 *3))
print('==='* 18)
print('==='* 18)

while True:
      print('==='* 18)
      print('[1] Gerar Senha: \n'                         
            '[2] Criptografar Senha: \n'                
            '[3] Descriptografar Senha: \n'              
            '[4] Criptografar Arquivo: \n'   
            '[5] Descriptografar Arquvivo: \n'
            '[6] Acessar Repositorio de Senhas:\n'
            '[7] Sair')
      print('==='* 18)
      escolha = valida('Digite uma opção: ')
      if escolha == 1:
            print('==='* 18)
            gerarsenha()

      elif escolha == 4:
            cript_arquivo(input('digite o nome do arquivo que será Encriptado: '), "ccLmrWCJu7vpwaroDuSEjv6amtpLyiY9MI-PS-oWy_4=")
      elif escolha == 2:
            encript_senha(input('Senha a ser Encriptada: '), "ccLmrWCJu7vpwaroDuSEjv6amtpLyiY9MI-PS-oWy_4=")
      elif escolha == 3:
            decript_senha(input('Senha a ser decriptada: '), "ccLmrWCJu7vpwaroDuSEjv6amtpLyiY9MI-PS-oWy_4=")
      elif escolha == 5:
            decript_arquivo(input('Digite o Arquivo que sera Decriptado: '), "ccLmrWCJu7vpwaroDuSEjv6amtpLyiY9MI-PS-oWy_4=")
      elif escolha == 6:
            repositorio()
      elif escolha ==7:
            print('==='* 18)
            print('\33[4;36mObrigado por usar o sistema Athena\33[m ')
            break


