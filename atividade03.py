# Verificação de Maioridade e Habilitação:
# Crie um programa que peça a idade do usuário e se ele possui habilitação (sim ou não). 
# Use operadores lógicos para verificar se ele é maior de idade (>= 18) e possui habilitação.

idade = int(input('Digite sua idade: '))
habilitacao = input('Você possui carteira de habilitação? (Sim ou Não): ')

if idade >= 18 and idade < 120 and habilitacao.lower() == 'sim':
    print('Você é maior de idade e possui carteira de habilitação!')
elif idade >= 18 and idade < 120 and habilitacao.lower() == 'não':
    print('Você é maior de idade e não possui carteira de habilitação!')
elif idade < 18 and habilitacao.lower() == 'sim':
    print('Erro! Você é menor de idade, portanto não pode possuir carteira de habilitação!')
elif idade < 18 and habilitacao.lower() == 'não':
    print('Você é menor de idade e não possui carteira de habilitação!')
else:
    print('Algum erro ocorreu! Tente novamente e verifique se as respostas digitadas são válidas!')