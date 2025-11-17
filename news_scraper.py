import requests
from bs4 import BeautifulSoup

# Set the target URL (example: BBC News)
URL = "https://www.bbc.com/news"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def fetch_headlines(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")
    # Find all h3 and h2 tags (common for headlines)
    headlines = []
    for tag in soup.find_all(['h3', 'h2']):
        title = tag.get_text(strip=True)
        if len(title) > 10:  # Filter out very short or meaningless lines
            headlines.append(title)
    return headlines

if __name__ == "__main__":
    headlines = fetch_headlines(URL)
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for line in headlines:
            file.write(line + "\n")
    print("Headlines saved to headlines.txt")
print("Headlines scraped:")
for h in headlines:
    print(h)
