import pandas as py
import plotly.express as px
import csv
df=py.read_csv("data.csv") 
fig =px.scatter(df,x="Student Number",y="Marks")
fig.show()