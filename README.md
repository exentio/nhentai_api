Python wrapper for nHentai APIs
===

This wrapper uses the official (and poorly documented) nHentai APIs to get info about the content of your favorite website.  
It's still a WIP, so be careful.

### Currently available methods
`Nhentai().all(page_num=1)`: Returns all the doujin on nHentai's homepage; to get the other pages, use the `page_num` parameter. Returns `dict`.  
`Nhentai().latest()`: Returns info about the latest uploaded doujin. Returns `dict`.  
`Nhentai().latest_id()`: Returns the ID of the latest uploaded doujin. Useful for random generators. Returns `int`.  
`Nhentai().query_search(user_query, page_num=1)`: Performs a search. Put your keywords in `user_query`; to get the other pages, use the `page_num` parameter. Returns `dict`.  
`Nhentai().book_info(book_id)`: Gets all the info about a magic number of your choice, like `177013`. Returns `dict`.  
`Nhentai().book_cover(book_id)`: Gets the URL of the cover of a book (a `.jpg` image). Returns `str`.  
`Nhentai().book_tags(book_id)`: Gets all the tags of a book, the result is alphabetically sorted. Returns `list`.  


In case of a request error (like 404 or similar) or invalid input, the output is `{"error": True}`. This behavior was chosen because it's the same output that nHentai APIs give on error. Let me know if it's not good practice.  

### TODO
+ Use objects instead of dicts. Which means don't use this wrapper expecting for things not to change.  
+ More documentation about the output of the APIs.  
+ Search by tag. nHentai APIs use tag IDs instead of words, so I have to find a way to find the ID that matches a certain tag. I think I'll go with scraping them from the `/tags` page.  
+ Pages and covers.  
+ Selective data. Like getting all the tags, the group name, the parody, and stuff like this.  
+ Look for bugs. I did some basic debugging but it was pretty late when I wrote this.  

### Resources used
+ [https://github.com/NHMoeDev/NHentai-android/issues/27](https://github.com/NHMoeDev/NHentai-android/issues/27)  
+ [https://edgyboi2414.github.io/nhentai-api](https://edgyboi2414.github.io/nhentai-api)
+ [https://github.com/RicterZ/nhentai](https://github.com/RicterZ/nhentai)