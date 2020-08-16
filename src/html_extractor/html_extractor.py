from bs4 import BeautifulSoup
from bs4 import SoupStrainer


only_captcha_tags = SoupStrainer("captcha")
only_a_tags = SoupStrainer("a")
only_input_tags = SoupStrainer("input")
only_p_tags = SoupStrainer("p")


class HtmlExtractor:
    def extract_captcha(self, html):
        soup = BeautifulSoup(html, 'html.parser', parse_only=only_captcha_tags)
        result = soup.captcha.contents[1].get('style')[44:-78]
        return result

    def extract_day_href(self, html):
        soup = BeautifulSoup(html, 'html.parser', parse_only=only_a_tags)
        result = soup.find("a", "arrow").get("href")
        return result

    def extract_time_slot_href(self, html):
        soup = BeautifulSoup(html, 'html.parser', parse_only=only_a_tags)
        result = soup.find("a", string="Записаться на прием").get('href')
        return result

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
