

class Report:
    def __init__(self, resources, cashDrawer) -> None:
        self.resources = resources
        self.cashDrawer = cashDrawer
        
        
    def print(self):
        print('------------------------ Report ----------------------')
        self.resources.print()
        self.cashDrawer.print()