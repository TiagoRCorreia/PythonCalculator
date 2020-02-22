#!/usr/bin/python

# Apenas para testar a Gihub CLI
# Criar um repositorio pela linha de comando
# Sem a necessidade de utilizar o browser.

num1 = 150
num2 = 20

def soma(num1, num2):
    return(num1 + num2)

def subtrai(num1, num2):
    return(num1 - num2)

def multiplica(num1, num2):
    return(num1 * num2)

def divide(num1, num2):
    return(num1 / num2)

print("O resultado da soma é " + str(soma(num1,num2)))
print("O resultado da subtração é " + str(subtrai(num1,num2)))
print("O resultado da multiplicação é " + str(multiplica(num1,num2)))
print("O resultado da divisão é " + str(divide(num1,num2)))
