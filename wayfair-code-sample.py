"""
Revision Date: 08/09/2018
Author: Bevan Glynn
Language: Python 2.7
Style: PEP8

Overview: This code demonstrations the use of functions and class structure
that return specific elements based on user input and inheritance
"""


class WayfairLLC:  # Base company class that defines gobal elements

    def __init__(self):
        self.Tagline = "Wayfair is one of the world's largest online destinations for the home"
        self.Shipping = "free shipping for orders over $49"


class Wayfair(WayfairLLC):  # Inherits global shipping and tagline from base company class

    # set the unique brand tagline
    Brand_tagline = "Wayfair has everything home for every budget"

    # set the unique brand URL
    Brand_link = "https://www.wayfair.com"


class JossMain(WayfairLLC):  # Inherits global shipping and tagline from base company class

    # set the unique brand tagline
    Brand_tagline = "Joss & Main has affordable discoveries for gorgeous living"

    # set the unique brand URL
    Brand_link = "https://www.jossandmain.com"


class AllModern(WayfairLLC):  # Inherits global shipping and tagline from base company class

    # set the unique brand tagline
    Brand_tagline = "All Modern offers unbelievable prices on everything modern"

    # set the unique brand URL
    Brand_link = "https://www.allmodern.com"


class BirchLane(WayfairLLC):  # Inherits global shipping and tagline from base company class

    # set the unique brand tagline
    Brand_tagline = "Birch lane is the home of classic designs and fresh finds"

    # set the unique brand URL
    Brand_link = "https://www.birchlane.com"


class Perigold(WayfairLLC):  # Inherits global shipping and tagline from base company class

    # set the unique brand taglinea
    Brand_tagline = "Perigold offers the widest-ever selection of premium home"

    # FamilyBrand_Shipping = "Perigold offers " + self.shipping

    # set the unique brand URL
    Brand_link = "https://www.perigold.com"


Choice = None
while Choice is None:
    User_input = int(input("Please choose from the following options for additional information on Wayfair brands \n 1. Wayfair \n 2. Joss & Main  \n 3. All Modern \n 4. Birch Lane \n 5. Perigold \n: "))
    try:
        # try and convert the string input to a number, forces error checking and offers a check condition
        Choice = int(User_input)
    except ValueError:
        # Provide the user with result of value check
        print("{user_input} is not a number, please enter a number only".format(input=User_value))

switcher = {
        1: Wayfair,
        2: JossMain,
        3: AllModern,
        4: BirchLane,
        5: Perigold
        }


def numbers_to_choice(Argument):
    # Pass user input into the dictonary and return the fuction name
    Brand = switcher.get(Argument, "nothing")
    Func = switcher.get(Argument, "nothing")

    # return the requested brand as an excutable fuction
    return Func()


User_result = numbers_to_choice(Choice)


print(User_result.Tagline)
print(User_result.Brand_tagline)
print(User_result.Shipping)
print(User_result.Brand_link)
