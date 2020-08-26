from bs4 import BeautifulSoup
from bs4 import SoupStrainer

from src.actions_executors.iexecutors import IHtmlExtractor

only_captcha_tags = SoupStrainer("captcha")
only_a_tags = SoupStrainer("a")
only_input_tags = SoupStrainer("input")
only_p_tags = SoupStrainer("p")


class HtmlExtractor(IHtmlExtractor):
    def extract_captcha(self, html):
        soup = BeautifulSoup(html, 'html.parser', parse_only=only_captcha_tags)
        if soup.captcha:
            return soup.captcha.contents[1].get('style')[44:-78]
        return None

    def extract_day_href(self, html):
        soup = BeautifulSoup(html, 'html.parser', parse_only=only_a_tags)
        if soup.find("a", "arrow"):
            return soup.find("a", "arrow").get("href")
        return None

    def extract_time_href(self, html):
        soup = BeautifulSoup(html, 'html.parser', parse_only=only_a_tags)
        if soup.find("a", string="Записаться на прием"):
            return soup.find("a", string="Записаться на прием").get('href')
        return None

    def extract_hidden_fields(self, html):
        soup = BeautifulSoup(html, 'html.parser', parse_only=only_input_tags)
        hidden_inputs = soup.find_all(type="hidden")
        result = {}
        for el in hidden_inputs:
            result[el.get('name')] = el.get('value')
        return result

    def check_success(self, html):
        soup = BeautifulSoup(html, 'html.parser', parse_only=only_p_tags)
        return "ошибка" not in soup.p.text
