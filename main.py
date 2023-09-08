import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f():
    df=pd.read_csv("https://data.wa.gov/api/views/f6w7-q2d2/rows.csv")

    print(df.shape)
    print(df.shape[0])
    print(df.describe())

    # Bottom 3 2020 Census Tract
    print(df.sort_values('2020 Census Tract', ascending = True)[:3])
    # Calculate the median for the 2022 numbers
    np.median(df['2020 Census Tract'].dropna())

    # Plot a histogram for the 2022 numbers
    data = df['2020 Census Tract'].dropna()

    # Create histogram
    plt.hist(data, bins=5, edgecolor="k")

    # Add labels and title
    plt.xlabel('Census Tract')
    plt.ylabel('Frequency')
    plt.title('Histogram of 2020 Census Tract')

    # Show plot
    plt.show()
