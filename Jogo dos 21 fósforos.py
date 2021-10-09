def joga_primeiro():
    r = input('Quem joga primeiro, jogador ou CPU?')
    if r == 'CPU':
        CPU()
    else:
        Jogador()

def Jogador():
    total = 21
    while total > 1:
        s = input('Escolha quantos fósforos quer tirar:')
        p = 5 - int(s)
        print('CPU tira', p)
        total = total - 5
        print('Ficam', total, 'fósforos')
    print('CPU ganhou o jogo!')


def CPU():
    total = 21
    while total > 1:
        print('CPU tira 1 fósforo')
        q = input('Escolha quantos fósforos quer tirar:')
        total = total - 1 - int(q)
        print('Ficam', total, 'fósforos')
        if int(q) + 1 != 5:
            print('CPU tira', 4-int(q))
            total = total - (4-int(q))
            while total > 1:
                s = input('Escolha quantos fósforos quer tirar:')
                p = 5 - int(s)
                print('CPU tira', p)
                total = total - 5
                print('Ficam', total, 'fósforos')
            print('CPU ganhou o jogo!')
        elif total == 1:
            print('Excelente, ganhou o jogo!')

joga_primeiro()
        
