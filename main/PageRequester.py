import requests


def request_page(html):
    page = requests.get("https://www.churchofjesuschrist.org/study/scriptures/ot/2-sam/1?lang=eng")

    return page
