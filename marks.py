import pandas as pd
import numpy as n
import os
os.system("cls")
import plotly.express as pe

df = pd.read_csv("marks.csv")
present = df["Days Present"].tolist()
marks = df["Marks In Percentage"].tolist()

d = {"x":present,"y":marks}
correlation = n.corrcoef(d["x"],d["y"])
print(correlation)