valor1 = 1
valor2 = 10
valor3 = 100
valor4 = 26.1965

# Imprime os valores da esquerda para direita sem formatação #
print("|%d|" % valor1)
print("|%d|" % valor2)
print("|%d|" % valor3)
print()

# Imprime os valores da direita para esquerda com 3 espaços #
print("|%3d|" % valor1)
print("|%3d|" % valor2)
print("|%3d|" % valor3)
print()

# Imprime os valores da esquerda para direita com 3 espaços #
print("|%-3d|" % valor1)
print("|%-3d|" % valor2)
print("|%-3d|" % valor3)
print()

# Imprime os valores da direita para esquerda preenchendo os valores em branco zeros #
print("|%03d|" % valor1)
print("|%03d|" % valor2)
print("|%03d|" % valor3)
print()

# Formata o numero de casas decimais apos o ponto. #
# Exemplo de composição: %6.2 = 999.99
print("|%6.0f|" % valor4)
print("|%6.1f|" % valor4)
print("|%6.2f|" % valor4)

