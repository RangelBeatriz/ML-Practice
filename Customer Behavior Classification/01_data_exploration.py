import pandas as pd
import numpy as np
from dateutil import parser
import matplotlib.pyplot as plt
import seaborn as sns
import os

path = os.getcwd()

df = pd.read_csv(path + '/data/appdata10.csv')

print(df.head())

print(df.describe())


df["hour"] = df.hour.str.slice(1, 3).astype(int)
