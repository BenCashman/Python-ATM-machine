#creat the base class for account
class Account:
  def __init__(self,name,balance,min_balance):
    self.name = name
    self.balance = balance
    self.min_balance = min_balance

#function to allow a person to make a deposit
  def deposit(self, amount):
    self.balance += amount

#Function to allow a person to make a withdrawal
  def withdraw(self,amount):
    if (self.balance - amount) >= self.min_balance:
      self.balance -= amount
    else:
      print("Sorry, you don't have enough money")

  def statement(self):
      print("You currently have {} in your account".format(self.balance))

#Child class of the account class - create new accounts with generous over draft
class Current(Account):
  def __init__(self,name,balance):
    super().__init__(name,balance,min_balance = -1000)
  def __str__(self):
    return "{} is the account holder, Balance is : {}".format(self.name,self.statement)

#Child class where we set min balance at 0
class Savings(Account):
  def __init__(self,name,balance):
    super.__init__(name,balance,min_balance = 0)

  def __str__(self):
    return "{} is the savings account holder, Balance is : {}".format(self.name,self.statement)
