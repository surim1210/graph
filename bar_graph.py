import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/silicon.csv')
bool_female = df['gender']=='Female'
bool_manager = df['job_category'] == 'Managers'
bool_not_all = df['race_ethnicity'] != 'All'

df[bool_female & bool_manager & bool_not_all].plot(kind='bar', x='race_ethnicity',  y='count')

plt.show()