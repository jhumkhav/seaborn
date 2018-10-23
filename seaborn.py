from numpy import median
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def each_line(line):
    l = []
    for item in line.strip():
        l.append(ord(item)-33)
    list_nums = []
    for num in l:
        list_nums.append(10**(-num/10))
    return list_nums

def get_values(list_nums):
    mini = min(list_nums)
    maxi = max(list_nums)
    med = median(list_nums)
    mean = sum(list_nums)/len(list_nums)
    return [mini, maxi, med, mean]

def list_of_values(file):
    list_values = []
    for line in file:
        list_nums = each_line(line)
        list_data = get_values(list_nums)
        list_values.append(list_data)
    return list_values

def scatter_plot(df):
    sns.lmplot('Mean', 'Median', data=df, fit_reg=False)
    plt.ylim(0,0.01)
    plt.show()

def histogram(df):
    sns.distplot(df["Mean"], bins=10)
    plt.show()

def strip_plot(df):
    sns.stripplot(x=df["Median"])
    plt.show()

if __name__ == "__main__":
    file = open(input("Filename: "))
    values = list_of_values(file)
    df = pd.DataFrame(values,columns=['Min','Max','Median','Mean'])
    scatter_plot(df)
    histogram(df)
    strip_plot(df)

