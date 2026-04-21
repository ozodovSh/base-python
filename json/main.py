import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

try:
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        with open("posts.json", "w", encoding="utf-8") as file:
            json.dump(posts, file, indent=4, ensure_ascii=False)

        print("Ma'lumotlar posts.json fayliga muvaffaqiyatli yozildi!")

    else:
        print(f"Xatolik yuz berdi: {response.status_code}")

except Exception as e:
    print(f"Xatolik: {e}")