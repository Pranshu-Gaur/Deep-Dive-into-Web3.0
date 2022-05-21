#Parent Class 
class User(): 
    def __init__ (self, first_name, last_name, age, date_of_birth, gender):
        self.name = first_name + ' '+ last_name
        self.age = age
        self.dob = date_of_birth
        self.gender = gender
        
    def show_details (self):
        print ("Personal Details")
        print ("")
        print ("Name:", self.name)
        print ("Age:", self.age)
        print ("Date of Birth:", self.dob)
        print ("Gender:", self.gender)
        
#Child Class
class Bank (User):
    def __init__ (self, first_name, last_name, age, date_of_birth, gender):
        super().__init__(first_name, last_name, age, date_of_birth, gender)
        self.balance = 0
        self.to_receive = 0
        
    def deposit (self, amount):
        self.amount = amount
        self.balance = self.balance + self. amount
        print("Account balance has been updated : ₹", self.balance)
        
    def withdraw (self, amount):
        self. amount = amount
        if self. amount > self.balance:
            print("Insufficient Funds | Balance Available : ₹", self.balance)
        else:
            self.balance = self.balance - self.amount
            print ("Account balance has been updated : ₹", self.balance)
            
    def view_balance (self):
        self.show_details ()
        print ("Account balance: ₹", self.balance)

#Borrower
class Lender(Bank):
    
    def __init__ (self, first_name, last_name, age, date_of_birth, gender):
        super().__init__(first_name, last_name, age, date_of_birth, gender)
        self.time = 0
        self.loan_amount = 0
        
    def borrow (self, borrow_amount, days):
        self.time += days
        if self.balance > 2*borrow_amount:
            self.balance -= borrow_amount
            self.to_receive += borrow_amount
            self.loan_amount += borrow_amount
            print ("Request has been approved!")
            print ("Kindly return the money within", days ,"days or else a fine of", borrow_amount/2,"will be imposed")
            
        else:
            print ("Cannot approve Request as the Requested Amount is too high!")
    
    def loan (self, loan_amount, days):
        self.time += days
        
        
        #Let Rate for Loan = 2% per day
        
        amount = loan_amount + loan_amount*days*2/100
        self.loan_amount += amount
        
        if loan_amount > self.balance:
            print("Requested Loan Amount is too high!", self.balance)
            
        else:
            print("Loan has been approved!")
            print("Amount to be returned after", days,"days is", amount)
            self.balance -= loan_amount
            self.to_receive += amount
    
    def return_amount (self, amount, days_after_loan):
        
        if days_after_loan > self.time:
            print("You are late in returning the Amount!")
            print("Returnable amount is", 1.5*self.loan_amount)
            if amount > 1.5*self.loan_amount:
                self.balance +=1.5*self.loan_amount
                self.to_receive -= 1.5*self.loan_amount
                self.loan_amount = 0
                print("Amount has been returned, you receive back the extra amount: ",amount-1.5*self.loan_amount)
            else:
                self.balance +=amount
                self.loan_amount = 1.5*self.loan_amount - amount
                self.to_receive -= 1.5*self.loan_amount - amount
                print("Amount has been accepted, Amount still remaining to return: ",self.loan_amount)
        
        else: 
            if amount > self.loan_amount:
                print("Amount has been returned, you receive back the extra amount: ",amount-self.loan_amount)
                self.balance +=self.loan_amount
                self.to_receive -= self.loan_amount
                self.loan_amount = 0
            else:
                self.balance +=amount
                self.loan_amount = self.loan_amount - amount
                self.to_receive -= amount
                print("Amount has been accepted, Amount still remaining to return: ",self.loan_amount)
                
    def view_current_state (self):
        
        print ("Account balance: ₹", self.balance)
        print ("Amount yet to receive: ₹", self.to_receive)
        print ("Amount lended: ₹", self.loan_amount)