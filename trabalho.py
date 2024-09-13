import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import shapiro
from scipy.stats import ttest_ind

astronomy = {'alunos':[1, 2 ,3, 4, 5, 6, 7, 8, 9, 10,
11, 12 ,13, 14, 15, 16, 17, 18, 19, 20,
21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35],
'pré': [10, 26, 17, 19, 22, 21, 12, 19, 17, 12, 14, 20, 12,
        12, 15, 20, 16, 17, 15, 15, 15, 15, 14, 16, 15, 14,
        23, 13, 14, 20, 19, 17, 16, 13, 17],
'pós': [14, 26, 18, 24, 27, 27, 25, 23, 19, 16, 21, 26, 13,
        20, 14, 27, 22, 16, 20, 20, 22, 18, 18, 21, 22, 22, 22, 15, 
        23, 29, 24, 12, 15, 20, 20]
}

dataFrame = pd.DataFrame(astronomy, columns = ['alunos', 'pré', 'pós'])
print(dataFrame)

stats, p = shapiro(dataFrame['pós']- dataFrame['pré'])
print('stats=%.3f, p=%.3f' % (stats, p))
if p > 0.05:
    print('Normalidade dos dados (falha em rejeitar H0)')
else:
    print('Não é normalidade dos dados (rejeita-se H0)')

plt.hist(dataFrame['pós']- dataFrame['pré'])
plt.show()

stat1, p1= ttest_ind(dataFrame['pré'], dataFrame['pós'])
print('stats=%.3f, p=%.3f' % (stat1, p1))
if p1 > 0.05:
    print('Não há diferença significativa (falha em rejeitar H0)')
else:
    print('Há diferença significativa (rejeita-se H0)')
