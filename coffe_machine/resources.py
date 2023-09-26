

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

class Resources:
    def __init__(self, w, m, c) -> None:
        self.resources = {"water":w,   "milk":m, "coffee": c}  
        
        
    def reduceResourceByAmt(self, resource, amt):
        if resource not in self.resources or self.resources[resource] < amt:
            raise Exception('Invalid operation! Don\'t have enough of this ingredient ')
        self.resources[resource] -= amt
        
        
    def reduceResourceByBeverage(self, beverage):
        for bev, amt  in MENU[beverage]['ingredients'].items():
            self.reduceResourceByAmt( bev, amt)
        
    def resourcesEnough(self, beverage):
        for resource, amt in MENU[beverage]['ingredients'].items():
            if  amt > self.resources[resource]:
                raise Exception('Sorry there is not enough ', beverage)
    
    
        
    def print(self):
        print(f'''
              Water  : {self.resources['water']}
              Milk   : {self.resources['milk']}
              Coffee : {self.resources['coffee']}
              ''')
        
        