import pandas as pd
import matplotlib.pyplot as plt

erros = {'dias':[1, 2 ,3, 4, 5, 6, 7, 8, 9, 10,
11, 12 ,13, 14, 15, 16, 17, 18, 19, 20,
21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
'Erros por dia': [8, 11, 8, 12, 14, 13, 11, 14, 14, 15,
6, 10, 14, 19, 6, 12, 7, 5, 8, 8,
10, 16, 10, 12, 12, 8, 11, 6, 7, 12,
7, 10, 14, 5, 12, 7, 9, 12, 11, 9,
14, 8, 14, 8, 12, 10, 12, 22, 7, 15]}

dataFrame = pd.DataFrame(erros)

print(dataFrame)

plt.scatter(x=dataFrame['dias'], y=dataFrame['Erros por dia'])
plt.xlabel('Dias') # Add label for x-axis
plt.ylabel('Erros por Dia') # Add label for y-axis
plt.title('Gráfico de Dispersão de Erros por Dia') # Add a title to the plot
plt.show()

frenq_abs = []
frenq_rel = []
densidade_freq = []
classe_de_erros = [(4, 9), (9, 14), (14, 19), (19, 24)]

for intervalo in classe_de_erros:
    contagem = sum(1 for numero in dataFrame['Erros por dia'] if intervalo[0] <= numero < intervalo[1])
    frenq_abs.append(contagem)
    frenq_rel.append(contagem / len(numeros))
    densidade_freq.append(contagem / (len(numeros) * (intervalo[1] - intervalo[0])))
hist = {'classe de erros': classe_de_erros, 
        'Frequências Absolutas': frenq_abs, 
        'Frequências Relativas': frenq_rel,
        'Densidade de Frequência': densidade_freq}
histFrames= pd.DataFrame(hist)
print(histFrames)
histograma = dataFrame['Erros por dia'].hist()
plt.show()
numeros_unicos = sorted(set(dataFrame['Erros por dia']))

print("Ramo | Folhas")
print("-----|-------")
for numero in numeros_unicos:
    print(f"  {numero}  | 0")
