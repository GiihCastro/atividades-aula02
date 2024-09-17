# Comparação de Idades:
# Peça ao usuário duas idades e use operadores de comparação para verificar se a primeira idade é maior, menor ou igual à segunda.

idade_usuario = int(input('Digite a sua idade: '))
idade_parente = int(input('Digite a idade do seu parente mais próximo: '))

if idade_usuario < idade_parente:
    print('A idade do seu parente é maior do que a sua!')
elif idade_usuario == idade_parente:
    print('As duas idades são iguais!')
else:
    print('A sua idade é maior do que a do seu parente!')