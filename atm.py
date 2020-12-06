class Atm(object):
    def __init__(self):
        self.amount=0
    def enterAccount(self):
        cardno=input('Enter card number: ')
        pin=input('Enter pin: ')
    def depositMoney(self): 
        deposit = input('Enter amount to be deposited: ')
        amount=amount+deposit
        print("\n Amount Deposited:", deposit)    
    def withdrawMoney(self):
        withdraw=input('Enter amount to be withdrawn: ')    
        if withdraw<=amount:
            print('Successfully withdrew',withdraw)
        else:
            print('Insufficient balance')    
newatm = Atm()
         

        
