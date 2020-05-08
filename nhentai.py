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
        return self.all()["result"][0]

    def latest_id(self):
        return int(self.latest()["id"])

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

    def book_cover(self, book_id):
        media_id = self.book_info(book_id)["media_id"]
        cover_url = "https://t.nhentai.net/galleries/" + str(media_id) + "/cover.jpg"
        return cover_url

    def book_tags(self, book_id):
        raw_tags = self.book_info(book_id)["tags"]
        tags = []
        for tag in raw_tags:
            if tag["type"] == "tag":
                tags.append(tag["name"]) 
        return sorted(tags)
