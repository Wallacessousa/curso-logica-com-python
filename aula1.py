###### Variáveis #####

# Números ex:
nota_filme = 8,5

# Valores boleanos ex:
esta_aberto = True

# strings ex:
nome_do_curso = "Lógica de programação"


##################################################
#Como váriáveis seriam usadas em um programa real?

#Problema 1 - Valor por hora.
#Escreva um programa que retorna o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.

# Isso é um pseudo codigo:
#      input salario_mensal
#      input horas_trabalhadas_por_mes
#      valor_hora = salario_mensal / horas_trabalhadas_por_mes
#      print valor_hora

#Transformando em Pyton:
salario_mensal = input ('Qual é o seu slário mensal?')
horas_trabalhadas_por_mes = input('Quantas horas trabalha por mês?')
valor_hora = int(salario_mensal) / int(horas_trabalhadas_por_mes)
print(valor_hora)
