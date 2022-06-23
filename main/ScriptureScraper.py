import TextScraper
import PageRequester

if __name__ == '__main__':
    page = PageRequester.request_page("https://www.churchofjesuschrist.org/study/scriptures/ot/2-sam/1?lang=eng")
    verses = TextScraper.verse_parser(page, 'div', "verse", "body")

    for v in verses:
        print(v)
