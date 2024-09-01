# submissions.py

import requests


def see_credits(api_key):
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
        return response.json()
    else:
        return response.status_code



test_key = 'e56dc958-ecfb-4fc4-bb69-5d3b5a4235c2'
print(see_credits(test_key))
