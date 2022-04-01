import os
from tkinter import *

top=Tk()
top.geometry("200x100")

class Atm(object):

    def __init__(self,card,pin):
     self.card = card 
     self.pin = pin 

print("Dear customer, we are honoured to be able to help you.")
print("To start with the procedure please write you secret pin number and card number.")
print("Don't worry this is an ATM so your card wont be hacked:)")
cardNo=input("Please type the card number over here")
pinNo=input("Please type the pin number over here")
customer= Atm(cardNo,pinNo)
fixed = Button(top,text="open or withraw a fixed deposit",activeforeground = "pink",activebackground="white",pady=10)
print("You can now open or withraw your fixed deposit in your atm. No need to stand in long ques of the bank")
recharge = Button(top,text="recharge your mobile",activeforeground = "pink",activebackground="white",pady=10)
print("Want to recharge your mobile. Don't go you are at the correst place")
income = Button(top,text="pay income tax",activeforeground = "pink",activebackground="white",pady=10)
print("Want to pay income tax from ATM. Register this facitlity in our website and have the fun of it.")
deposit = Button(top,text="deposit cash",activeforeground = "pink",activebackground="white",pady=10)
print("Deposit your cash without any hesitation.")
insurance = Button(top,text="pay insurance premium",activeforeground = "pink",activebackground="white",pady=10)
print("You have your policy number handy? Why not pay the insurance here.")
loan = Button(top,text="apply for personal loan",activeforeground = "pink",activebackground="white",pady=10)
print("Want to apply for small personal loans? No need to stand in line for that, just do it over here.")
transfer = Button(top,text="transfer cash",activeforeground = "pink",activebackground="white",pady=10)
print("Not able to access netbanking and wanna transfer money immediately? Don't worry here you can do so.")
pay = Button(top,text="pay your bill",activeforeground = "pink",activebackground="white",pady=10)
print("Want to pay utility bills? Just register the biller on the banks website and you can pay it over here.")
ticket = Button(top,text="book railway ticket",activeforeground = "pink",activebackground="white",pady=10)
print("Book long distance train tickets from here.")