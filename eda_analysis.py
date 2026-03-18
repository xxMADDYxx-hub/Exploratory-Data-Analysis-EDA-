import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# 1. LOAD DATASET
# -----------------------------
file_path = "data.csv"  # Make sure this file exists in your project folder

try:
    df = pd.read_csv(file_path)
    print("✅ Dataset loaded successfully!\n")
except FileNotFoundError:
    print("❌ Error: data.csv not found. Place it in the project folder.")
    exit()

# -----------------------------
# 2. BASIC DATA OVERVIEW
# -----------------------------
print("🔹 First 5 Rows:")
print(df.head())

print("\n🔹 Dataset Info:")
print(df.info())

print("\n🔹 Summary Statistics:")
print(df.describe())

# -----------------------------
# 3. CHECK MISSING VALUES
# -----------------------------
print("\n🔹 Missing Values:")
print(df.isnull().sum())

# -----------------------------
# 4. CORRELATION HEATMAP
# -----------------------------
numeric_df = df.select_dtypes(include=['number'])

if not numeric_df.empty:
    plt.figure(figsize=(8, 6))
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()
else:
    print("⚠ No numeric columns found for correlation.")

# -----------------------------
# 5. DISTRIBUTION PLOT
# -----------------------------
if not numeric_df.empty:
    col = numeric_df.columns[0]

    plt.figure(figsize=(6, 4))
    sns.histplot(df[col], kde=True)
    plt.title(f"Distribution of {col}")
    plt.show()

# -----------------------------
# 6. SCATTER PLOT (if possible)
# -----------------------------
if len(numeric_df.columns) >= 2:
    col1, col2 = numeric_df.columns[:2]

    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=df[col1], y=df[col2])
    plt.title(f"{col1} vs {col2}")
    plt.show()
else:
    print("⚠ Not enough numeric columns for scatter plot.")