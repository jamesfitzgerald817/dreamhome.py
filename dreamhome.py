#COSC 151. 101
#Spring 2020
#James Fitzgerald
#Febuary 18, 2020

home_location = input("What is your dream home location?")#What is the State of your dream home?
climate1 = input("What is your dream climate (tropic, polar, etc.)?")#What is the ideal climate of your dream home location?
own_rent = input("Do you own or rent your dream home?")#Do you own or rent your dream home?
number_years = int(input("How many years have you lived in your location?"))#What is the number of years you have reside in your home? 
homename = input("What is the name of your home(Playboy Mansion, Graceland, Neverland, etc.)?") #What is the name you've given to your home?
hometype = input("The type of home you reside in(apt,condo,etc.)?")#What type of home is your home?
floors = int(input("How many floors does your home contain?"))#How many floors are inside your home?
style_home = input("What is the style of home you reside in(ranch,duplex,mansion,etc.)?")#What is the style of your home?
gas_electric = input("Does your home use electric or gas?")#Does your home use gas or electric heating?
watersource = input("What type of water source do you have(surface or ground)?")#What is the form of the main source of water to your home surface or ground?
mortgage = float(input("What is total you pay for your mortgage yearly?"))#What is the amount you pay for your mortgage per year?
utilities = float(input("What is the total you pay for your utilities yearly?"))#What is the total you pay for your homes utilities per year?
taxes = float(input("What is the total amount of taxes you pay per year on your home?"))#What is the total ampount you pay in taxes per year for your home?                                 
yearly_cost = mortgage+utilities+taxes
monthlytotal = yearly_cost/12



print("Tell me the name of your palace",homename, "and what type of design is this masterpiece",hometype,"please provide the number of floors",floors,"tell me does your home run on",gas_electric,"please provide the wate your source your home uses",watersource,"Thank you the monthly total of your home will be $.",format(monthlytotal,'.2f'))

