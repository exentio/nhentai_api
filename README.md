Python wrapper for nHentai APIs
===

This wrapper uses the official (and poorly documented) nHentai APIs to get info about the content of your favorite website.  
It's still a WIP, so be careful.  

[Documentation in the wiki.](https://github.com/exentio/nhentai_api/wiki)

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