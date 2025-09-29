pilha = []
caracter = str()
expressao = str(input('Digite a expressão: ')).strip()
for i in range(0, len(expressao)):
    caracter = expressao[i]
    if caracter == '(':
        pilha.append(caracter)
    elif caracter == ')':
        if len(pilha) == 0:
            print(f'Erro: Parêntese de fechamento sem par correspondente (posição {i}).')
            exit()
        else:
            pilha.pop()
if len(pilha) == 0:
    print('A expressão é válida.')
else:
    print('Erro: Existem parênteses de abertura sem par de fechamento.')

