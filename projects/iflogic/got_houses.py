#!/usr/bin/env python3
ipchk = input("What house are you in GOT:") # this line now prompts the user for input

# check if ipchk does NOT have a value
while ipchk == "":
    ipchk = input("What house are you in GOT:") # this line now prompts the user for input

# if user sets Preffered House
if ipchk == "house lanister":
   print("Looks like House Lanister of Casterly Rock was set: " + ipchk + " This is not recommended!!")
elif ipchk == "house stark":
    print("house stark lives on🐺")
elif ipchk == "house targaryen":
    print("Dracarys 🔥🔥🔥🐉")
else: # if any data is provided, this will test true
    print("Looks like The Mother of Dragons, Queen of the unsully, breaker of chains will accept your response") 
#e: # if data is NOT provided
 #  print("You did not provide input.n\ Dracarys") # indented under else
