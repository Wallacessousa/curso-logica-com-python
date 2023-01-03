# Laços de repetição + Listas
'''Ao invés de fazer isso:'''
print('carregando')
print('carregando')
print('carregando')

'''Pode fazer isso:'''
for palavra in range (1,4):
    print('Carregando')

'''
for item in coleção:
    espressão
'''    

# Assim, ele printa tudo, menos o ultimo:
for item in range(1,20):
    print(item)
    
# Assim, ele printa pulando 2 numeros:
for item in range(1,20,2):
    print(item)
    
    
# Ex com nomes:
nomes = ('Jhonatan','Chrinstian','Roberto','Camila')
for nome in nomes:
    print(nome)
    



''' IMPRIMA OS VALORESDE 1 A N'''
# PESEUDO CODIGO #
'''
input numero maximo
valor inicial = 1
loop de valor_inicial e numero_maximo
    print valor
'''
# Transformando em Python:
valor_maximo = int(input ('Digite o valor máximo: '))
valor_inicial = 1
for numero in range(valor_inicial,valor_maximo +1):
    print(numero)