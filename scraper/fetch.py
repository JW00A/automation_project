import requests

def fetch_page(url):
    """
    Fetch the HTML content of a url,
    Returns the page text on success, or None if the request fails.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print("Status code:", response.status_code)

        return response.text
    
    except requests.exceptions.RequestException as e:
        print("Error fetching page:", e)
        
        return None