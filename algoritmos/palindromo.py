"""Verifica se uma palavra é um palíndromo."""

palavra = input().strip().lower()

if palavra == palavra[::-1]:
    print("É palíndromo")
else:
    print("Não é palíndromo")
