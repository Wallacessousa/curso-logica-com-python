# Coleções (listas)

# ao invés de usar:
preco_1 = 20
preco_2 = 50
preco_3 = 200

#usar lista:
precos = [20,50,200] # 0 1 2 - Começa sempre do zero
print(precos[0]) # vai imprimir o valor do intem 0 (20)

#pode usar o valor pra descobrir qual é a ordem do intem:
print(precos.index(200)) #Vai imprimir o n. 2, pois é o item referente.



''' As listas são dinamicas. Podendo armazenar numeros, valores boleanos'''

diversidades = ['wallace',15,True]
print(diversidades[0])
print(diversidades[1])
print(diversidades[2])


'''Para imprimir todos os itens da lista:'''
for preco in precos:
    print(preco) 
    

'''EXEMPLO 5 - SOME OS VALORES
Dados uma coleção de dados "idades" [15,46,75,34,23],
imprima na tela a soma destes valores.

*pseudo codigo:
idades = [15,46,75,34,23]
total = 0
loop idade em idades
    total = total + idade
print total
'''

idades = [15,46,75,34,23]
total = 0
for idade in idades:
    total = total + idade
print (total)