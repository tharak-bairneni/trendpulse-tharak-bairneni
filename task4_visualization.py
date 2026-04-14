import pandas as pd
import matplotlib.pyplot as plt
import os

# ==============================
# STEP 1 — Load Data & Setup
# ==============================

file = "data/trends_analysed.csv"

if not os.path.exists(file):
    print("❌ File not found. Run Task 3 first.")
    exit()

df = pd.read_csv(file)

# Create outputs folder
os.makedirs("outputs", exist_ok=True)

# ==============================
# STEP 2 — Chart 1: Top 10 Stories by Score
# ==============================

# Get top 10
top10 = df.sort_values("score", ascending=False).head(10)

# Shorten long titles
top10["short_title"] = top10["title"].apply(lambda x: x[:50] + "..." if len(x) > 50 else x)

plt.figure(figsize=(10, 6))
plt.barh(top10["short_title"], top10["score"])
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()

plt.savefig("outputs/chart1_top_stories.png")
plt.show()
plt.close()

# ==============================
# STEP 3 — Chart 2: Stories per Category
# ==============================

category_counts = df["category"].value_counts()

plt.figure(figsize=(8, 5))
plt.bar(category_counts.index, category_counts.values,
        color=["blue", "green", "red", "purple", "orange"])
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.savefig("outputs/chart2_categories.png")
plt.show()
plt.close()

# ==============================
# STEP 4 — Chart 3: Score vs Comments
# ==============================

plt.figure(figsize=(8, 5))

# Separate popular vs not
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.scatter(popular["score"], popular["num_comments"], label="Popular", alpha=0.7)
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular", alpha=0.7)

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()

plt.savefig("outputs/chart3_scatter.png")
plt.show()
plt.close()

# ==============================
# BONUS — Dashboard
# ==============================

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Chart 1
axes[0].barh(top10["short_title"], top10["score"])
axes[0].set_title("Top 10 Stories")
axes[0].set_xlabel("Score")

# Chart 2
axes[1].bar(category_counts.index, category_counts.values)
axes[1].set_title("Stories per Category")
axes[1].set_xlabel("Category")

# Chart 3
axes[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axes[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axes[2].set_title("Score vs Comments")
axes[2].set_xlabel("Score")
axes[2].legend()

plt.suptitle("TrendPulse Dashboard")

plt.savefig("outputs/dashboard.png")
plt.show()
plt.close()

print("✅ All charts saved in outputs/")