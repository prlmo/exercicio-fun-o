#6. Escreva um programa que receba como parâmetro de entrada um número inteiro de 5 dígitos no
# intervalo fechado [10000, 30000] que represente có-digos de produtos vendidos em uma loja.
# A função deve calcular e retornar o dígito verificador utilizando regra de cálculo explicada a seguir.
# Considere o código 21853, em que cada dígito é multiplicado por um peso começando em 2,
# os valores obtidos são somados, e do total obtido calcula-se o resto de sua divisão por 7.
# imagem de exemplo representada no livro.
#1°dig    2°    3°   4°   5°
#peso 2    3    4     5   6 e depois calcular o resto da soma por 7
def digVerificador(a, b, c, d, e):
    calculo = ((a * 2)+(b * 3)+(c * 4)+(d * 5)+(e * 6)) % 7
    return calculo


n = input('Digite um numero no intervalo de 10000 á 30000: ')
L = []
for i in n:
    L.append(int(i))
res = digVerificador(*L)
print(res)