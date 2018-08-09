""" 
Revision Date: 08/09/2018
Author: Bevan Glynn
Language: Python 2.7
Style: PEP8

Overview: This code demonstrations the use of functions and class structure that return specific elements based on user input and inheritance
"""
class WayfairLLC: # Base company class that defines gobal elements 
    
    def __init__(self):
        self.tagline = "Wayfair is one of the world's largest online destinations for the home"
        self.shipping = "free shipping for orders over $49"
       ## self.brand = brand 
            
class wayfair(WayfairLLC): # Inherits from shipping and tagline from baseclass 
    
    # set the unique brand tagline
    FamilyBrand_tagline = "Wayfair has everything home for every budget"

    # set the unique brand URL
    FamilyBrand_link = "https://www.wayfair.com"

class jossMain(WayfairLLC): # Inherits from shipping and tagline from baseclass 
    
    # set the unique brand tagline
    FamilyBrand_tagline = "Joss & Main has affordable discoveries for gorgeous living"

    # set the unique brand URL
    FamilyBrand_link = "https://www.jossandmain.com"

class allmodern(WayfairLLC): # Inherits from shipping and tagline from baseclass 
    
    # set the unique brand tagline
    FamilyBrand_tagline = "All Modern offers unbelievable prices on everything modern"

    # set the unique brand URL
    FamilyBrand_link = "https://www.allmodern.com"

class birchlane(WayfairLLC): # Inherits from shipping and tagline from baseclass 
    
    # set the unique brand tagline
    FamilyBrand_tagline = "Birch lane is the home of classic designs and fresh finds"

    # set the unique brand URL
    FamilyBrand_link = "https://www.birchlane.com"

class perigold(WayfairLLC): # Inherits from shipping and tagline from baseclass 
    
    # set the unique brand taglinea
    FamilyBrand_tagline = "Perigold offers the widest-ever selection of premium home"

    ##FamilyBrand_Shipping = "Perigold offers " + self.shipping

    # set the unique brand URL
    FamilyBrand_link = "https://www.perigold.com"


 
choice = None
while choice is None:
    user_input = input("Please choose from the following options for additional information on Wayfair brands \n 1. Wayfair \n 2. Joss & Main  \n 3. All Modern \n 4. Birch Lane \n 5. Perigold \n: ")
    try:
        # try and convert the string input to a number, forces error checking and offers a check condition 
        choice = int(user_input)
    except ValueError:
        # Provide the user with result of value check
        print("{user_input} is not a number, please enter a number only".format(input=user_value))
 
switcher = {
        1: wayfair,
        2: jossMain,
        3: allmodern,
        4: birchlane,
        5: perigold
        }
 
def numbers_to_choice(argument):
    # Get the function from switcher dictionary
    brand = switcher.get(argument, "nothing")
    func = switcher.get(argument, "nothing")
    # print(switcher.get(argument, "nothing"))

    # return the brand as a excutable fuction
    return func()


user_result = numbers_to_choice(choice)


print(user_result.tagline)
print(user_result.FamilyBrand_tagline)
##print(user_result.FamilyBrand_Shipping)
print(user_result.shipping)
print(user_result.FamilyBrand_link)

