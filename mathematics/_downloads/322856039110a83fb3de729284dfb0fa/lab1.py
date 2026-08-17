from scipy.stats import laplace, uniform, norm, cauchy, poisson
import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd
from tabulate import tabulate

# Task 1
selection_size = [10, 50, 1000]  # Размеры выборок
HIST_TYPE = 'stepfilled'  # Вид гистограммы
LINE = 'k-.'
hist_visibility = 0.5
line_width = 1

TITLE = "Size: " 
Y_LABEL = "Probability density"


def plot_distribution(dist, params, label, color):
    for size in selection_size:
        fig, ax = plt.subplots(1, 1)
        random_values = dist.rvs(size=size, **params)        
        if dist == poisson:  
            ax.hist(random_values, density=True, histtype=HIST_TYPE, alpha=hist_visibility, color=color, label='Histogram')            
            x = np.arange(dist.ppf(0.01, **params), dist.ppf(0.99, **params))
            ax.plot(x, dist.pmf(x, **params), LINE, lw=line_width, label='PMF')
        else:
            ax.hist(random_values, density=True, histtype=HIST_TYPE, alpha=hist_visibility, color=color)
            x = np.linspace(dist.ppf(0.01, **params), dist.ppf(0.99, **params), 100)
            ax.plot(x, dist.pdf(x, **params), LINE, lw=line_width)
        ax.set_xlabel(label)
        ax.set_ylabel(Y_LABEL)
        ax.set_title(TITLE + str(size))
        plt.grid()
        plt.legend()
        plt.show()


# Построение графиков для каждого распределения
plot_distribution(norm, {'scale': 1, 'loc': 0}, "Normal distribution", "green")
plot_distribution(cauchy, {'scale': 1, 'loc': 0}, "Cauchy distribution", "grey")
plot_distribution(poisson, {'mu': 10}, "Poisson distribution", "violet")
plot_distribution(uniform, {'scale': 2*math.sqrt(3), 'loc': -math.sqrt(3)}, "Uniform distribution", "red")


#Task 2
sample_sizes = [10, 100, 1000]  # Размеры выборок
num_iterations = 1000  # Количество повторений

# Функция для вычисления статистических характеристик
def calculate_statistics(samples):
    mean = np.mean(samples)  # Среднее значение
    median = np.median(samples)  # Медиана
    Q1 = np.percentile(samples, 25)  
    Q3 = np.percentile(samples, 75)  
    zQ = (Q1 + Q3) / 2 
    return mean, median, zQ

# Функция для вычисления и вывода таблицы результатов
def compute_and_print_table(dist, params, label):
    results = {size: {'mean': [], 'median': [], 'zQ': []} for size in sample_sizes}
    
    for size in sample_sizes:
        for _ in range(num_iterations):
            random_values = dist.rvs(size=size, **params)
            mean, median, zQ = calculate_statistics(random_values)
            results[size]['mean'].append(mean)
            results[size]['median'].append(median)
            results[size]['zQ'].append(zQ)

    data = []
    for size in sample_sizes:
        E_mean = np.mean(results[size]['mean'])
        E_median = np.mean(results[size]['median'])
        E_zQ = np.mean(results[size]['zQ'])
        
        D_mean = np.var(results[size]['mean'])
        D_median = np.var(results[size]['median'])
        D_zQ = np.var(results[size]['zQ'])
        
        data.append([size, E_mean, E_median, E_zQ, D_mean, D_median, D_zQ])
    
    df = pd.DataFrame(data, columns=["Sample Size", "E(mean)", "E(median)", "E(zQ)", "D(mean)", "D(median)", "D(zQ)"])
    print(f"\nResults for {label} distribution:")
    df = df.round(4)
    print(df.to_markdown(index=False))


compute_and_print_table(norm, {'loc': 0, 'scale': 1}, "Normal")
compute_and_print_table(cauchy, {'loc': 0, 'scale': 1}, "Cauchy")
compute_and_print_table(poisson, {'mu': 10}, "Poisson")
compute_and_print_table(uniform, {'loc': -np.sqrt(3), 'scale': 2*np.sqrt(3)}, "Uniform")