"""
Revision Date: 08/10/2018
Author: Bevan Glynn
Language: Python 2.7
Style: PEP8
Repo: https://github.com/Bayesian-thought/code-sample
Overview: This code demonstrations the use of functions and class structures
that return specific elements based on user input and inheritance
"""


def main():
    switcher = {
        1: Wayfair,
        2: JossMain,
        3: AllModern,
        4: BirchLane,
        5: Perigold
        }

    choice = None
    while choice is None:
        user_input = int(input("Please choose from the following options for additional information on Wayfair brands \n 1. Wayfair \n 2. Joss & Main  \n 3. All Modern \n 4. Birch Lane \n 5. Perigold \n: "))
        try:
            # try and convert the string input to a number, forces error checking and offers a check condition
            choice = int(user_input)
        except ValueError:
            # Provide the user with result of value check
            print("{User_input} is not a number, please enter a number only".format(input=user_input))

    # Improve this by calling directly from user input
    user_result = numbers_to_choice(choice, switcher)

    print(user_result.tagline)
    print(user_result.brand_tagline)
    print(user_result.shipping)
    print(user_result.brand_link)


class WayfairLLC:  # Base company class that defines gobal elements

    def __init__(self):
        self.tagline = "Wayfair is one of the world's largest online destinations for the home"
        self.shipping = "free shipping for orders over $49"


class Wayfair(WayfairLLC):  # Inherits global shipping and tagline from base company class

    # set the unique brand tagline
    brand_tagline = "Wayfair has everything home for every budget"

    # set the unique brand URL
    brand_link = "https://www.wayfair.com"


class JossMain(WayfairLLC):  # Inherits global shipping and tagline from base company class

    # set the unique brand tagline
    brand_tagline = "Joss & Main has affordable discoveries for gorgeous living"

    # set the unique brand URL
    brand_link = "https://www.jossandmain.com"


class AllModern(WayfairLLC):  # Inherits global shipping and tagline from base company class

    # set the unique brand tagline
    brand_tagline = "All Modern offers unbelievable prices on everything modern"

    # set the unique brand URL
    brand_link = "https://www.allmodern.com"


class BirchLane(WayfairLLC):  # Inherits global shipping and tagline from base company class

    # set the unique brand tagline
    brand_tagline = "Birch lane is the home of classic designs and fresh finds"

    # set the unique brand URL
    brand_link = "https://www.birchlane.com"


class Perigold(WayfairLLC):  # Inherits global shipping and tagline from base company class

    # set the unique brand taglinea
    brand_tagline = "Perigold offers the widest-ever selection of premium home"

    # FamilyBrand_Shipping = "Perigold offers " + self.shipping

    # set the unique brand URL
    brand_link = "https://www.perigold.com"


def numbers_to_choice(argument, switcher):
    # Pass user input into the dictonary and return the fuction name
    brand = switcher.get(argument, "nothing")
    func = switcher.get(argument, "nothing")

    # return the requested brand as an excutable fuction
    return func()


if __name__ == '__main__':
    # Execute main method to trigger user input
    main()

