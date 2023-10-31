from abc import ABC,abstractmethod
import re


class Person(ABC):
    def __init__(self,fn,ln,ct,id):  # Constructor
        self.first_name = fn
        self.last_name = ln
        self.contact = ct
        self.email = id

    @abstractmethod   # abstract method
    def display_car(self):
        pass


class PremiumCars(Person):  # Inheritance

    def display_car(self):   # polymorphism  ,   Encapsulation
        _premium_car_list = ["Maserati","Ferrari","BMW","Mercedes","Jaguar"]
        __price = [6120000,3515600,1120900,3690000,4620000]    # duck typing, access specifiers
        __car_prices = dict(zip(_premium_car_list, __price))   # duck typing, access specifiers
        print(__car_prices)
        premium_car_dict = {i + 1: _premium_car_list[i] for i in range(len(_premium_car_list))} # dict comprehension
        print(premium_car_dict)
        user_choice = int(input("Please select option you like to go ahead with :"))
        bought_car = _premium_car_list[user_choice-1]
        price_of_bought_car = __price[user_choice-1]
        print(f"You have opted for {bought_car}")
        yes_or_no = input("Are you sure you want to buy this car ? y/n")
        print("Congratulation !!") if yes_or_no == "y" else print("Thanks, See you again!!!")
        full_name = self.first_name + " " + self.last_name   # Inheritance
        print(f"""Name : {full_name} 
Contact : {self.contact}
Email Address : {self.email}
Bought : {bought_car} With Price {price_of_bought_car}
                """)


class AffordableCars(Person):  # Inheritance
    def display_car(self):  # polymorphism     ,     Encapsulation
        _affordable_car_list = ["Tata", "Honda", "Kia", "Suzuki", "Hyundai"]
        __price = [612000, 351560, 112090, 369000, 462000]          # duck typing, access specifier
        __car_prices = dict(zip(_affordable_car_list, __price))     # duck typing, access specifier
        print(__car_prices)
        affordable_car_dict = {i + 1: _affordable_car_list[i] for i in range(len(_affordable_car_list))} # dict comprehension
        print(affordable_car_dict)
        user_choice = int(input("Please select option you like to go ahead with :"))
        bought_car = _affordable_car_list[user_choice - 1]
        price_of_bought_car = __price[user_choice - 1]
        print(f"You have opted for {bought_car}.")
        yes_or_no = input("Are you sure you want to buy this car ? y/n")
        print("Congratulation !!") if yes_or_no == "y" else print("Thanks, See you again!!!")
        full_name = self.first_name + " " + self.last_name     # Inheritance
        print(f"""Name : {full_name} 
Contact : {self.contact}
Email Address : {self.email}
Bought : {bought_car} With Price {price_of_bought_car}
                """)


def get_user_details():
    f_name = input("Enter your first name : ")
    l_name = input("Enter your last name : ")
    while True:
        ct = input("Enter your 10-digit contact number: ")
        ct_lambda = lambda x, y: re.fullmatch(x, y)     # lambda function
        pattern = r'^\d{10}$'   # regular expression
        if ct_lambda(pattern,ct):
            break
        else:
            print("Invalid contact number. Please enter a 10-digit number.")
    while True:
        mail = input("Enter your email address: ")
        e_lambda = lambda x, y: re.fullmatch(x, y)      # lambda function
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'   # Regular expression
        if e_lambda(pattern,mail):
            break
        else:
            print("Invalid email address. Please enter a valid email.")
    return f_name, l_name, ct, mail


first_name, last_name, contact, email = get_user_details()
c = input("Which option would you like to go with Premium Cars or Affordable Cars? \n "
          "Enter 1. for Premium Cars \n Enter 2. for Affordable cars \n")
if c == "1":
    p = PremiumCars(first_name, last_name, contact, email)
    p.display_car()

elif c == "2":
    print("Here's the list of Affordable cars With their prices!")
    a = AffordableCars(first_name, last_name, contact, email)
    a.display_car()

