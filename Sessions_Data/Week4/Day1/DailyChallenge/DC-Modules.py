import requests
import time

def get_page_load_time(url):
    """
    Measures the time it takes for a webpage to load and returns the duration.

    Args:
        url (str): The URL of the webpage to test.

    Returns:
        float or None: The time in seconds it took to load the page, or None if an error occurred.
    """
    try:
        start_time = time.time()
        response = requests.get(url, timeout=10) # Set a timeout to prevent indefinite waiting
        end_time = time.time()
        response.raise_for_status() # Raises an exception for bad status codes (4xx or 5xx)
        load_time = end_time - start_time
        return load_time
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while loading {url}: {e}")
        return None

if __name__ == "__main__":
    sites = [
        "https://www.google.com",
        "https://www.ynet.co.il",
        "https://www.imdb.com",
        "https://www.wikipedia.org",
        "https://www.github.com"
    ]

    print("Measuring page load times:\n")
    for site in sites:
        load_time = get_page_load_time(site)
        if load_time is not None:
            print(f"The webpage {site} took {load_time:.4f} seconds to load.")
