"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

# print('0',lista[0], '1',lista[1], '2',lista[2])

lista = ['Maria', 'Helena', 'Luiz']
lista.append('joão')

indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))