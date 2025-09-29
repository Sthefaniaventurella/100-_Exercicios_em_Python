from random import choice
a1 = input('Digite o nome do 1° aluno: ')
a2 = input('Digite o nome do 2° aluno: ')
a3 = input('Digite o nome do 3° aluno: ')
a4 = input('Digite o nome do 4° aluno: ')
nome = [a1, a2, a3, a4]
escolhido = choice(nome)
print(f' O aluno sorteado para apagar o quadro é: {escolhido}')