#variaveis compostas homegêneas
#conjunto de elementos do mesmo tipo onde cada um pode armazenar um tipo de informação diferente, mas todas com mesmo nome e tipo
#associa-se indíces: representam a posição do vetor, individualizando os elementodos
#array unidimensional: vetor // array multidimensional: matriz 

import os
os.system("cls || clear")


vetor_notas = [2, 5, 10]

#for each:
for nota in vetor_notas:
    print(nota) #para cada nota em notas print nota

#por indice
print(vetor_notas[1])#aparece segunda nota( a contagem começa no 0 )
print(vetor_notas[2])#aparece última nota