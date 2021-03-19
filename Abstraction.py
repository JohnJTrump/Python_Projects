#
#
#   Python version: 3.9.2
#
#   Author: John Trump 
#           
#   Purpose:    -Step #272 in Python Course
#               -Abstraction challenge
#                   - Create class using abstraction concept
#                   - class should contain atleast on abstract method and one regular method
#                   - create child class that defines the implementation of its parents abstract method
#                   - create object that utilizes both parent and child methods0
#
#





from abc import ABC, abstractmethod # importing for use the Abstract Base Class(ABC)
class fancy(ABC): # creating a class with the imported method
    def yourStatus(self, image): # defining parent method which pulls in abstract obj for use
        print("Your overall appearance: ",image) # using parent method to print string with an abstract object 
    @abstractmethod # calling ABC for use
    def critique(self, image): # defining abstract child method ????
        pass


class TodaysAppearance(fancy): # creating second class
    def critique(self, image): # defining method which pulls in abstract obj for use
        print('Your overall appearance of {} is limiting your ability to assimilate.'.format(image))


obj = TodaysAppearance() # calling the method for use 
obj.yourStatus("dirty") # imputing data into a method
obj.critique("dirty") # imputing data into another method
