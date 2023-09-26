




class Payment:
    def __init__(self, Q, P, N, D) -> None:
        self.Q = Q
        self.P = P
        self.N = N
        self.D = D
        
    def amtPaid(self):
       cents = (self.Q * 25) + (self.D * 10) + (self.N * 5)  + self.P  
       return cents / 100
