#XP Gold

#Exercise 1 - Restaurant Menu Manager

#See three "menu" files - restaurant_menu.json, menu_manager.py, and menu_editor.py

#Exercise 2 - Giphy

# import requests
# import json

# # API key and search parameters
# api_key = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
# query = "hilarious"
# rating = "g"
# limit = 10

# # Use an f-string to build the URL with variables
# url = f"https://api.giphy.com/v1/gifs/search?q={query}&rating={rating}&api_key={api_key}&limit={limit}"

# try:
#     response = requests.get(url)
    
#     # Check if the status code is 200
#     if response.status_code == 200:
#         json_data = response.json()
        
#         # Filter for gifs with height > 100
#         filtered_gifs = [
#             gif for gif in json_data["data"] 
#             if int(gif["images"]["original"]["height"]) > 100
#         ]
        
#         # Return the length of the filtered object
#         print(f"Number of gifs with height > 100: {len(filtered_gifs)}")
        
#         # Return the first 10 gifs (already handled by the 'limit' parameter in the URL)
#         print("\nFirst 10 gifs returned:")
#         for gif in filtered_gifs:
#             print(f"- {gif['title']} (Height: {gif['images']['original']['height']})")

#     else:
#         print(f"Error: Received status code {response.status_code}")
        
# except requests.exceptions.RequestException as e:
#     print(f"An error occurred: {e}")

#Exercise 3 - Giphy #2

# import requests
# import json

# # Your GIPHY API key
# API_KEY = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
# SEARCH_URL = "https://api.giphy.com/v1/gifs/search"
# TRENDING_URL = "https://api.giphy.com/v1/gifs/trending"

# def get_gifs(search_term):
#     """
#     Fetches gifs based on a search term. If no gifs are found, it fetches trending gifs.
#     """
#     # Parameters for the API request
#     params = {
#         'api_key': API_KEY,
#         'q': search_term,
#         'limit': 10  # Limit to 10 results for a cleaner output
#     }
    
#     # Make the search request
#     response = requests.get(SEARCH_URL, params=params)
    
#     if response.status_code == 200:
#         data = response.json().get('data', [])
        
#         # Check if the search returned any results
#         if data:
#             print(f"\nHere are some gifs for '{search_term}':")
#             return data
#         else:
#             # If no results, fetch trending gifs
#             print(f"\nCould not find any gifs for '{search_term}'. Showing trending gifs instead:")
#             return get_trending_gifs()
#     else:
#         print(f"Error fetching data: {response.status_code}")
#         return None

# def get_trending_gifs():
#     """
#     Fetches the trending gifs of the day.
#     """
#     params = {
#         'api_key': API_KEY,
#         'limit': 10
#     }
    
#     response = requests.get(TRENDING_URL, params=params)
    
#     if response.status_code == 200:
#         return response.json().get('data', [])
#     else:
#         print(f"Error fetching trending gifs: {response.status_code}")
#         return None

# def display_gif_titles(gifs):
#     """
#     Prints the titles of the gifs.
#     """
#     if gifs:
#         for i, gif in enumerate(gifs):
#             print(f"{i + 1}. {gif['title']}")
#     else:
#         print("No gifs to display.")

# # Main program loop
# if __name__ == "__main__":
#     while True:
#         user_input = input("\nEnter a term or phrase to search for gifs (or 'exit' to quit): ")
#         if user_input.lower() == 'exit':
#             print("Goodbye! 👋")
#             break
        
#         gifs_to_display = get_gifs(user_input)
#         display_gif_titles(gifs_to_display)