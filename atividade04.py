# Verificação de Notas Aprovadas:
# Escreva um programa que peça duas notas de um aluno. Use operadores

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

if nota1 >= 6 and nota2 >= 6:
    print(f'Parabéns! As notas {nota1} e {nota2} estão aprovadas pois são maiores que 6!')
elif nota1 < 6:
    print(f'Que pena! Apenas a nota {nota2} está aprovada pois a nota {nota1} é menor que 6!')
elif nota2 < 6:
    print(f'Que pena! Apenas a nota {nota1} está aprovada pois a nota {nota2} é menor que 6!')
elif nota1 < 6 and nota2 < 6:
    print(f'Que pena! Tanto a nota {nota1} quanto a nota {nota2} estão reprovadas pois são menores que 6!')
else:
    print('As notas são iguais!')