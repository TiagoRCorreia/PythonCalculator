#!/usr/bin/python

# Apenas para testar a Gihub CLI
# Criar um repositorio pela linha de comando
# Sem a necessidade de utilizar o browser.

import Calculator as Calc


def main():
    c1 = Calc.Calculator(150, 20)

    print("O resultado da Soma é ->", c1.soma())
    print("O resultado da Subtração é ->", c1.subtrai())
    print("O resultado da Multiplicação é ->", c1.multiplica())
    print("O resultado da Divisão é ->", c1.divide())


if __name__ == "__main__":
    main()
