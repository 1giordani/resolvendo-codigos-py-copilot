"""Realiza operações matemáticas básicas com dois números."""

primeiro_numero = float(input())
segundo_numero = float(input())

print(f"Soma: {primeiro_numero + segundo_numero:g}")
print(f"Subtração: {primeiro_numero - segundo_numero:g}")
print(f"Multiplicação: {primeiro_numero * segundo_numero:g}")

if segundo_numero != 0:
    print(f"Divisão: {primeiro_numero / segundo_numero:g}")
else:
    print("Divisão: não é possível dividir por zero")
