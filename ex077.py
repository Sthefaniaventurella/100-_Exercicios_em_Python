palavras = 'livro', 'amor', 'musica', 'arte', 'cores', 'vida'
for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')




