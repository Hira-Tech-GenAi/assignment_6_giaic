#? 4. Class Variables and Class Methods
#?Assignment:
#?Create a class Bank with a class variable bank_name. Add a class method #?change_bank_name(cls, name) that allows changing the bank name. Show that it affects #?all instances.

class Bank:
  bank_name:str = "world bank"

  @classmethod
  def change_bank_name(cls, name):
    cls.bank_name = name

  def display(self):
    print(f"New Bank is: {Bank.bank_name}")

bank1 = Bank()
print(bank1.bank_name)
Bank.change_bank_name("hira bank")
bank1 = Bank()
bank1.display()