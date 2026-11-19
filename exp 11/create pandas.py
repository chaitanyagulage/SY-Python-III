import numpy as np
import pandas as pd

# Example using NumPy to generate 10 random numbers
random_ser = pd.Series(np.random.rand(10))
print("Random Series:\n", random_ser)
# Create a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [24, 27, 22]}
df = pd.DataFrame(data)
print("\nDataFrame from Dictionary:\n", df)

# Create a DataFrame from a list of dictionaries
data_list = [
    {'Name': 'Alice', 'Age': 24, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 27, 'City': 'Los Angeles'},
]
df_list = pd.DataFrame(data_list)
print("\nDataFrame from List of Dictionaries:\n", df_list)

# Create a Series from a list
ser = pd.Series([10, 20, 30, 40, 50])

# Create a Series with a custom index
ser_custom = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
print("\nSeries with Custom Index:\n", ser_custom)