# sobrecarga: quando o mesmo método tem mais de uma forma

def sobrecarga(nome, numero = None):
    print(nome)
    if numero:
        print(numero)


print('Primeira execução')
sobrecarga('Gustavo')

print('\nSegunda execução')
sobrecarga('Gustavo', 10)