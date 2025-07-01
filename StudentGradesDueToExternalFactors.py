# 📊 Student Performance Analysis (UCI Dataset)
# Goal: Analyze how personal, social, and familial factors influence academic grades

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load and clean data
df = pd.read_csv("student-mat.csv", sep=";")

# Check for missing values
print("Missing Values:\n", df.isnull().sum())

# Rename and transform columns for readability
df["gender"] = df["sex"]
df["Pstatus"] = np.where(df["Pstatus"] == "T", "Together", "Divorced")
df["internet"] = df["internet"].map({"yes": "Has Internet", "no": "Has no Internet"})
df["famrel"] = df["famrel"].map({
    1: "Very bad",
    2: "Pretty bad",
    3: "Normal/Distant",
    4: "Good",
    5: "Satisfactory/Good"
})
df["studytimestring"] = df["studytime"].map({1: "< 2", 2: "2 - 5", 3: "5 - 10", 4: ">=10"})
df["Drinks Alcohol"] = df["Dalc"]
df["Drinks Alcohol (weekends)"] = df["Walc"]

# 2. Create subplot grid
fig, axs = plt.subplots(2, 3, figsize=(14, 10))

# --- PARENT STATUS ---
axs[0, 0].set_title("Parent Status vs Grade by Gender")
axs[0, 0].set_xlabel("Parent Status")
axs[0, 0].set_ylabel("Final Grade (G3)")
sns.barplot(
    data=df,
    x="Pstatus",
    y="G3",
    hue="gender",
    ax=axs[0, 0],
    order=["Together", "Divorced"],
    hue_order=["M", "F"],
    palette=["#1dbade", "#e610d7", "#3b66a3", "#992391"]
)

# --- PAST FAILURES ---
axs[0, 1].set_title("Past Failures vs Grade")
axs[0, 1].set_xlabel("Failures")
axs[0, 1].set_ylabel("Final Grade (G3)")
sns.barplot(
    data=df,
    x="failures",
    y="G3",
    ax=axs[0, 1],
    palette=["#ff0015", "#c71625", "#8c1d27", "#781e25"]
)

# --- STUDY TIME ---
axs[0, 2].set_title("Study Time vs Grade")
axs[0, 2].set_xlabel("Study Time (hrs/week)")
axs[0, 2].set_ylabel("Final Grade (G3)")
sns.boxplot(
    data=df,
    x="studytimestring",
    y="G3",
    ax=axs[0, 2],
    order=["< 2", "2 - 5", "5 - 10", ">=10"],
    color="#73fff1"
)

# --- INTERNET ACCESS ---
axs[1, 0].set_title("Internet Access vs Grade")
axs[1, 0].set_xlabel("Internet Access")
axs[1, 0].set_ylabel("Final Grade (G3)")
sns.barplot(data=df, x="internet", y="G3", ax=axs[1, 0], color="#1bd15e")

# --- FAMILY RELATIONSHIP ---
axs[1, 1].set_title("Family Relationship vs Grade by Gender")
axs[1, 1].set_xlabel("Family Relationship Quality")
axs[1, 1].set_ylabel("Final Grade (G3)")
sns.barplot(
    data=df,
    x="famrel",
    y="G3",
    hue="gender",
    ax=axs[1, 1],
    order=["Very bad", "Pretty bad", "Normal/Distant", "Good", "Satisfactory/Good"],
    hue_order=["M", "F"],
    palette=["#1dbade", "#e610d7"] * 5
)

# --- HEATMAP OF CORRELATIONS ---
axs[1, 2].set_title("Correlation Heatmap")
corr_cols = ["G1", "G2", "G3", "studytime", "failures", "absences", "Drinks Alcohol", "Drinks Alcohol (weekends)"]
sns.heatmap(df[corr_cols].corr(), annot=True, cmap="YlGnBu", ax=axs[1, 2])

# Final layout
plt.tight_layout()
plt.show()
