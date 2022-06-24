from flask import Flask

import TextScraper
import PageRequester

app = Flask(__name__)


@app.route("/")
def get_scripture():
    page = PageRequester.request_page("https://www.churchofjesuschrist.org/study/scriptures/ot/ps/119?lang=eng")
    verses = TextScraper.verse_parser(page, 'html.parser', 'div', "verse", 'a', 'sup', "body")
    http = ""

    for v in verses:
        http = http + str(v)

    return http

if __name__ == '__main__':
    app.run()
