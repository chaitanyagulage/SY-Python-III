import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    'Age': [24, 27, 22, 32, 29, 25, 30],
    'Salary': [50000, 60000, 52000, 58000, 62000, 55000, 60000]
}

df = pd.DataFrame(data)

# Display dataset
print("Dataset:")
print(df)

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

print("\nMean:", df['Age'].mean())
print("Median:", df['Age'].median())
print("Mode:", df['Age'].mode()[0])
print("Standard Deviation:", df['Age'].std())
print("Variance:", df['Age'].var())
print("Minimum:", df['Age'].min())
print("Maximum:", df['Age'].max())
print("Quantiles:", df['Age'].quantile([0.25, 0.5, 0.75]))

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())

print("\nData after handling missing values:")
print(df)

# Detect outliers using IQR
Q1 = df['Salary'].quantile(0.25)
Q3 = df['Salary'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df['Salary'] < lower) | (df['Salary'] > upper)]

print("\nOutliers:")
print(outliers)

# Visualization and Plotting

# Histogram
plt.figure(figsize=(6, 4))
sns.histplot(df['Age'], bins=5, kde=True)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Boxplot
plt.figure(figsize=(6, 4))
sns.boxplot(x=df['Salary'])
plt.title("Salary Boxplot")
plt.show()

# Scatter plot
plt.figure(figsize=(6, 4))
sns.scatterplot(x='Age', y='Salary', data=df)
plt.title("Age vs Salary")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

print("\nEDA Completed Successfully!")
