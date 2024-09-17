# Verificar Igualdade de Strings:
# Peça ao usuário duas palavras e use operadores de comparação para verificar se elas são iguais.

palavra1 = input('Digite a primeira palavra: ')
palavra2 = input('Digite a segunda palavra: ')

if palavra1.lower() == palavra2.lower():
    print(f'As palavras "{palavra1}" e "{palavra2}" são iguais.')
else:
    print(f'As palavras "{palavra1}" e "{palavra2}" são diferentes.')