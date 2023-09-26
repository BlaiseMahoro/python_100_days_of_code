
from resources import Resources
from cashDrawer import CashDrawer
from report import Report
from Payment import Payment

W = 100
M = 50
C = 76
M = 2.5


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


    
class CoffeeMachine:
    def __init__(self) -> None:
         
        self.resources = Resources(W, M, C)
    
        self.cashDrawer = CashDrawer(M)
    
        self.report = Report(self.resources, self.cashDrawer)
    
    
    def handleUserInteraction(self):
        
        userChoice = input('What would you like? (espresso/latte/cappuccino). Type "report" to see the available resources and "off" to exit. \n')
        
        if userChoice.strip().upper() == 'OFF':
            print('Thank you for using Me!')
            exit(0)
            
        if userChoice.strip().upper() == 'REPORT':
            self.report.print()
            return
            
        if userChoice.strip().upper() not in {'ESPRESSO', 'LATTE', 'CAPPUCCINO'}:
            print('Invalid selection.... Try again')
            return 
        selectedBeverage = userChoice.strip().lower()
        
        self.resources.resourcesEnough(selectedBeverage)
        
        amtDue = MENU[selectedBeverage]['cost']
        print('Insert this amount : $ ', MENU[selectedBeverage]['cost'])
        
        Q = int(input('Enter the number of Quarters: '))
        D = int(input('Enter the number of Dimes: '))
        N = int(input('Enter the number of Nickels: '))
        P = int(input('Enter the number of Pennies: '))
        
        payment = Payment(Q, P, N, D)
        
        amtTendered = payment.amtPaid()
        
        print('You inserted $ ', amtTendered)
        if amtTendered < amtDue:
            print('Sorry that\'s not enough money. Money Refunded')
            return
        
        if amtTendered > amtDue:
            print('You paid too much money. Refunded $ ', round(amtTendered - amtDue, 2))
            
        self.resources.reduceResourceByBeverage(selectedBeverage)
        

        self.cashDrawer.addAmt(amtDue)
        
        
        
        
          
         
        