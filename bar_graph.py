import matplotlib.pyplot as plt
import pandas as pd

bar_df = pd.read_csv('data/silicon.csv', index_col=0)


bool_female = bar_df['gender'] == 'Male'
bool_manager = bar_df['job_category'] == 'Managers'
bool_not_all = bar_df['race_ethnicity'] != 'All'

bar_graph = bar_df[bool_female & bool_manager & bool_not_all].plot(kind='bar', x='race_ethnicity',  y='count')

plt.show()