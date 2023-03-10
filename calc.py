import os 

print("==========")

operacoes = {
    "+": "Soma",
    "-": "Subtração",
    "*": "Multiplicação",
    "/": "Divisão",
    "^": "Exponenciação"
}

while True :
    os.system("clear")
    i = 0
    for op, name in operacoes.items():
        print(i, ":", name)
        i += 1
    print("")
    print("Escolha a operação:")
    op = int(input())
    op_str = list(operacoes.keys())[op]

    print("")
    print("{} ecolhida.".format(op_str))
    print("")
    print("Qual o primeiro valor?")
    v1 = float(input())
    print("Qual o segundo valor?")
    v2 = float(input())

    if op == 0:
        result = v1 + v2
    elif op == 1:
        result = v1 - v2
    elif op == 2:
        result = v1 * v2
    elif op == 3:
        result = v1 / v2
    elif op == 4:
        result = v1 ** v2

    print("")
    print("{} {} {} = {}".format(v1, op_str, v2, result))
    print("")
    
    print("================")
    print("Deseja realizar alguma outra operação?")
    confirme = input()

    if confirme == "n":
        break
        