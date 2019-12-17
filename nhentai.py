import json
import requests
import urllib.parse

class Nhentai():
    BASE_URL = "https://nhentai.net/api/"

    @classmethod
    def make_request(cls, url):
        response = requests.get(url)
        if not response:
            return json.loads('{"error": true}')
        return json.loads(response.text)

    def all(self, page_num=1):
        url = self.BASE_URL + "galleries/all"

        parsed_response = self.make_request(url)

        if not isinstance(page_num, int):
            return json.loads('{"error": true}')

        max_pages = parsed_response["num_pages"]
        if page_num > 1 and page_num <= max_pages:
            url = url + "?page=" + str(page_num)
            parsed_response = self.make_request(url)

        return parsed_response

    def latest(self):
        all_parsed_response = self.all()
        return all_parsed_response["result"][0]

    def latest_id(self):
        return self.latest()["id"]

    def query_search(self, user_query, page_num=1):
        query = urllib.parse.quote(user_query, safe='')
        url = self.BASE_URL + "galleries/search?query=" + query

        parsed_response = self.make_request(url)

        if not isinstance(page_num, int):
            return json.loads('{"error": true}')

        max_pages = parsed_response["num_pages"]
        if page_num > 1 and page_num <= max_pages:
            url = url + "?page=" + page_num
            parsed_response = self.make_request(url)

        return parsed_response

    def book_info(self, book_id):
        url = self.BASE_URL + "gallery/" + str(book_id)
        return self.make_request(url)