import pandas as pd
import matplotlib.pyplot as plt
import statistics as st


corretora1 = {'porcentagens da corretora 1': [45, 62, 38, 55, 54, 65, 60, 55, 48, 56, 59, 55, 54, 70, 64, 55, 48, 60]}
corre1 = pd.DataFrame(corretora1)
corretora2 = {'porcentagens da corretora 2': [57, 50, 59, 61, 57, 55, 59, 55, 52, 55, 52, 57, 58, 51, 58, 59, 56, 53, 50, 54, 56]}
corre2 = pd.DataFrame(corretora2)
print('moda da corretora 1':)
print(st.mode(corre1['porcentagens da corretora 1']))
print('moda da corretora 2':)
print(st.mode(corre2['porcentagens da corretora 2']))
print(corre1.describe())
print(corre2.describe())

corre1.boxplot()
plt.show()
corre2.boxplot()
plt.show()
