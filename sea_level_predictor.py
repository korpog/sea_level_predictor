import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot

    df_2000 = df[df['Year'] >= 2000]
    year_range = range(1880, 2051)
    year_range2000 = range(2000, 2051)

    lr = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    lr2 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])

    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    plt.plot(year_range, lr.slope * year_range +
             lr.intercept, 'r', label='Linear regression')

    # Create second line of best fit
    plt.plot(year_range2000, lr2.slope * year_range2000 +
             lr2.intercept, 'g', label='Linear regression')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
