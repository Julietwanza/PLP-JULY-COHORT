""" 
Iris Dataset Analysis Project

Tasks:
1. Load and Explore the Dataset
2. Basic Data Analysis
3. Data Visualization
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# ===============================
# Task 1: Load and Explore Dataset
# ===============================

try:
    iris_data = load_iris(as_frame=True)
    df = iris_data.frame
except FileNotFoundError:
    print("Dataset file not found!")

# Display first few rows
print("First 5 rows:")
print(df.head())

# Inspect dataset
print("\nDataset info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# Clean dataset
df = df.dropna()

# ===============================
# Task 2: Basic Data Analysis
# ===============================

print("\nBasic statistics:")
print(df.describe())

grouped = df.groupby("target").mean()
print("\nGrouped means (by target):")
print(grouped)

# Add species names
df["species"] = df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})

print("\nObservations:")
print("- Setosa has the smallest petal length and width.")
print("- Virginica has the largest sepal and petal dimensions.")
print("- Versicolor is intermediate between Setosa and Virginica.")

# ===============================
# Task 3: Data Visualization
# ===============================

sns.set(style="whitegrid")

# 1. Line chart – sepal length across samples
plt.figure(figsize=(10,5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.title("Sepal Length Trend Across Samples")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart – average petal length per species
plt.figure(figsize=(8,5))
sns.barplot(x="species", y="petal length (cm)", data=df, ci=None, palette="viridis")
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram – sepal width distribution
plt.figure(figsize=(8,5))
plt.hist(df["sepal width (cm)"], bins=20, color="skyblue", edgecolor="black")
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot – sepal length vs petal length
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, palette="deep")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
