import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():

    df = pd.read_csv("epa-sea-level.csv")

    fig, ax = plt.subplots(figsize=(10,6))

    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(1880, 2051))
    y_pred = res1.intercept + res1.slope * x_pred
    ax.plot(x_pred, y_pred, 'r')

    df_2000 = df[df['Year'] >= 2000]
    res2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_pred2 = pd.Series(range(2000, 2051))
    y_pred2 = res2.intercept + res2.slope * x_pred2
    ax.plot(x_pred2, y_pred2, 'g')

    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    fig.savefig('sea_level_plot.png')
    return fig
