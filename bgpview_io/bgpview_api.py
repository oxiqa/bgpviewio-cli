import requests

# bgpview api URL
API_URL = "https://api.bgpview.io"
# search API
def search(query_term):
    params = {"query_term": query_term}
    
    try:
        response = requests.get(API_URL + '/search', params=params)
        response.raise_for_status()  # Raise an error if the request is not successful
        return response.json()    
        
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return e

def get_ip4_prefixes(query_term):
    data = search(query_term)
    ipv4_prefixes = data.get("data", {}).get("ipv4_prefixes", [])
        
    if ipv4_prefixes:
        return ipv4_prefixes
    else:
        print("No IPv4 prefixes found in the response.")
        return []