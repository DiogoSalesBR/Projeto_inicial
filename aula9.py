
n1=float(input('Nota 1°Bimestre: '))
n2=float(input('Nota 2°Bimestre: '))
n3=float(input('Nota 3° Bimestre: '))
n4=float(input('Nota do 4°Bimestre: '))
st=n1+n2+n3+n4
media_aprovado = 7
media_reprovado = 6.9

print(f'O somatorio das notas é igual a {st:.2f}')
print(f'Sua Media Anual é igual a {st/4:.2f}')


if st/4 >= media_aprovado:
    print('Parabens, voce está aprovado')

else:
    print('VOCE ESTÁ REPROVADO')







