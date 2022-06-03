meuCartão = int(input("digite o numero do cartão de crédito: "))

cartãoLido = 1
encontreiMeuCartão = False

while cartãoLido != 0:
    cartãoLido =int(input("digite o numero do proximo cartão de crédito: "))
    if cartãoLido == meuCartão:
        encontreiMeuCartão = True
if  encontreiMeuCartão:
    print("Eba!!! Achei meu cartão!")
else:
    print("Ops, perdi meu cartão! :( ")

