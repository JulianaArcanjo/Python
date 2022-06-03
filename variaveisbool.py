

decrescente =True
anterior = int (input("digite o primeiro numero da sequência: "))
valor = 1

while valor != 0 and decrescente:
    valor = int(input("digite o proximo numero da sequência: "))
    if valor > anterior:
        decrescente = False
    anterior = valor
if decrescente == True:
    print("A sequência está em ordem decrescrente! :-) ")
else:
     print("A sequência está em ordem crescrente! :-(  ")    