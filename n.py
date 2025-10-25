import newspaper
import feedparser
import csv
from datetime import datetime

def scrape_news_from_feed(feed_url):
    articles = []
    feed = feedparser.parse(feed_url)

    for entry in feed.entries:
        print(f"Processing: {entry.link}")
        article = newspaper.Article(entry.link)

        try:
            article.download()
            article.parse()
            articles.append({
                'title': article.title,
                'author': ', '.join(article.authors),
                'publish_date': article.publish_date if article.publish_date else '',
                'content': article.text,
                'url': entry.link
            })
        except Exception as e:
            print(f"⚠️ Error processing {entry.link}: {e}")
            continue

    return articles


def save_to_csv(articles, filename='news_articles.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'author', 'publish_date', 'content', 'url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for article in articles:
            writer.writerow(article)

    print(f"\n✅ Saved {len(articles)} articles to '{filename}'")


# MAIN PROGRAM
if __name__ == "__main__":
    feed_url = 'https://feeds.bbci.co.uk/news/rss.xml'
    print("📰 Starting News Scraper...")
    articles = scrape_news_from_feed(feed_url)
    save_to_csv(articles)
