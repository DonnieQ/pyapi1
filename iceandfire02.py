#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# Documentation for this API is at
# https://anapioficeandfire.com/Documentation

import pprint
import requests

AOIF_BOOKS = "https://www.anapioficeandfire.com/api/books"

def main():
    ##Send HTTPS GET to the API of ICE and Fire books resource
    gotresp = requests.get(AOIF_BOOKS)

    ## Decode the response
    got_dj = gotresp.json()

    ## print the response
    ## using pretty print so we can read it
    pprint.pprint(got_dj)

    for book in got_dj:
        print(book["name"], "can be referenced at:\n\t", book["url"], "\n")

if __name__ == "__main__":
    main()