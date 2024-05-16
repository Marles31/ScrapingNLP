from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


class parsingEntity:

    def response(self):
        response_list = []
        myurl ="https://stackoverflow.com/questions/415511/how-do-i-get-the-current-time-in-python"
        request_site = Request(myurl, headers={"User-Agent": "Mozilla/5.0"})
        html = urlopen(request_site).read()
        soupifield = BeautifulSoup(html, "html.parser")
        question = soupifield.find("div", {"class": "postcell post-layout--right"})
        questiontext = question.find("div", {"class": "s-prose js-post-body"})
        answer = soupifield.find("div", {"class": "answercell post-layout--right"})
        answertext = answer.find("div", {"class": "s-prose js-post-body"})
        answer_text = answertext.get_text().strip().replace('\n', '<br>')

        response_info = {
            "Question": questiontext.get_text().strip(),
            "Answer": answer_text
        }

        response_list.append(response_info)

        return response_list