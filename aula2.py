# condicionais:
# if, elif e else


'''      Exemplo 1:
- E ae mano, bora sair hoje?
- Se eu terminar meu trabalho aqui, eu consigo.
'''
# transformando em Pyton:

trabalho_terminado = True
if trabalho_terminado == True:
    print('Opa! Bora dar uma saída.')
else:
    print('po, não vai dar...')
    



'''     Exemplo 2:
- Você consegue me ajudar a levar essas caixas lá pra fora?
- Se eu estiver livre, sim.
'''
# transformando em Pyton:

estou_livre = False
if estou_livre == True:
    print('ok, posso ajudar sim')
else:
    print('Peça para o meu irmão te ajudar')
    
    
    
'''     Exemplo 3:
- Eu cheguei atrasado, posso entrar ainda?
- Se não for seu terceiro atraso, pode.
'''
# transformando em Pyton:

numero_de_atrasos = 0 #pode mudar esse numero pra testar
if numero_de_atrasos >= 3:
    print('Você está suspenso')
elif numero_de_atrasos ==1:
    print('pode entrar, mas se tomar mais duas faltas, ja era')
elif numero_de_atrasos == 2:
    print('Pode entrar, mas se faltar de novo ta lascado')
else:
    print('Pode entrar')
    
    
    '''     Exemplo 4:
Encontre o maior entre 2 números.
Variáveis:

input primeiro_valor
input segundo_valor
if primeiro_valor > segundo_valor
    print o primeiro valor é maior
else
    print o primeiro valor é maior    
'''
# transformando em Pyton:

primeiro_valor = input('Digite 1º valor: ')
segundo_valor = input('Digite 2º valor: ')

if int (primeiro_valor) > int (segundo_valor):
    print('O primeiro valor é maior')
else:
    print('O segundo valor é maior')