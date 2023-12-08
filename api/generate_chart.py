import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

plt.switch_backend('Agg')

df = pd.read_csv("api/static/EDGA_dataset.csv")
indexForCountry = dict(zip(list(df["Country"]), list(df.index)))

def getPayeChart(name):
    x = df.iloc[indexForCountry[name]].values[1:]
    plt.figure(figsize=(10, 6))
    plt.plot(x.T)

    # Adding labels and title
    plt.title('Scatter Plot with Trend Line - Temperature by Year')
    plt.xlabel('Year')
    plt.ylabel('Temperature (°C)')

    # Display the legend
    plt.legend()
    plt.grid(True)

    # Save the plot as a BytesIO object
    img_stream = BytesIO()
    plt.savefig(img_stream, format='jpg')
    img_stream.seek(0)

    # You can return the BytesIO object directly
    return img_stream
