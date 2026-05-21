import csv
from datetime import datetime
import feedparser


SOURCES = {
    'Corriere della Sera' : 'https://xml2.corriereobjects.it/rss/homepage.xml',
    'La Repubblica' : 'https://www.repubblica.it/rss/homepage/rss2.0.xml',
    'Il Messaggero' : 'https://www.ilmessaggero.it/rss/home.xml'
}

OUTPUT_FILE = f"dataset_{datetime.now().strftime('%Y-%m-%d')}.csv"


def download_titles():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_data = []

    for newspaper, url_rss in SOURCES.items():
        try:
            feed = feedparser.parse(url_rss)

            for entry in feed.entries[:10]:
                title = entry.title.replace("\n", " ").strip()
                new_data.append([current_datetime, newspaper, title])

        except Exception as e:
            print(f"Error while downloading from {newspaper}: {e}")


    with open(OUTPUT_FILE, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Newspaper", "Title"])
        writer.writerows(new_data)

    print(f"[{current_datetime}] Collection completed!")


if __name__ == "__main__":
    download_titles()

