from abc import ABC,abstractmethod
class Car(ABC):
    def __init__(self,make,model,year,car_type):
        self.make = make
        self.model = model
        self.year = year
        self.type = car_type

    def display(self):
        print(f"You have entered Company : {make}, Model : {model}, Year {year}, Type? :{car_type}")

    @abstractmethod
    def display_car(self):
        pass


class PremiumCars(Car):
    def display_car(self):
        _premium_car_list = ["Masserati","Ferrari","BMW","Mercedes","Jaguar"]
        __price = [6120000,3515600,1120900,3690000,4620000]
        __car_prices = dict(zip(_premium_car_list, __price))
        print(__car_prices)
        for i in range(len(_premium_car_list)):
            print(f"{i+1} : {_premium_car_list[i]}")


        user_choice = int(input("Choose Number of car that you like to buy?"))

        print("CAR = ",_premium_car_list[user_choice-1])
        print("PRICE = ", __price[user_choice-1])
        YN = input("Are you sure you want to buy thsi car ? y/n")

        print("Congratulation !!") if YN =="y"  else print("Chal java mand!!!")


class AffordableCars(Car):
    def display_car(self):
        _afordable_car_list = ["Tata", "Honda", "Kia", "Suzuki", "Hyundai"]
        __price = [612000, 351560, 112090, 369000, 462000]
        __car_prices = dict(zip(_afordable_car_list, __price))
        print(__car_prices)
        for i in range(len(_afordable_car_list)):
            print(f"{i+1} : {_afordable_car_list[i]}")


        user_choice = int(input("Choose Number of car that you like to buy?"))

        print("CAR = ",_afordable_car_list[user_choice-1])
        print("PRICE = ", __price[user_choice-1])
        YN = input("Are you sure you want to buy thsi car ? y/n")

        print("Congratulation !!") if YN =="y"  else print("Chal java mand!!!")


def get_car_details():
    make = input("Enter the company name: ")
    model = input("Enter the model name: ")
    year = int(input("Enter the year: "))
    car_type = input("Enter the type: ")
    return make, model, year, car_type


make, model, year, car_type = get_car_details()


c = input("Premium or Affordable ?  = ")

if c == "Premium":
    p = PremiumCars(make,model,year,car_type)
    p.display_car()

elif c == "Affordable":
    a = AffordableCars(make,model,year,car_type)
    a.display_car()

