import requests
import json
import time
import os
from datetime import datetime

# Base URLs
TOP_STORIES_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

# Header (required)
headers = {"User-Agent": "TrendPulse/1.0"}

# Category keywords
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}

# Store collected data
collected_data = []

# Step 1 — Fetch top story IDs
try:
    response = requests.get(TOP_STORIES_URL, headers=headers)
    story_ids = response.json()[:500]
except Exception as e:
    print("Failed to fetch top stories:", e)
    story_ids = []

# Function to classify category
def get_category(title):
    """Assign category based on keywords"""
    title_lower = title.lower()
    for category, keywords in categories.items():
        for word in keywords:
            if word in title_lower:
                return category
    return None

# Track count per category
category_counts = {cat: 0 for cat in categories}

# Step 2 — Fetch each story
for category in categories:
    print(f"\nProcessing category: {category}")
    
    for story_id in story_ids:
        # Stop if we reached 25 for this category
        if category_counts[category] >= 25:
            break
        
        try:
            res = requests.get(ITEM_URL.format(story_id), headers=headers)
            
            if res.status_code != 200:
                print(f"Failed to fetch story {story_id}")
                continue
            
            story = res.json()
            
            # Skip if no title
            if not story or "title" not in story:
                continue
            
            assigned_category = get_category(story["title"])
            
            # Check if it belongs to current category
            if assigned_category == category:
                collected_data.append({
                    "post_id": story.get("id"),
                    "title": story.get("title"),
                    "category": category,
                    "score": story.get("score", 0),
                    "num_comments": story.get("descendants", 0),
                    "author": story.get("by", "unknown"),
                    "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                
                category_counts[category] += 1
        
        except Exception as e:
            print(f"Error fetching story {story_id}: {e}")
            continue
    
    # Wait 2 seconds after each category
    time.sleep(2)

# Step 3 — Save to JSON

# Create folder if not exists
os.makedirs("data", exist_ok=True)

# File name with date
file_name = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"

# Save file
with open(file_name, "w", encoding="utf-8") as f:
    json.dump(collected_data, f, indent=4)

# Final output
print(f"\nCollected {len(collected_data)} stories.")
print(f"Saved to {file_name}")