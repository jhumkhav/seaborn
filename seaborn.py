from numpy import median
import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use("Agg")
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
    plt.scatter(df[ 'Mean'], df['Median'])
    plt.ylim(0,0.01)
    plt.xlabel("Mean")
    plt.ylabel("Median")
    plt.show()

def histogram(df):
    plt.hist(df["Mean"], bins=10)
    plt.xlabel("Mean Values")
    plt.ylabel("Amount")
    plt.show()

def scatter_plot2(df):
        plt.scatter(df['Mean'], df['Max'])
        plt.ylim(0,0.01)
        plt.xlabel("Mean")
        plt.ylabel("Max")
        plt.show()

if __name__ == "__main__":
    file = open(input("Filename: "))
    values = list_of_values(file)
    df = pd.DataFrame(values,columns=['Min','Max','Median','Mean'])
    scatter_plot(df)
    histogram(df)
    scatter_plot2(df)
