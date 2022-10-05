class Person:
    def  __init__(self,name,age,address,city,mobile):
        self.name = name
        self.age = age
        self.address = address
        self.city = city
        self.mobile = mobile

    def display_details(self):
        print("\"Below are the details you entered:\n Name = {}\n Age =  {}\n Address = {}\n City = {}\n Mobile No = {}\"".format(self.name,self.age,self.address,self.city,self.mobile))
        

def create():
    name = input("Enter Your  Name: ")
    age = input("Enter Your Age: ")
    address = input("Enter Your Address: ")
    city = input("Enter  Your City: ")
    mobile = input("Enter Your Mobile Number: ")
    return Person(name, age, address,city,mobile)

Person_one = create()
Person_one.display_details()