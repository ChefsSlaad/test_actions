import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone

def get_first_headline():
    url = "https://www.nu.nl/"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    headline_tag = soup.find("h3")  # may need adjustment depending on site structure
    if headline_tag:
        return headline_tag.get_text(strip=True)
    return None

def append_headline_to_file(filename, headline):
    # Current UTC timestamp in yyyy-mm-dd hh:mm:ss
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    line = f"{timestamp} {headline}\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(line)

def main():
    headline = get_first_headline()
    if headline:
        print("First headline:", headline)
        append_headline_to_file("first_headline.txt", headline)
    else:
        print("Could not find a headline on nu.nl")

if __name__ == "__main__":
    main()
