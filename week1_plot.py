import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset as pandas dataframe
df_teeth = pd.read_csv("mammal_teeth.csv")

plt.figure(figsize=(5, 10))  # set figure size
plt.scatter(
    x=df_teeth['Top incisors'],
    y=df_teeth['MAMMAL']
)  # set figure x, y axis
plt.gca().xaxis.set_visible(False)

# Change the title name to include your name
plt.title("Plot for mammal_teeth dataset - Sara Bawany")

# Save the figure
plt.savefig("mammal_teeth_scatterplot.png", dpi=150)
