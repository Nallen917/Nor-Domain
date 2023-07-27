#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()

    ## get start date
    start_date = input("Enter the start date (YYYY-MM-DD): ")

    ## get end date but its optional
    end_date = input("Enter the end date (YYYY-MM-DD) [optional]: ")

    request_params = "start_date=" + start_date
    if end_date:
        request_params += "&end_date=" + end_date

    # make a request with the request library
    neowrequest = requests.get(NEOURL + request_params + "&" + nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()

    ## display NASAs NEOW data
    print(neodata)
    print("Asteroids have been returned from the following dates:")
    print(neodata["near_earth_objects"].keys())

if __name__ == "__main__":
    main()

