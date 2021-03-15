#
#
# Python:   3.9
#
# Author:   John Trump
#           
#
# Purpose:  Create two classes that inherit from another class:
#               1. Ensure each child has at least two of their own attributes
#               2. Comment the code
#


class Block:
    # Define the attribute of the class
    name = "No Name Provided"
    size = ""
    color = "multi"
    age_range = 0

#child classes of Block below (Wooden and NonStackable)
#inherited all properties from Block and added their own properties(attributes)
class Wooden(Block):
    connectable = False
    number_of_parts= ''

class NonStackables(Block):
    Connection_Type = ' '
    material = ""

   


