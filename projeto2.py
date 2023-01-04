'''
Escreva um programa que , ao iniciar gera um valor aleatório de 1 a 10 
e perminet que o usuário chute um númer até que o valor aleatório gerado
no início do programa seja chutado corretamente.

O programa deve informar se o chute foi acima, abaixo ou igual ao valor
aleatório gerado no início do programa.

# Método 5Qs
1. Dados necessários:
    1-10, chute do usuário
2. o que fzez com esses dados?
    comparar o chute do usuario com o valor aleatorio gerado e dizer se foi maior, menor ou igual
3. Quais restrições?
    de 1 a 10
4. Resultado esperado?
    o resultado é dizer se o chute do usuario com o valor aleatorio gerado e dizer se foi maior, menor ou igual
5. Sequencia de passos:
input valor_aleatório de 1 a 10
input chute
if chute > valoraleatorio:
    print(chute foi maior que o valor gerado)
if chute < valoraleatorio:
    print(chute foi menor que o valor gerado)
if chute = valoraleatorio:
    print(Você acertou!)
'''

import random # O python tem esse biblioteca de valores aleatórios pra importar

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int(input('Chute um valor de 1 a 10: '))
    if chute > valor_aleatorio:
        print('chute foi maior que o valor gerado')
    elif chute < valor_aleatorio:
        print('chute foi menor que o valor gerado')
    elif chute == valor_aleatorio:
        acertou = True
        print('Você acertou!')