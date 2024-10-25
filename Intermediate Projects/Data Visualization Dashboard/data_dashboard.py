# This is the main Python file for the Data Visualization Dashboard project.
import matplotlib.pyplot as plt

def plot_data(data):
    labels, values = zip(*data.items())
    plt.bar(labels, values)
    plt.xlabel('Category')
    plt.ylabel('Value')
    plt.title('Data Visualization Dashboard')
    plt.show()

data = {
    'Category A': 23,
    'Category B': 17,
    'Category C': 35,
    'Category D': 29
}

plot_data(data)
