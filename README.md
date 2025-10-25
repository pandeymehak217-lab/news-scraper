
# 📰 News Scraper with Python

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)

A Python project that scrapes news articles from RSS feeds using `feedparser` and `newspaper3k`.  
It downloads and parses articles, then saves them into a CSV file for easy analysis.

---

## 📌 Project Overview

This project demonstrates:

- How to parse RSS feeds to discover news articles  
- How to extract article title, author, publish date, and full text  
- How to handle errors or broken links gracefully  
- Saving structured data into a CSV file (`news_articles.csv`) for further analysis  

It’s ideal for building a custom news aggregator or conducting media analysis.

---

## ⚙️ Requirements

- **Python 3.x**  
- **feedparser**  
- **newspaper3k**  

Install dependencies using pip:

```bash
pip install feedparser newspaper3k
🛠️ Setup & Usage
Clone the repository:
git clone https://github.com/pandeymehak217-lab/news-scraper.git
cd news-scraper
Run the script:
python n.py
The script will:
Fetch RSS feeds from predefined sources
Extract article details (title, author, publish date, content)
Save the data into news_articles.csv
📂 Repository Structure
news-scraper/
├─ n.py              # Main script to scrape and save news articles
├─ news_articles.csv # Output file containing scraped articles
├─ README.md         # Project documentation
🔗 About
This project showcases the use of Python for web scraping and data extraction.
By leveraging libraries like feedparser and newspaper3k, it automates the process of gathering and storing news articles from various RSS feeds.
