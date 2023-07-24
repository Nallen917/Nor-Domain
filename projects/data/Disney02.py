#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://api.disneyapi.dev

import pprint
import requests

AOIF_CHARACTERS = "https://api.disneyapi.dev/character"

def main():
    ## Send HTTPS GET to the API of ICE and Fire books resource
    gotresp = requests.get(AOIF_CHARACTERS)

    ## Decode the response
    got_dj = gotresp.json()

    ## print the response
    ## using pretty print so we can read it
    pprint.pprint(got_dj)

if __name__ == "__main__":
    main()

