import json
import requests
import urllib.parse
from datetime import datetime

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
        if page_num > max_pages:
            raise ValueError("There are only " + str(max_pages) + " pages.")

        return parsed_response

    def latest(self):
        return self.all()["result"][0]

    def latest_id(self):
        return int(self.latest()["id"])

    def id_exists(self, book_id):
        try:
            self.book_info(book_id)["error"]
        except KeyError:
            return True
        return False

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

    def book_title(self, book_id):
        title = self.book_info(book_id)["title"]["english"]
        if len(title) == 0:
            title = "N/A"
        return title

    def book_title_jp(self, book_id):
        title = self.book_info(book_id)["title"]["japanese"]
        if len(title) == 0:
            title = "N/A"
        return title

    def book_cover(self, book_id):
        media_id = self.book_info(book_id)["media_id"]
        cover_url = "https://t.nhentai.net/galleries/" + str(media_id) + "/cover.jpg"
        return cover_url

    def book_pagenum(self, book_id):
        return self.book_info(book_id)["num_pages"]

    def book_date(self, book_id, return_string = False):
        timestamp = self.book_info(book_id)["upload_date"]

        if return_string:
            return datetime.utcfromtimestamp(timestamp).strftime('%d-%m-%Y %H:%M:%S')
        return timestamp

    def book_category(self, book_id):
        raw_tags = self.book_info(book_id)["tags"]
        tags = []
        for tag in raw_tags:
            if tag["type"] == "category": 
                return tag["name"]

    def book_tags(self, book_id, return_string = False):
        raw_tags = self.book_info(book_id)["tags"]
        tags = []
        for tag in raw_tags:
            if tag["type"] == "tag":
                tags.append(tag["name"])

        if return_string:
            return ', '.join(sorted(tags))
        return sorted(tags)

    def book_artists(self, book_id, return_string = False):
        raw_tags = self.book_info(book_id)["tags"]
        artists = []
        for tag in raw_tags:
            if tag["type"] == "artist":
                artists.append(tag["name"])

        if not artists:
            artists = ["no artist"]
        if return_string:
            return ', '.join(sorted(artists))
        return sorted(artists)

    def book_parodies(self, book_id, return_string = False):
        raw_tags = self.book_info(book_id)["tags"]
        parodies = []
        for tag in raw_tags:
            if tag["type"] == "parody":
                parodies.append(tag["name"])

        if not parodies:
            parodies = ["no parody"]
        if return_string:
            return ', '.join(sorted(parodies))
        return sorted(parodies)

    def book_groups(self, book_id, return_string = False):
        raw_tags = self.book_info(book_id)["tags"]
        groups = []
        for tag in raw_tags:
            if tag["type"] == "group":
                groups.append(tag["name"])

        if not groups:
            groups = ["no groups"]
        if return_string:
            return ', '.join(sorted(groups))
        return sorted(groups)

    def book_language(self, book_id, return_string = False):
        raw_tags = self.book_info(book_id)["tags"]
        language = []
        for tag in raw_tags:
            if tag["type"] == "language":
                language.append(tag["name"])

        if not language:
            language = ["no language info"]
        if return_string:
            return ', '.join(sorted(language))
        return sorted(language)

    def book_characters(self, book_id, return_string = False):
        raw_tags = self.book_info(book_id)["tags"]
        characters = []
        for tag in raw_tags:
            if tag["type"] == "character":
                characters.append(tag["name"])

        if not characters:
            characters = ["no character info"]
        if return_string:
            return ', '.join(sorted(characters))
        return sorted(characters)