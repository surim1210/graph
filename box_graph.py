import matplotlib.pyplot as plt
import pandas as pd

box = pd.read_csv('data/starbucks.csv')

box.plot(kind='box', y='Calories')

plt.show()