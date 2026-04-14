import pandas as pd
import json
import os
import glob

# ==============================
# STEP 1 — Load JSON File
# ==============================

# Find latest JSON file automatically
json_files = glob.glob("data/trends_*.json")

if not json_files:
    print("❌ No JSON file found. Run Task 1 first.")
    exit()

latest_file = sorted(json_files)[-1]

# Load JSON
with open(latest_file, "r", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data)

print(f"Loaded {len(df)} stories from {latest_file}")

# ==============================
# STEP 2 — Clean the Data
# ==============================

# Remove duplicates based on post_id
before = len(df)
df = df.drop_duplicates(subset=["post_id"])
print(f"\nAfter removing duplicates: {len(df)}")

# Drop rows with missing essential values
before = len(df)
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# Convert score and num_comments to integers
df["score"] = pd.to_numeric(df["score"], errors="coerce").fillna(0).astype(int)
df["num_comments"] = pd.to_numeric(df["num_comments"], errors="coerce").fillna(0).astype(int)

# Remove low-quality stories (score < 5)
before = len(df)
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# Strip whitespace from title
df["title"] = df["title"].str.strip()

# ==============================
# STEP 3 — Save as CSV
# ==============================

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

csv_file = "data/trends_clean.csv"
df.to_csv(csv_file, index=False)

print(f"\nSaved {len(df)} rows to {csv_file}")

# ==============================
# SUMMARY — Stories per Category
# ==============================

print("\nStories per category:")
print(df["category"].value_counts())