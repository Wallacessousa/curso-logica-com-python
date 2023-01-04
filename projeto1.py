#EXEMPLO 5 - Fatorial de um número
'''
Crie um programa que recebe um número e imprime o fatorial
daquele número.

# método 5 Q's para montar o algorítimo:

- Analise criticamente o problema e descubra:
    1. Quais são os dados de entrada necessários?
        numero
        
    2. O que devo fazer com esses dados?
        Devo calcular o fatorial do numero recebido e exibir na tela
        
    3. Quais são as restrições desse problema?
        A) o numero deve ser positivo B) deve ser inteiro
        
    4. Qual é o resultado esperado?
        Que o fatorial do nuemro desejado seja exibido.
        
    5. Qual é a sequencia de passos para chegar no resultado?(pseudocodigo)
        input numero
        if numero > 0
        if numero = inteiro
        fatorial = 1
        loop de 1 a numero
            fatorial = fatorial * numero
        print (fatorial)
'''

#codando...

numero = int(input('Digite um número: '))
if numero > 0:
    fatorial = 1
    for item in range(1,numero +1):
            fatorial = fatorial * item
            print(fatorial)