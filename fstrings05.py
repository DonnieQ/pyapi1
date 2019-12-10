#!/usr/bin/python3

def main():
    myname = "Dusty" #string
    myage = 27 #i nt
    mykids= ["Eason", "Ezra"] # list

    # this will work (this is called concatination)
    print(myname + " is the GOAT.")

    #this will not work
    #print(myname + " is " + myage)
    #this will work (we changed an orange into an apple)
    print(myname + " is " + str(myage))

    #we can also print a series of objects regardless of their type
    print(myname, "is", myage)

    ## f strings can be used anywhere even inside print
    print(f'My name, {myname}, was given to me {myage} years ago')

    mystring = f"The name of my kids are {mykids[0]} and {mykids[1]}"
    print(mystring)

if __name__ == "__main__":
    main()