'''
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data/silicon_valley_details.csv')


adobe = df['company'] == 'Adobe'
race = df['race'] == 'Overall_totals'
count = df['count'] != 0

total = df['job_category'] != 'Totals'
previous = df['job_category'] != 'Previous_totals'

boolean_job_category = (df['job_category'] != 'Totals') & (df['job_category'] != 'Previous_totals'
df_condition = df[adobe & race & count & total & previous]
df_condition.set_index('job_category', inplace=True)
df_condition.plot(kind='pie', y='count')
plt.show()
'''
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/silicon_details.csv")

boolean_adobe = df['company'] == 'Adobe'
boolean_all_races = df['race'] == 'Overall_totals'
boolean_count = df['count'] != 0
boolean_job_category = (df['job_category'] != 'Totals') & (df['job_category'] != 'Previous_totals')

df_adobe = df[boolean_adobe & boolean_all_races & boolean_count & boolean_job_category]
df_adobe.set_index('job_category', inplace=True)
df_adobe.plot(kind='pie', y= 'count')
plt.show()