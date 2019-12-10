#!usr/bin/python3

import _json
import json
import urllib.request

NEO = "https://api.nasa.gov/neo/rest/v1/feed?api_key=gMzrNEsbplUQamZcQ1uYI1mQvk3fClolbZuT3VLB"

def main():
    ## Get my API key
    with open(r"C:\Users\Student\Documents\nasacreds.txt", "r") as nc:
        ## used little r for little strings -- second r is READ
        myapikey = nc.read()

        print("*****")
        print(myapikey)
        print("*****")


    ##mske a request to NEO and save resp as neoresp
    neoresp = urllib.request.urlopen(NEO)
    ## strip off ATTACHED json data and save as neojson
    neojson = neoresp.read().decode("utf-8")
    ## what the heck is neojson
    print(type(neojson)) ## this returns bytes UNTIL we .decode now it is returning STR

    neopy = json.loads(neojson) ## this now returns dict

    print(neojson) # printing out our dictionary

    for astroids in neopy["near_earth_objects"]["2019-12-08"]:
       # print(astroids["id"])
        #print(astroids["name"])
        print("The Human name is: ", astroids["name"])
        print("The Astronomical ID is: ", astroids["id"])
        print("The Magnitude is: ", astroids["absolute_magnitude_h"])
        print("Estimated Diameter")
        print("Estimated Diameter Min: ", astroids["estimated_diameter"]["kilometers"]["estimated_diameter_min"])
        print("Estimated Diameter Max: ", astroids["estimated_diameter"]["kilometers"]["estimated_diameter_max"])
        print("Close approach date: ", astroids["close_approach_data"][0]["close_approach_date"])
        print("Approach Speed")
        print("Close approach speed in Kilos per second: ", astroids["close_approach_data"][0]["relative_velocity"]["kilometers_per_second"])
        print("Close approach speed in Kilos per hour: ", astroids["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"])
        print("Close approach speed in Miles per hour: ", astroids["close_approach_data"][0]["relative_velocity"]["miles_per_hour"])
        print()
if __name__ == "__main__":
    main()