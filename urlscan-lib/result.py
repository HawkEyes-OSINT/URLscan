# result.py

import requests
import time


def get_result(uuid, wait_time=30):
    """
    Retreives the results from a domain UUID

    Args:
        UUID (str): The UUID of the domain scan to view

    Returns:
        dict or (int and/or str): If the request is successful it returns a dict with scan results
                     If the request is not successful, it returns the response status code
                     Relevant error messages are also returned
    """
    url = f'https://urlscan.io/api/v1/result/{uuid}/'
    response= requests.get(url)

    if response.status_code == 200:
        # successful request
        data = response.json()
        return data
    
    elif response.status_code == 429 or response.status_code == 404:
        # server connection issue
        if wait_time:
            time.sleep(5)
            return get_result(uuid, wait_time=wait_time-5)
        else:
            return response
        
    elif response.status_code == 410:
        # deleted scan
        return response.status_code, 'result deleted'
    
    else:
        return response.status_code
    

def get_png_snapshot(uuid, wait_time=30):
    """
    Get a snapshot of website from a scan UUID

    Args:
        UUID (str): The UUID of the domain scan to view

    Returns:
        bytes or (int and/or str): If the request is successful it returns the PNG snapshot
                     If the request is not successful, it returns the response status code
                     Relevant error messages are also returned
    """ 
    url = f'https://urlscan.io/screenshots/{uuid}.png'
    response = requests.get(url)

    if response.status_code == 200:
        # successful request
        return response.content
    
    elif response.status_code == 429:
        # server connection issue
        if wait_time:
            time.sleep(5)
            return get_png_snapshot(uuid, wait_time=wait_time-5)
        else:
            return response

    elif response.status_code == 404:
        # no screenshot stored
        return response.status_code, 'no screenshot stored'

    else:
        return response.status_code
    

def get_dom_snapshot(uuid, wait_time=30):
    """
    Get a DOM snapshot of website from a scan UUID

    Args:
        UUID (str): The UUID of the domain scan to view

    Returns:
        bytes or (int and/or str): If the request is successful it returns the DOM snapshot
                     If the request is not successful, it returns the response status code
                     Relevant error messages are also returned
    """
    url = f'https://urlscan.io/dom/{uuid}/'
    response = requests.get(url)

    if response.status_code == 200:
        # successful request
        return response.content

    elif response.status_code == 429:
        # server connection issue
        if wait_time:
            time.sleep(5)
            return get_dom_snapshot(uuid, wait_time=wait_time-5)
        else:
            return response

    elif response.status_code == 404:
        # no screenshot stored
        return response.status_code, 'no screenshot stored'

    else:
        return response.status_code


print(get_dom_snapshot('9cf13d62-3b36-454d-9751-a85132d0e1cc'))