numero = int(input('Digite um número: '))
print(('Escolha qual será a base de conversão: \n'
       '- [1] para \033[33mBINÁRIO \033[m\n'
      '- [2] para \033[33mOCTAL \033[m\n'
      '- [3] para \033[33mHEXADECIMAL \033[m\n'))
escolha = int(input('Sua opção: '))
if escolha == 1:
    print(f'{numero} Convertido para BINÁRIO é igual a {bin(numero)[2:]}')
elif escolha == 2:
    print(f'{numero} Convertido para OCTAL é igual a {oct(numero)[2:]}')
elif escolha == 3:
    print(f'{numero} Convertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
else:
    print('Opção inválida. Tente novamente.')


