import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv("icecreamsales.csv")
fig = px.scatter(df, x = "Temperature", y = "Ice-cream Sales( ₹ )")
fig.show()
