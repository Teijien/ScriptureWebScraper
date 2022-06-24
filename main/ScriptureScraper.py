import TextScraper
import PageRequester

if __name__ == '__main__':
    page = PageRequester.request_page("https://www.churchofjesuschrist.org/study/scriptures/ot/2-sam/1?lang=eng")
    verses = TextScraper.verse_parser(page, 'html.parser', 'div', "verse", 'a', 'sup', "para-mark", "body")

    for v in verses:
        print(v.get_text())
