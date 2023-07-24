#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://api.disneyapi.dev

import requests

AOIF = "https://api.disneyapi.dev"

def main():
    ## Send HTTPS GET to the API of Disney
    gotresp = requests.get(AOIF)

    ## Decode the response
    got_dj = gotresp.json()

    ## print the response
    print(got_dj)
    
    ## display only the keys within
    ## the dictionary by using dict.keys()
    ## great for seeing what keys are available for lookup
    print(got_dj.keys())
    

if __name__ == "__main__":
    main()

