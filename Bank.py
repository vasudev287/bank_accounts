##Creating an account system for banker and consumer 
# The banker can add/ deduct balannce balace & loan 
# The consumer can view balance and interest

#######Known bug: Needs to have an entry before adding or editing file 

## the banker can create and check accounts. Need to update the ability to edit records 
## The customer can view records

from sys import exit
from random import randint
import csv
import os 

class Bank_Account (object):

        
                
        def __init__(self, account_number, account_name, balance):
             self.account_number = account_number
             self.account_name = name
             self.account_balance = balance
        def print_statement(self,account_number,account_name):
                print ("Account Details:")
                print ("Account Holder:{}".format(account_name))
                print ("Account Number: {}" .format(account_number))
                print ("Account Balance ")

                 
class Classification (object):          
        def classification_fun(self):
                type = input (""" Welcome to Dena Bank :) 
                                Select the Number based on the type of user: 
                                1)  Banker 
                                2)  Consumer \n >>""")
                if (type == '1'):
                     return Banker.enter(self)
                elif (type == '2'):
                    return Consumer.enter(self)
                else:
                        print("Invalid Choice: Please try again ")
                        return Classification()
                
class Consumer (object):
    def enter(self):
            
            print ("Welcome to Dena Bank.Please __enter__ your credentials")
            account_name = input("\r Account Holder Name: ")
            account_number = input ("\r Account Number: ")
            Var1 = Records.csv_dict_reader("output.csv", account_details)

class Banker (object):
    def enter(self):
            Banker_Credentials = input ("Enter the Admin Password:")
            if Banker_Credentials == "B@nk3r":
                print("Welcome! Please Enter the account details ")
                account_details = input("\r Account Number: ")
                Records.account_details(self,account_details)
                  
                
                
            else:
                print ("Incorrect Credentials! Now Exiting")
                exit(1)
        
        
class Records (object):
        """Add/ Show records of existing customers"""
        def csv_dict_reader (file_obj, keyword):
                
                with open (file_obj, 'r+') as csv_file:
                        reader = csv.DictReader(csv_file, delimiter = ',')
                        
                        count =0
                        for line in reader:
                                count+=1
                                if line ["account_number"] == keyword or line['first_name'] == keyword:
                                        print ("Record Exists!!")
                                        print (line["first_name"], end = '      ')
                                        print (line["last_name"], end = '       ')
                                        print (line['account_number'],  end = '  ')
                                        print (line['balance'],'\n')
                                        
                                        Var3= input("Do you want to modify Balance? Y/N")
                                        if (Var3 == 'Y'):
                                            line['balance'] = input("Enter new balance")
                                            
                                        else:
                                            return 'record_exists'
                                else:

                                        print ("Entered Else Block")
                                        return 'no_record'
                                        
        def csv_write(file_obj, data):
                with open (file_obj, 'a+', newline = '') as csv_file:
                        writer = csv.writer(csv_file, delimiter = ',')
                        writer.writerow(data)
                        
        def account_details (self,account_details):
                
                Var1 = Records.csv_dict_reader("output.csv", account_details)             
                if Var1 == 'no_record':
                        print ("Value of Var1 inside the if statement is{}".format(Var1))
                        Var2= input ("No record exists \n Create one Y/N?  ")
                        if (Var2 == 'Y'):
                            Records.new_account(self)
                        else:
                                print ("Session Expired")
                                return exp.classification_fun()
        def new_account(self):
                dict = {}
                dict['first_name']= input ("Enter First Name")
                dict['last_name'] = input ("Enter Last Name")
                dict['account_number'] = input ("Enter Account Number")
                dict['balance'] = input ("Enter the initial balance")
                print ("Debug",dict)                              
                Records.csv_write("output.csv",dict)
                return Banker.enter(self)        

if __name__ == '__main__':

        print("Object to classification class created.")
        first_line = ['first_name','last_name','account_number','balance']

        if (os.path.isfile('output.csv')) == False:
                with open ('output.csv', 'a+', newline = '') as csv_file:
                        writer = csv.DictWriter(csv_file, delimiter = ',', fieldnames = first_line)
                        writer.writeheader()
                        

        exp = Classification()
        exp.classification_fun()

