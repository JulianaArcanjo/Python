def eh_primo(x):
    fator = 2
    while x % fator != 0 and fator <= x / 2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True

def maio_primo(n):
    maior_numero = 0
    i = 2
    while i <= n:
        if eh_primo(i):
            print(i)
            maior_numero = i
        i = i + 1
    return maior_numero
   

n = int(input('Digite um número: '))
print ('Maior numero primo: + str(maior_primo(n)')