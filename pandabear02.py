#!/usr/bin/python3

import pandas as pd

def main():
    ciscocsv = pd.read_csv("ciscodata.csv")
    ciscojson = pd.read_json("ciscodata2.json")

    print(ciscocsv.head())

    print(ciscojson.head())

    ciscodf = pd.concat([ciscocsv, ciscojson])

    print(ciscodf)

if __name__ == "__main__":
    main()