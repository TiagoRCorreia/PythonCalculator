#!/usr/bin/python

# Apenas para testar a Gihub CLI
# Criar um repositorio pela linha de comando
# Sem a necessidade de utilizar o browser.


class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def soma(self):
        return self.num1 + self.num2

    def subtrai(self):
        return self.num1 - self.num2

    def multiplica(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2
