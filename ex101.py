from datetime import datetime
def voto(ano):
    data_atual = datetime.now()
    ano_atual = data_atual.year
    id = ano_atual - ano
    if id < 18:
        return print(f'Com {id} anos: NÃO VOTA.')
    elif id >= 18 and id <= 65:
        return print(f'Com {id} anos: VOTO OBRIGATÓRIO.')
    elif id >= 65:
        return print(f'Com {id} anos: VOTO OPCIONAL.')


ano_nasc = int(input('Em que ano você nasceu? '))
voto(ano_nasc)

