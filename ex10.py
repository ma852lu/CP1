a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
op = input("Escolha a operação (+, -, *, /): ")

if op == "+":
    resultado = a + b
elif op == "-":
    resultado = a - b
elif op == "*":
    resultado = a * b
elif op == "/":
    if b != 0:
        resultado = a / b
    else:
        print("Erro: divisão por zero")
        exit()
else:
    print("Operação inválida")
    exit()

print(f"Resultado: {resultado}")
