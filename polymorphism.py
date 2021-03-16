#
#
# Python:   3.9
#
# Author:   John Trump
#           
#
# Purpose:  Create two clases that inherit from another class
#               1. Each child will have two attributes
#               2. Parent will have one method
#               3. Both children will use polymorphism of parent
#



class Fruit:
    # Define the attribute of the class
    name = "No Name Provided"
    origin = "No Region Provided"
    ripe_color = "Color"
    

     #Define the methods of the class
    def Info(self):#"self" is the key to the Fruit class, def is its method
        msg = "\nName: {}\nCentrally located: {}\nColor when ripe: {}".format(self.name,self.origin,self.ripe_color)
        return msg


#child classes of user below (Kiwi and Mango)
#inherited all properties from Fruit and added their own properties(attributes)
class Kiwi(Fruit):
    price = 5.00
    taste = 'sweet and sour'

    #Define the methods of the class
    def Info(self):
        msg = "\nName: {}\nCentrally located: {}\nColor when ripe: {}\nPrice: {}\nHow it tastes: {}".format(Fruit.name,Fruit.origin,Fruit.ripe_color,self.price,self.taste)
        return msg

    

class Mango(Fruit):
    messy = 'yes'
    delicious = True

    #Define the methods of the class
    def Info(Fruit,Self):
        msg = "\nName: {}\nCentrally located: {}\nColor when ripe: {}\nIs messy?: {}\nIs delicious?: {}".format(Fruit.name,Fruit.origin,Fruit.ripe_color,self.messy,self.delicious)
        return msg



#Invokes the methods inside class Kiwi Mango
if __name__ == "__main__":
    Kiwi = Kiwi()
    print(Kiwi.Info())


