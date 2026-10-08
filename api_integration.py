import requests


API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_posts():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()

        posts = response.json()

        print("API Integration Project Started!")
        print(f"Total posts received: {len(posts)}")

        for post in posts[:5]:
            print("\nPost ID:", post["id"])
            print("Title:", post["title"])
            print("Body:", post["body"])

    except requests.exceptions.RequestException as error:
        print("Error while connecting to the API:", error)


if __name__ == "__main__":
    fetch_posts()