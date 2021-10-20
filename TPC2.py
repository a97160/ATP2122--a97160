import random

tentativas = 0

número = random.randint(1, 100)
print('Estou a pensar num número entre 1 e 100.')

while tentativas < 7:
    print('Tente de novo')
    guess = input()
    guess = int(guess)

    tentativas = tentativas + 1

    if guess < número:
        print('Tenta um número maior.')

    elif guess > número:
        print('Tente um número menor.')

    elif guess == número:
        print('Parabéns, acertou o número em', tentativas)
        tentativas = 8

    else: 
        número = str(número)
        print('Não conseguiste! O número que eu estava a pensar é' + número)
