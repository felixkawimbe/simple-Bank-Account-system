class Bank_Account:
	def __init___(self):
		self.balance=0
		print("welcome to Bank account sample ")
	#deposit funiction
	def deposit(self):
		amout=float(input("Enter amount to Deposition.K"))
		self.balance +=amount
		print("/n Amount Deposition:k",amount)
	#withdraw function
    def withraw(self):
    	amount=float(input("Enter amount to be withdrawn"))
    	if self.balance>=amount:
    		self.balance-=amount
    		print("/n Your Withdraw is :k",amount)
    	else:
    		print("/n insufficient balance")
    def display(self):
    	print("/n Net Available balance :K",self.balance)
 s=Bank_Account()
 s.deposit()
 s.withdraw()
 s.display()