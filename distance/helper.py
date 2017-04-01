"""
Helper functions

http://wiki.c2.com/?HelperFunction
"""


def http_get(url):
    """
    Wrappper function to call the HTTP GET Method
    """
    import requests
    import json
    response = requests.get(url)
    if not response.ok:
        response.raise_for_status()

    return json.loads(response.content.decode('utf-8'))


def loadfile(filename):
    """
    Given a CSV file read and convert in dict structure
    """
    import csv
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return [dict(r) for r in reader]


def head_list(value):
    """
    Gets the first element of list
    Inspired in https://lodash.com/docs#head
    """
    return (value or [None])[0]


def chunkfy(lst, n):
    """
    Split the list to new list with 'n' elements
    """
    return[lst[i:i + n] for i in range(0, len(lst), n)]
