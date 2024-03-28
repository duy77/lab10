#import os
#print(os.getcwd())  # Check current working directory (must cd to lab5)

import json

class customers:
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name= last_name

    def to_json(self):
        return json.dumps({
            "user_id": self.user_id,
            "first_name": self.first_name,
            "last_name": self.last_name,   
        },indent=2)

john = customers(1, 'john', 'smith')

print(john.to_json())  

class accounts:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance

    def to_json(self):
        return json.dumps({
            "account_id": self.account_id,
            "balance": self.balance       
        },indent=2)
        
john_account = accounts(1, 5000)
print(john_account.to_json())

class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def remove_customer(self, customer):
        self.customers.remove(customer)

    def add_account(self, account):
        self.accounts.append(account)

    def remove_account(self, account):
        self.accounts.remove(account)

    def to_json(self):
        customers_json = [customer.__dict__ for customer in self.customers]
        accounts_json = [account.__dict__ for account in self.accounts]
        
        print(customers_json)
        return json.dumps({
            "customers": customers_json,
            "accounts": accounts_json
        },indent=2,separators=(',', ':'))
        
      
        
bank = Bank()
bank.add_customer(john)
bank.add_customer(customers(2, "Jane", "Doe"))
bank.add_account(john_account)

# print(john.to_json())

# print(bank.customers[0].to_json())

print(bank.to_json())





#with open('bank.json') as f:
# data = json.load(f)
#for bank in data['customers']:
#  print(bank['id'],bank['first_name'],bank['last_name'])
    


