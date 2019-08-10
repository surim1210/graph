import matplotlib.pyplot as plt
import pandas as pd

world_df = pd.read_csv('data/world_index.csv')

#1
x = world_df['Life expectancy at birth- years']
y = world_df['Internet users percentage of population 2014']

#2
z = world_df['Forest area percentage of total land area 2012']
f = world_df['Carbon dioxide emissionsAverage annual growth']

plt.scatter(x, y)
plt.show()