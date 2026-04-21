import requests
from bs4 import BeautifulSoup

URL = "https://upg.uz/uz/"

def get_categories():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    categories = []

    items = soup.find_all("div")

    for item in items:
        text = item.get_text(strip=True)

        if text in [
            "Klaviaturalar", "Sichqoncha", "Monitorlar",
            "Naushniklar", "Mikrofonlar", "Gamepad"
        ]:
            categories.append(text)

    return list(set(categories))


if __name__ == "__main__":
    print(get_categories())