import os
from yelpapi import YelpAPI

MY_API_KEY = "api key from yelp dot com"

with YelpAPI(MY_API_KEY) as yapi:
    search_results = yapi.search_query(term='ice cream', location='austin, tx', sort_by='rating', limit=5)
    print(search_results)