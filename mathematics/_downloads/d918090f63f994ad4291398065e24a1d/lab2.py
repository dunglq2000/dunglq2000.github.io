from scipy.stats import norm, laplace, poisson, cauchy, uniform
import numpy as np
import math as m
import seaborn as sns
import matplotlib.pyplot as plt
sizes = [20, 100, 1000]
NORMAL, CAUCHY, POISSON, UNIFORM = "NormalNumber", "CauchyNumber", "PoissonNumber", "UniformNumber"
NUMBER_OF_REPETITIONS = 1000
STR_1, STR_2, STR_3 = 'Доля выбросов выборки из 20 элементов: ', 'Доля выбросов выборки из 100 элементов: ', 'Доля выбросов выборки из 1000 элементов: '
EXPANSION = '.jpg'
def moustache(distribution):
  q_1, q_3 = np.quantile(distribution, [0.25, 0.75])
  return q_1 - 3 / 2 * (q_3 - q_1), q_3 + 3 / 2 * (q_3 - q_1)

def count_out(distribution):
  x1, x2 = moustache(distribution)
  filtered = [x for x in distribution if x > x2 or x < x1]
  return len(filtered)

def DrawBoxplot(tips, name):
    sns.set_theme(style="whitegrid")    
    sns.boxplot(data=tips, palette='rainbow', orient='h');
    sns.despine(offset=10)
    plt.xlabel("x")
    plt.ylabel("n")
    plt.title(name)
    plt.yticks(np.arange(len(sizes)), sizes) 
    plt.savefig(str(name)+EXPANSION)    
    return

def printAnswer(result):
    print(STR_1 + str(result[0]))
    print(STR_2 + str(result[1]))
    print(STR_3 + str(result[2]))

def NormalBoxplotTukey():
    tips, result, count = [], [], 0
    for size in sizes:
        for i in range(NUMBER_OF_REPETITIONS):
            distribution = norm.rvs(size=size)
            distribution.sort()
            count += count_out(distribution)
        result.append(count/(size * NUMBER_OF_REPETITIONS))
        distribution = norm.rvs(size=size)
        distribution.sort()
        tips.append(distribution)
    DrawBoxplot(tips, NORMAL)  
    printAnswer(result)
    return
def CauchyBoxplotTukey():
    tips, result, count = [], [], 0
    for size in sizes:
        for i in range(NUMBER_OF_REPETITIONS):
            distribution = cauchy.rvs(size=size)
            distribution.sort()
            count += count_out(distribution)
        result.append(count/(size * NUMBER_OF_REPETITIONS))
        distribution = cauchy.rvs(size=size)
        distribution.sort()
        tips.append(distribution)
    DrawBoxplot(tips, CAUCHY)  
    printAnswer(result)
    return
def PoissonBoxplotTukey():
    tips, result, count = [], [], 0
    for size in sizes:
        for i in range(NUMBER_OF_REPETITIONS):
            distribution = poisson.rvs(10, size=size)
            distribution.sort()
            count += count_out(distribution)
        result.append(count/(size * NUMBER_OF_REPETITIONS))
        distribution = poisson.rvs(10, size=size)
        distribution.sort()
        tips.append(distribution)
    DrawBoxplot(tips, POISSON)  
    printAnswer(result)
    return
def UniformBoxplotTukey():
    tips, result, count = [], [], 0
    for size in sizes:
        for i in range(NUMBER_OF_REPETITIONS):
            distribution = uniform.rvs(size=size, loc=-m.sqrt(3), scale=2 * m.sqrt(3))
            distribution.sort()
            count += count_out(distribution)
        result.append(count/(size * NUMBER_OF_REPETITIONS))
        distribution = uniform.rvs(size=size, loc=-m.sqrt(3), scale=2 * m.sqrt(3))
        distribution.sort()
        tips.append(distribution)
    DrawBoxplot(tips, UNIFORM)  
    printAnswer(result)
    return

NormalBoxplotTukey()
CauchyBoxplotTukey()
PoissonBoxplotTukey()
UniformBoxplotTukey()