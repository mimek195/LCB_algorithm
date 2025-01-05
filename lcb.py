import numpy

lista_1 = ['a', 'b', 'a', 'm', 'b', 'b', 'a']
lista_2 = ['a', 'd', 'c', 'b', 'b', 'a', 'n']

lcb = numpy.zeros((len(lista_1), len(lista_2)), dtype=int)
wynik = 0

for i in range(len(lista_1)):
    for j in range(len(lista_1)):
        if lista_1[i] == lista_2[j]:
            lcb[i][j] = lcb[i - 1][j - 1] + 1
        else:
            lcb[i][j] = 0
        if lcb[i][j] > wynik:
            wynik = lcb[i][j]

print(wynik)
