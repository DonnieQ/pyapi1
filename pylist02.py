#!/usr/bin/python3

def main():
    ##create an empty list
    mylist = []

    mylist.append("monday")

    mylist.append("tuesday")

    mylist.append("wednesday")

    mylist.append("thursday")

    print(mylist)

    #print thursday on the screen
    print(mylist[3])

    ##create and empty dictionary
    studiomovies = {}

    ##we want to create a KEY pixar and map a value
    studiomovies["pixar"] = "toystory"

    studiomovies["universal"] = "jaws"

    studiomovies["paramount"] = "raiders of the lost ark"

    print(studiomovies)

    print(studiomovies["paramount"])

    studiomovies["pixar"] =["toy story", "up"]
    print(studiomovies)
    print(studiomovies["pixar"][1])

if __name__ == "__main__":
    main()