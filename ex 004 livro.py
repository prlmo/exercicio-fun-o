#4. Escreva uma função que receba um número inteiro N e retorne uma lista com os bits 0 e 1,
# que representam N convertido para binário. Não use nenhuma função Python de conversão para binários.
# Em vez disso, elabore uma lógica baseada no processo de divisões sucessivas.
def binario(x):
    L = []
    i = 2
    while 0 < x:
        res = x // i
        sobra = x % i
        L.insert(0, sobra)
        if res == 1 and sobra == 1:
            L.insert(0, res)
            break
        else:
            x = res
    return L


n = int(input('Digite um numero: '))
b = binario(n)
print(f'O número {n} convertido para binário fica assim: {b}')