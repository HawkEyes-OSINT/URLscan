# search.py

import requests
import time


def search(perameter, field_name='domain', size=100, wait_time=30):
    """
    Searches for domains based on the provided parameter and query.
    For details regarding fields and layout, see https://urlscan.io/docs/search/
    
    Args:
        perameter (str): The value to search for in the specified field.
        field_name (str, optional): The field to search within. Defaults to 'domain'.
        size (int, optional): The maximum number of results to return. Defaults to 100.
        
    Returns:
        dict: The JSON response from the CRT.sh API.
    """
    url = f'https://urlscan.io/api/v1/search/?q={field_name}:{perameter}&size={size}'
    response = requests.get(url)

    if response.status_code == 200:
        # successful request
        data = response.json()
        return data
    
    elif response.status_code == 429:
        # server connection issue
        if wait_time:
            time.sleep(wait_time)
            return search(perameter, field_name=field_name, size=size, wait_time=wait_time-5)
        else:
            return response
        
    else:
        return response.status_code
    
print(search('google.com'))