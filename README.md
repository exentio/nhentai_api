Python wrapper for nHentai APIs
===

This wrapper uses the official (and poorly documented) nHentai APIs to get info about the content of your favorite website.  
It's still a WIP, so be careful.

### Currently available methods
`Nhentai().all(page_num=1)`: Returns all the books on nHentai's homepage; to get the other pages, use the `page_num` parameter. Returns `dict`. Throws exception if `page_num` is more than the actual available pages.  
`Nhentai().latest()`: Returns info about the latest uploaded book. Returns `dict`.  
`Nhentai().latest_id()`: Returns the ID of the latest uploaded book. Useful for random generators. Returns `int`.  
`Nhentai().id_exists(book_id)`: Checks the existence of a book by ID. Returns `bool`.  
`Nhentai().query_search(user_query, page_num=1)`: Performs a search. Put your keywords in `user_query`; to get the other pages, use the `page_num` parameter. Returns `dict`.  
`Nhentai().book_info(book_id)`: Gets all the info about a magic number of your choice, like `177013`. Returns `dict`.  
`Nhentai().book_title(book_id)`: Gets the book title, english format. Returns `str`.  
`Nhentai().book_title_jp(book_id)`: Gets the book title, japanese format. Returns `str`.  
`Nhentai().book_cover(book_id)`: Gets the URL of the cover of a book (a `.jpg` image). Returns `str`.  
`Nhentai().book_pagenum(book_id)`: Gets the number of pages of a book. Returns `int`.  
`Nhentai().book_date(book_id, unix_ts = False)`: Gets the date of a book. Returns `str` in the format `DD-MM-YYYY HH:MM:SS` if the ID is the only parameter; instead if `unix_ts` is set to `True`, it returns an Unix timestamp as an `int`.  
`Nhentai().book_tags(book_id, return_string = False)`: Gets all the tags of a book, the result is alphabetically sorted. Returns `list` if the ID is the only parameter; instead if `return_string` is set to `True`, it returns a `str`.  
`Nhentai().book_artists(book_id, return_string = False)`: Gets the artists of a book, the result is alphabetically sorted. Returns `list` if the ID is the only parameter; instead if `return_string` is set to `True`, it returns a `str`. If the artist is missing, the only content of the list is `no artist`.  
`Nhentai().book_parodies(book_id, return_string = False)`: Gets all the parodies associated to the book, the result is alphabetically sorted. Returns `list` if the ID is the only parameter; instead if `return_string` is set to `True`, it returns a `str`. If the info about parodies is not available, the only content of the list is `no parodies`.  
`Nhentai().book_groups(book_id, return_string = False)`: Gets the groups that made a book, the result is alphabetically sorted. Returns `list` if the ID is the only parameter; instead if `return_string` is set to `True`, it returns a `str`. If there are no groups, the only content of the list is `no groups`.  
`Nhentai().book_language(book_id, return_string = False)`: Gets the language of a book, the result is alphabetically sorted (often there's the tag "translated"). Returns `list` if the ID is the only parameter; instead if `return_string` is set to `True`, it returns a `str`. If there is no info about the language, the only content of the list is `no language info`.  
`Nhentai().book_characters(book_id, return_string = False)`: Gets the characters in a book, the result is alphabetically sorted. Returns `list` if the ID is the only parameter; instead if `return_string` is set to `True`, it returns a `str`. If there is no info about the characters, the only content of the list is `no character info`.  


Exceptions in case of 404 or invalid input are NOT handled, I suggest using the `id_exists()` function to check for 404s. Some functions in case of a request error give this output: `{"error": True}`. This behavior is the same output that nHentai APIs give on error. The only exception raising I implemented is when the parameter of `Nhentai().all()` is bigger than the number of actual pages on the website. Let me know if those things are not good practice.  

### TODO
+ Use objects instead of dicts. Which means don't use this wrapper expecting for things not to change.  
+ More documentation about the output of the APIs.  
+ Filter by tag. nHentai APIs use tag IDs instead of words, so I have to find a way to find the ID that matches a certain tag. I think I'll go with scraping them from the `/tags` page.  
+ Get specific book pages.  
+ Look for bugs.  

### Resources used
+ [https://github.com/NHMoeDev/NHentai-android/issues/27](https://github.com/NHMoeDev/NHentai-android/issues/27)  
+ [https://edgyboi2414.github.io/nhentai-api](https://edgyboi2414.github.io/nhentai-api)
+ [https://github.com/RicterZ/nhentai](https://github.com/RicterZ/nhentai)