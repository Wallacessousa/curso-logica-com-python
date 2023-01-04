'''
#  Projeto - Medidor de velocidade

Levando  em consideraçãoa velocidade máxima permitidade de 80km/h
em uma determinada rua, crie um programa que recebe do usuário um
valor que representa a velocidade e com base nessa velocidade
diga se ele tomou uma multa leve, grave ou gravíssima. 
Levando em consideração que se a pessoa estiver abaixo da velocidade máxima,
seu programa deve exibir:
"Não houve multa", caso esteja até 10 km acimna é leve. entre 11 e 20km acima, deve exibir "Multa Grave".
Acima de +20km="Multa gravíssima"

1. Quais são os dados de entrada necessários?
        velocidade_máxima = 80
        input = ('Qual foi a velocidade atingida?:')
        
    2. O que devo fazer com esses dados?
        Comparar a velocidade máxima com a v. atingida e printar na tela se ele
        tomou uma multa leve, grave ou gravíssima. 
        
    3. Quais são as restrições desse problema?
        
    4. Qual é o resultado esperado?
        printar na tela se ele tomou uma multa leve, grave ou gravíssima. 
        
    5. Qual é a sequencia de passos para chegar no resultado?(pseudocodigo)
    velocidade_max = 80
    velocidade = (input "Qual foi a velocidade atingida?")
    if velocidade <= velocidade_max:
        print "Não houve multa" 
    if velocidade > velocidade_max e velocidade_max +10:
        print "Multa Leve"
    if velocidade > velocidade_max +11 e velocidade_max +20:
        print "Multa grave"
    if velocidade > velocidade_max +20:
        print "Multa gravíssima"
'''

velocidade = int(input('Qual foi a velocidade?'))
velocidade_max = 80
if velocidade <= velocidade_max:
    print('Não houve multa')
elif velocidade > velocidade_max and velocidade <= velocidade_max + 10:
    print('Multa leve')
elif velocidade >= velocidade_max + 11 and velocidade <= velocidade_max + 20:
    print('Multa grave')
elif velocidade > velocidade_max + 21:
    print('Multa gravíssima')