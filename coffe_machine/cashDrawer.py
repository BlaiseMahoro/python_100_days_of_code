

class CashDrawer:
    def __init__(self, amt) -> None:
        self.amt = amt
        
    def __str__(self) -> str:
        return str(self.amt)
    
    def addAmt(self, amt):
        self.amt += amt
    
    def print(self):
         print(f'''
              Money  : {self}
              ''')