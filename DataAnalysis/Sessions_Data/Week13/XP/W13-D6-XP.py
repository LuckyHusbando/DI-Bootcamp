#Exercise 1

from urllib.request import urlopen
from bs4 import BeautifulSoup

# 1. Define the URL
url_to_scrape = 'https://www.scrapethissite.com/pages/simple/'

try:
    # 2. Use urlopen() to fetch the HTML content
    print(f"Fetching content from: {url_to_scrape}")
    html = urlopen(url_to_scrape)
    
    # Read the HTML content
    html_content = html.read()
    
    # 3. Create a BeautifulSoup object to parse the HTML
    # We use 'html.parser' for the parsing engine
    soup = BeautifulSoup(html_content, 'html.parser')
    
    print("-" * 30)

    # 4. Find the title of the webpage
    title_tag = soup.find('title')
    webpage_title = title_tag.text if title_tag else "Title not found"
    print(f"✅ Webpage Title: **{webpage_title}**")
    
    print("-" * 30)

    # 5. Extract all paragraphs (<p> tags)
    all_paragraphs = soup.find_all('p')
    print(f"✅ Found **{len(all_paragraphs)}** paragraph(s) (<p> tag):")
    for i, p in enumerate(all_paragraphs[:5]):  # Print first 5 for brevity
        print(f"   [{i+1}] {p.text.strip()[:70]}...")

    print("-" * 30)

    # 6. Retrieve all links (URLs in <a href=""> tags)
    all_links = soup.find_all('a', href=True)
    print(f"✅ Found **{len(all_links)}** link(s) (URLs in <a> tags):")
    for i, link in enumerate(all_links[:5]):  # Print first 5 for brevity
        href = link['href']
        text = link.text.strip()
        print(f"   [{i+1}] URL: **{href}** | Text: {text}")

except Exception as e:
    print(f"An error occurred: {e}")

#Exercise 2

from urllib.request import urlopen
from urllib.error import URLError, HTTPError

# Define the URL for Wikipedia's robots.txt
ROBOTS_TXT_URL = 'https://www.wikipedia.org/robots.txt'

def get_robots_txt(url):
    """
    Downloads and prints the content of a robots.txt file from the specified URL.
    """
    print(f"Attempting to download robots.txt from: {url}\n")
    
    try:
        # 1. Open the URL and send the request
        with urlopen(url) as response:
            
            # Check for a successful HTTP status code (200 is typical for success)
            if response.getcode() == 200:
                print("✅ Successfully downloaded robots.txt (HTTP 200 OK).\n")
                
                # 2. Read the content (it's typically text)
                robots_content = response.read().decode('utf-8')
                
                # 3. Display the content
                print("-" * 50)
                print("         WIKIPEDIA ROBOTS.TXT CONTENT         ")
                print("-" * 50)
                print(robots_content)
                print("-" * 50)
            else:
                print(f"❌ Failed to download robots.txt. HTTP Status Code: {response.getcode()}")
                
    except HTTPError as e:
        # Handles errors like 404 (Not Found) or 403 (Forbidden)
        print(f"❌ HTTP Error: Could not retrieve the file. Status code: {e.code} - {e.reason}")
    except URLError as e:
        # Handles errors like a bad domain name or network issues
        print(f"❌ URL Error: Could not connect or resolve the domain. Reason: {e.reason}")
    except Exception as e:
        # Catch any other unexpected errors
        print(f"❌ An unexpected error occurred: {e}")

# Execute the function
get_robots_txt(ROBOTS_TXT_URL)

#Exercise 3

from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

# Define the URL for the English Wikipedia Main Page
WIKIPEDIA_URL = 'https://en.wikipedia.org/wiki/Main_Page'

def extract_headers(url):
    """
    Fetches a webpage, parses it, and extracts all HTML header tags (h1 to h6).
    """
    print(f"Fetching content from: {url}\n")
    
    try:
        # 1. Fetch the HTML content
        with urlopen(url) as response:
            html_content = response.read()
        
        # 2. Create a BeautifulSoup object to parse the HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 3. Find all header tags: h1, h2, h3, h4, h5, h6
        # find_all accepts a list of tag names
        header_tags = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        
        print("-" * 50)
        print(f"✅ Found **{len(header_tags)}** total header tags on the page.")
        print("-" * 50)
        
        # 4. Extract and display the text content
        for header in header_tags:
            # header.name gives the tag name (e.g., 'h1', 'h2')
            # header.text.strip() gets the clean text content
            level = header.name
            text = header.text.strip()
            
            # Print with indentation based on header level for readability
            indentation = '  ' * (int(level[1]) - 1)
            print(f"{indentation}{level.upper()}: **{text}**")

        print("-" * 50)

    except HTTPError as e:
        print(f"❌ HTTP Error: Could not retrieve the page. Status code: {e.code}")
    except URLError as e:
        print(f"❌ URL Error: Could not connect or resolve the domain. Reason: {e.reason}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Execute the function
extract_headers(WIKIPEDIA_URL)

#Exercise 4

from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

# Define the URL to check
TARGET_URL = 'https://www.scrapethissite.com/pages/simple/' 

def check_for_title(url):
    """
    Fetches a webpage and checks if a <title> tag exists.
    """
    print(f"Checking URL for <title> tag: {url}\n")
    
    try:
        # 1. Fetch the HTML content
        with urlopen(url) as response:
            html_content = response.read()
        
        # 2. Create a BeautifulSoup object
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 3. Search for the <title> tag
        # The .find() method returns the first matching tag or None if not found.
        title_tag = soup.find('title')
        
        # 4. Determine and display the result
        print("-" * 40)
        if title_tag:
            title_text = title_tag.text.strip()
            print(f"✅ Success! The page **contains a title**.")
            print(f"   Title Content: **{title_text}**")
        else:
            print("❌ Failure. The page **does not contain a <title> tag**.")
        print("-" * 40)

    except HTTPError as e:
        print(f"❌ HTTP Error: Could not retrieve the page. Status code: {e.code}")
    except URLError as e:
        print(f"❌ URL Error: Could not connect or resolve the domain. Reason: {e.reason}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Execute the function
check_for_title(TARGET_URL)

#Exercise 5

import feedparser
import datetime
import calendar
from urllib.error import URLError

# The official RSS feed URL for CISA NCAS Alerts (formerly US-CERT)
CISA_ALERTS_RSS_URL = 'https://us-cert.cisa.gov/ncas/alerts.xml'

def count_cisa_alerts_current_year(rss_url):
    """
    Downloads the CISA Alerts RSS feed and counts the entries published 
    in the current calendar year.
    """
    current_year = datetime.datetime.now().year
    alert_count = 0
    
    print(f"Counting CISA Security Alerts for the year **{current_year}**...")
    print("-" * 50)
    
    try:
        # 1. Parse the RSS feed
        feed = feedparser.parse(rss_url)

        if feed.status != 200:
            print(f"❌ Error fetching feed: HTTP Status Code {feed.status}")
            return

        # 2. Iterate through each entry (alert) in the feed
        for entry in feed.entries:
            # Check if the entry has a 'published_parsed' field
            if hasattr(entry, 'published_parsed'):
                # Convert the parsed date tuple to a datetime object
                published_date = datetime.datetime(*entry.published_parsed[:6])
                
                # 3. Check if the alert's publication year matches the current year
                if published_date.year == current_year:
                    alert_count += 1
                    # Optional: Print the title of the alert
                    print(f"   [Alert] {published_date.strftime('%Y-%m-%d')}: {entry.title}")

        print("-" * 50)
        print(f"🎉 Total CISA/US-CERT Security Alerts issued in {current_year}: **{alert_count}**")

    except URLError as e:
        print(f"❌ Network Error: Could not connect to the RSS feed URL. Reason: {e.reason}")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Execute the function
count_cisa_alerts_current_year(CISA_ALERTS_RSS_URL)

#Exercise 6

import requests
from bs4 import BeautifulSoup
import random
from typing import List, Dict

# The URL for IMDb's Top 250 Movies list
IMDB_URL = 'https://www.imdb.com/chart/top'

def get_random_movies(url: str, count: int = 10) -> List[Dict]:
    """
    Scrapes a movie list page, extracts movie details, and returns 
    a random selection of 'count' movies.
    """
    print(f"Fetching data from: {url}")
    
    # Use a User-Agent header to mimic a web browser and avoid being blocked
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching URL: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    all_movies = []

    # Target the main container for all movie list items
    # Note: IMDb's HTML structure can change, making CSS selectors critical.
    # The structure below is for a typical IMDb list page.
    movie_list_items = soup.find_all('li', class_='ipc-metadata-list-summary-item')

    if not movie_list_items:
        print("❌ Could not find movie list items on the page. The website structure may have changed.")
        return []

    for item in movie_list_items:
        try:
            # 1. Movie Name (Title)
            title_tag = item.find('h3', class_='ipc-title__text')
            movie_name = title_tag.text.split('.', 1)[-1].strip() if title_tag else 'N/A'

            # 2. Year
            # The year and other details are often grouped in a span
            details_spans = item.find_all('span', class_='cli-title-metadata-item')
            movie_year = details_spans[0].text.strip() if details_spans else 'N/A'

            # 3. Brief Summary (Plot Summary)
            # A brief summary isn't available on the main list page, only on the movie's detail page.
            # We'll use a placeholder since fetching 250 detail pages is complex and slow.
            summary = "Summary not available on the list page. Check the movie's detail page."
            
            all_movies.append({
                'name': movie_name,
                'year': movie_year,
                'summary': summary
            })

        except Exception as e:
            # Skip any malformed entries
            # print(f"Warning: Skipped one entry due to error: {e}")
            continue

    # 4. Select a random sample
    if len(all_movies) < count:
        print(f"Warning: Only found {len(all_movies)} movies, returning all of them.")
        random_selection = all_movies
    else:
        random_selection = random.sample(all_movies, count)
        
    return random_selection

# --- Main Execution ---
TARGET_COUNT = 10
random_movies = get_random_movies(IMDB_URL, TARGET_COUNT)

print("\n" + "=" * 50)
print(f"       🎥 Top {TARGET_COUNT} Random Movies from IMDb List       ")
print("=" * 50)

if random_movies:
    for i, movie in enumerate(random_movies):
        print(f"\n**{i+1}. {movie['name']}** ({movie['year']})")
        print(f"   Summary: {movie['summary']}")
else:
    print("No movies were extracted.")

print("\n" + "=" * 50)