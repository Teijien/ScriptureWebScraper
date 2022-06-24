import requests


def request_page(html):
    page = requests.get(html)

    return page
