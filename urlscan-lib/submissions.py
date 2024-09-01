# submissions.py


import requests
import time


def see_credits(api_key, wait_time=30):
    """
    Retrieves the current credit balance for the given API key.

    Args:
        api_key (str): The API key to use for authentication.

    Returns:
        dict or int: If the request is successful, returns a dictionary containing the credit balance.
                     If the request fails, returns the HTTP status code.
    """
    url = 'https://urlscan.io/user/quotas/'
    headers = {
        'API-Key': api_key,
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # accepted scan
        return response.json()

    elif response.status_code == 429 or response.status_code == 404:
        # server connection issue or incomplete scan
        if wait_time:
            time.sleep(5)
            return see_credits(api_key, wait_time=wait_time-5)
        else:
            return response

    else:
        return response.status_code
    


def submit_url(scan_url, api_key, wait_time=30):
    """
    Submits a URL for scanning by the URLscan.io service.

    Args:
        url (str): The URL to be scanned.
        api_key (str): The API key to use for authentication.

    Returns:
        dict or int: If the request is successful, returns a dictionary containing the scan results.
                     If the request fails, returns the HTTP status code.
    """
    url = 'https://urlscan.io/api/v1/scan'
    headers = {
        'API-Key': api_key,
        'Content-Type': 'application/json'
    }
    data = {
        'url': scan_url,
        'visibility': 'public'
        }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        # accepted scan
        return response.json()
    
    elif response.status_code == 429:
        # server connection issue
        time.sleep(5)
        return submit_url(scan_url, api_key, wait_time=wait_time-5)
    
    elif response.status_code == 400:
        # rejected scan
        return response.json()
    
    else:
        return response.status_code
    

def submit_url_list(url_list, api_key):
    """
    Submits a list of URLs for scanning by the URLscan.io service.

    Args:
        url_list (list): A list of URLs to be scanned.
        api_key (str): The API key to use for authentication.

    Returns:
        list: A list of dictionaries containing the scan results for each URL.
    """
    results = []
    for url in url_list:
        result = submit_url(url, api_key)
        results.append(result)
        time.sleep(2)
    return results

