# Utilize a função EPrimo desenvolvida no Exercício resolvido 5.1
# para carregar uma lista contendo os N primeiros números primos, em que N é um número inteiro fornecido pelo usuário.
def Eprimo(x):
    L = []
    i = 2
    while len(L) < x:
        for j in range(2, i+1):
            if j == i:
                L.append(i)
                i += 1
                break
            if i % j == 0:
                i += 1
                break
    return L

n = int(input('Digite um numero: '))
p = Eprimo(n)
print(f'Os {n} primeiros numeros primos são = {p}')
#tente testar com os 25 primeiros primos( que são os numeros primos de 1 a 100)
