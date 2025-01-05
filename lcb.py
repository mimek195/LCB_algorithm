import numpy

list_1 = ['a', 'b', 'a', 'm', 'b', 'b', 'a']
list_2 = ['a', 'd', 'c', 'b', 'b', 'a', 'n']

lcb = numpy.zeros((len(list_1), len(list_2)), dtype=int)
result = 0

for i in range(len(list_1)):
    for j in range(len(list_1)):
        if list_1[i] == list_2[j]:
            lcb[i][j] = lcb[i - 1][j - 1] + 1
        else:
            lcb[i][j] = 0
        if lcb[i][j] > result:
            result = lcb[i][j]

print(result)
