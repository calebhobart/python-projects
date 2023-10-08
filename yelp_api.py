import os
import pandas as pd
from yelpapi import YelpAPI

MY_API_KEY = "api key from yelp dot com"

term = None

while term is None:
    input_value = input("Please enter your restaurant search terms: ")
    try:
        term = str(input_value)
    except ValueError:
        print("{input} is not a string, please enter a string only".format(input=input_value))

#term = 'ice cream'
location = 'columbus, oh'
sort_by = 'rating'
limit = 5

print("Calling Yelp API to search for {input} in {location}...\n".format(input=term,location=location))

with YelpAPI(MY_API_KEY) as yapi:
    search_results = yapi.search_query(term=term, location=location, sort_by=sort_by, limit=limit)
    #for each in search_results:
        #print(type(each))
        #print(type(search_results[each]))
    df = pd.DataFrame(search_results.get('businesses'))
    #print(df)
    print('Results of search:')
    for each in df['name']:
        print(each)

    