from bs4 import BeautifulSoup


def verse_parser(page, tag, verse_class, body_class=None):
    soup = BeautifulSoup(page.content, 'html.parser')

    if body_class is not None:
        body = soup.find(tag, class_=body_class)
    else:
        body = soup.find(tag)

    scripture = body.find_all(class_=verse_class)

    verses = [""] * len(scripture)

    # Put the text into a clean format
    for i in range(len(scripture)):
        verses[i] = scripture[i].get_text()

    return verses
