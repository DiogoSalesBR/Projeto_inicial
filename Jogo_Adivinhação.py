


palavra_secreta = 'aprendizado'
digitadas = []
chance = 3
while True:

    if chance <= 0:
        print('Voce Perdeu :(')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Muito engraçidinho(a), digite apenas 1 letra')
        continue

    digitadas.append(letra)

    if letra in palavra_secreta:
        print(f'Booaa, acabou de acertar a letra "{letra}" que faz parte da palavra secreta.')
    else:
        print(f'Que tal pensar mais um pouco? A letra "{letra}" não faz parte da palavra.')
        digitadas.pop()

    palavra_temporaria = ''
    for letra_temporaria in palavra_secreta:
        if letra_temporaria in digitadas:
            palavra_temporaria += letra_temporaria
        else:
            palavra_temporaria += '*'

    if palavra_temporaria == palavra_secreta:
            print(f'Shoow, acabou de acertar a palavra secreta "{palavra_secreta}"')
            break
    else:
            print(f'Apalavra secreta está assim {palavra_temporaria}')

    if letra not in palavra_secreta:
            chance -= 1
            print(f'Voce ainda tem {chance}. ')
            print()




