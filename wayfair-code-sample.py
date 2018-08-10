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

    brand_options = {
        1: Wayfair,
        2: JossMain,
        3: AllModern,
        4: BirchLane,
        5: Perigold
        }

    choice = None
    while choice is None:
        user_input = raw_input("Please choose from the following options for additional information on Wayfair brands \n 1. Wayfair \n 2. Joss & Main  \n 3. All Modern \n 4. Birch Lane \n 5. Perigold \n: ")
        try:
            # try and convert the string input to a number, forces error checking and offers a check condition
            choice_id = int(user_input)
            choice = resolve_option_from_key(choice_id, brand_options)
        except ValueError:
            # Provide the user with result of value check
            print("'{0}' is not a valid option, please choose an option from the list".format(user_input))

    print(choice.tagline)
    print(choice.brand_tagline)
    print(choice.shipping)
    print(choice.brand_link)



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

    # set the unique brand tagline
    brand_tagline = "Perigold offers the widest-ever selection of premium home"

    # set the unique brand URL
    brand_link = "https://www.perigold.com"


def resolve_option_from_key(option_key, options):
    # provided a key, return the corresponding item or raise an error

    option = options.get(option_key)

    if option is None:
        raise ValueError("Argument is invalid")

    # return the requested object
    return option()

    
if __name__ == '__main__':
    # Execute main method to trigger user input
    main()

