from flask import Flask

""" 
    Global variable list  holds  orders , initially its empty
    
"""
orders_db = []


class Order:
    """ Class for modeling orders """

    def __init__(self, food_id,order_id,food_name,location,quantity, status):
        """
            This method acts as a constructor
            for our class, its used to initialise class attributes
        """
        self.order_id = order_id
        self.food_id =food_id
        self.food_name = food_name
        self.location = location
        self.quantity = quantity
        self.status = status

    def place_an_order(self):
        """ 
            This method receives an object of the 
            class, creates and returns a dictionary from the object
        """
        order = {

            "order_id": self.order_id,
            "food_id":self.food_id,
            "food_name": self.food_name,
            "location":self.location,
            "quantity": self.quantity,
            "status": self.status
        }

        orders_db.append(order)
        return order

   
    
