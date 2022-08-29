import pandas
import plotly.graph_objects as pg
import csv

df = pandas.read_csv('data.csv')
#Mean of attempts each level
print(df.groupby('level')['attempt'].mean())

levels = ["level 1", "level 2", "level 3", "level 4"]
fig = pg.Figure(pg.Bar(x=df.groupby('level')['attempt'].mean(), y=levels, orientation='h', marker=dict(color=["cadetblue", "deeppink", "lime", "tomato"])))
fig.show()