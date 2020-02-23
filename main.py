#!/usr/bin/python

# Apenas para testar a Gihub CLI
# Criar um repositorio pela linha de comando
# Sem a necessidade de utilizar o browser.
from termcolor import colored
import Calculator as Calc
import argparse
import sys

VERSION = "1.1"
NUM1 = 100
NUM2 = 70


def main():
    ps = argparse.ArgumentParser()

    ps.add_argument("--num1", help="first number", type=int, default=NUM1)
    ps.add_argument("--num2", help="second number", type=int, default=NUM2)
    ps.add_argument("--version", help="output version information", action="store_true")

    args = ps.parse_args()

    if args.version:
        print("Version:", VERSION)
        sys.exit(0)

    c1 = Calc.Calculator(args.num1, args.num2)

    print("O resultado da Soma é ->", colored(c1.soma(), "green"))
    print("O resultado da Subtração é ->", colored(c1.subtrai(), "green"))
    print("O resultado da Multiplicação é ->", colored(c1.multiplica(), "green"))
    print("O resultado da Divisão é ->", colored(c1.divide(), "green"))


if __name__ == "__main__":
    main()
