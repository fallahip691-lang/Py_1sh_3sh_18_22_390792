

from store import *
from wish_and_basket import *
admin={}
admin = {"user": "parsa", "password": "1386"}
user={}
users=[]
products = {}
def login(username=str,password=str):
    
    while True:
        Menu=input("1.login 2.sighn in 3.exit")
        match Menu:
            case "1":
                
                if user_name == admin["user"] and password == admin["password"]:
                    store(products)

                elif user_name == user["user"] and password == user["password"]:
                        wish_and_basket(basket)  
                else:
                    print("user not found")
                

            case "2":
                user_name=input("user name")
                password=input("password")
                credit=int(input("credit:"))
                user={"user":user_name,"password":password,"credit":credit}
                print(user)
            case 3:
                break



