from bs4 import BeautifulSoup


def verse_parser(page, parser_type, div_tag, verse_class, a_tag, sup_tag, paramark_class, body_class=None):
    soup = BeautifulSoup(page.content, parser_type)

    if body_class is not None:
        body = soup.find(div_tag, class_=body_class)
    else:
        body = soup.find(div_tag)

    scripture = body.find_all(class_=verse_class)

    # Remove all marker tags from the fetched html
    for v in scripture:
        for a in v.find_all(a_tag):
            a.find(sup_tag).decompose()

    verses = [""] * len(scripture)

    # Put the text into a clean format
    for i in range(len(scripture)):
        verses[i] = scripture[i]

    return verses
