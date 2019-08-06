import matplotlib.pyplot as plt
import pandas as pd


line_df = pd.read_csv('data/gdp.csv', index_col=0)

line_graph = line_df.plot(y=["Korea_Rep", "United_States", "United_Kingdom", "Germany", "China", "Japan"])

plt.show()


