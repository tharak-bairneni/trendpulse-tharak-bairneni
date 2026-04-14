# trendpulse-tharak-bairneni
# TrendPulse: What's Actually Trending Right Now

TrendPulse is an end-to-end data pipeline that collects trending stories from the HackerNews API, cleans and processes the data, performs analysis using Pandas and NumPy, and visualizes insights using Matplotlib.

## Pipeline Overview
Task 1 — Fetch trending stories from HackerNews and save as JSON  
Task 2 — Clean and process data, remove duplicates and missing values, save as CSV  
Task 3 — Perform analysis, compute statistics, and add new features  
Task 4 — Create visualizations and a dashboard using Matplotlib  

## Project Structure
trendpulse/
- task1_data_collection.py  
- task2_data_processing.py  
- task3_analysis.py  
- task4_visualization.py  
- data/ (stores JSON and CSV files)  
- outputs/ (stores charts and dashboard images)  

## Technologies Used
Python, Requests, Pandas, NumPy, Matplotlib  

## How to Run
Run the scripts in order:
python task1_data_collection.py  
python task2_data_processing.py  
python task3_analysis.py  
python task4_visualization.py  

## Output
- JSON file with raw data  
- Cleaned CSV file  
- Analysed CSV file  
- Charts and dashboard images  

## Key Insights
Technology and science topics appear frequently in trending stories.  
Stories with higher scores tend to receive more comments.  
Engagement varies across categories.

## Conclusion
This project demonstrates a complete data pipeline from data collection to visualization, turning raw API data into meaningful insights.