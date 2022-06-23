#. Escreva uma função que receba uma lista L e elimine os eventuais elemen-tos repetidos contidos na mesma,
# deixando na lista resultante apenas uma ocorrência de cada elemento. Escreva um programa para testar essa fun-ção,
# o qual deve ler do teclado os elementos que farão parte da lista. (veja o Exercício proposto 4.10)
def list(x):
    repetidos = []
    unicos = []
    for j in range(len(x)):
        cont = x[j]
        rep = 1
        for k in range(j+1, len(x)):
            if cont in repetidos:
                break
            if cont == x[k]:
                repetidos.append(x[k])
    for final in x:
        if final in repetidos:
            continue
        else:
            unicos.append(final)
    unicos.sort()
    return unicos


L = []
n = int(input('Digite um numero: '))
while n != 0:
    if n == 0:
        break
    else:
        L.append(n)
        n = int(input('Digite um numero: '))
res = list(L)
print(f'Valores únicos na lista: {res}')