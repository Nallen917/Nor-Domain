#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://api.disneyapi.dev

import requests
num = int(input("Pick the number of a Disney memory between 0-49?"))
url = "https://api.disneyapi.dev/character/"

def main():
    ## Send HTTPS GET to the API of ICE and Fire books resource
    get_url =requests.get(url)
    api = get_url.json()
    api_dict = api    
    ## Decode the response
    #got_dj = gotresp.json()
    #print(api_dict['data'][1]['tvShows'])
    disney = api_dict['data'][num]["tvShows"]
    print(api_dict['data'][num]["name"])
    if disney : 
        for tvShows in disney:
            print(tvShows)
    else :
        print("this character hasn't been in a tv show yet")
    
'''
    ## loop across response
    for singlecharacter in got_dj:
        ## display the names of each character
        ## all of the below statements do the same thing
        #print(singlebook["name"] + ",", "pages -", singlebook["numberOfPages"])
        #print("{}, pages - {}".format(singlebook["name"], singlebook["numberOfPages"]))
        print(f"{singlecharacter['info']}, totalPages - {singlecharacter['count']}")
        print(f"\tAPI URL -> {singlecharacter['url']}\n")
        # print data
        print(f"\tdata -> {singlecharacter['data']}\n")
        print(f"\ttvshows -> {singlecharacter['tvshows']}\n")
        print(f"\tfilms -> {len(singlecharacter['films'])}\n")
'''
if __name__ == "__main__":
    main()

