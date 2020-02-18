horaTrabalhada = float(input("Entre a quantidade de horas trabalhadas:   "))
vlrHora = float(input("Entre o valor da hora de trabalho:  "))
percentDesconto = float(input("Entre o valor percentual do desconto:   "))

salarioBruto = horaTrabalhada * vlrHora
totalDesconto = (percentDesconto / 100) * salarioBruto
salarioLiquido = salarioBruto - totalDesconto

print()

print("Salario Bruto........ %8.2f" % salarioBruto)
print("Desconto...... %8.2f" % totalDesconto)
print("Salario Liquido...... %8.2f" % salarioLiquido)


#Outra maneira de declarar o programa
#salario = int(input('Salario? '))
#imposto = float(input('Imposto em % (ex: 27.5)? '))
#print("Valor real: {0}".format(salario - (salario *(imposto * 0.01))))

