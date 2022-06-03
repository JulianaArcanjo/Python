valor = int(input('Entre com um número para saber a tabuada: '))  
aux = 0  
print('*' * 13)  
print('Tabuada de {}'.format(valor))  
print('*' * 13)  
while(aux <= 10):  
  print('{0} X {1} = {2}'.format(aux, valor, (aux * valor)))  
  aux = aux + 1 