import requests

url = "https://jsonplaceholder.typicode.com/users"

def get_api_data(url):
    '''get data from url'''
    response = requests.get(url)

    api_data = response.json()

    return api_data

