import requests
import json

api_key = "YOUR API KEY"
def scrape_google_images(query, num_images=50):
    # Send a request to SerpApi
    search_url = "https://serpapi.com/search.json"
    params = {
        "q": query,
        "tbm": "isch",
        "ijn": 0,
        "api_key": api_key
    }

    try:
        response = requests.get(search_url, params=params, timeout=10)
        response.raise_for_status()
        search_results = response.json()

        # Extract the image URLs from the search results
        image_urls = [result["original"] for result in search_results["images_results"][:num_images]]
        return image_urls

    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
        print(f"No or bad internet connection")
        return None
