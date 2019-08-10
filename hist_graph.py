import matplotlib.pyplot as plt
import pandas as pd

hist = pd.read_csv('data/starbucks.csv')

hist.plot(kind='hist', y='Calories', bins=20)   # bins: 구간 개수

plt.show()