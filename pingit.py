#!/usr/bin/python3
"""Alta3 Research | RZFeeser@alta3.com
   Writing a script to perform ICMP checks."""

import os
import sys


## Ping router - returns True or False
def ping_router(hostname):

    response = os.system("ping -c 1 " + hostname)

    #and then check the response...
    if response == 0:
        return True
    else:
        return False


def main():
    # Get the command-line arguments excluding the script name
    args = sys.argv[1:]

    if not args:
        print("Usage: python script_name.py <ip_address> [ip_address ...]")
        return

    print("\n***** STARTING ICMP CHECKING *****")
    
    # Iterate through the command-line arguments (IP addresses) and perform ICMP checks
    for x in args:
        if ping_router(x):
            print(f"IP address {x} is responding to ICMP")
        else:
            print(f"IP address {x} is not responding to ICMP")

if __name__ == "__main__":
    main()



