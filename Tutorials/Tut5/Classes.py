# class Dog:
#     def __init__(self,name,colour,Age):
#         self.colour = colour
#         self.age = Age
#         self.name = name

# rocky = Dog("Rocky","Black",5)
# snowhite = Dog("Snowhite","White",8)

# print(rocky.name,rocky.colour,rocky.age)
# print(snowhite.name,snowhite.colour,snowhite.age)


# class Human:
#     school = "KMPS"
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# human1 = Human("Anita",20)    
# human2 = Human("Kshma",20)    
# human3 = Human("Dhruv",20)    
# human4 = Human("Madhav",12)    
# print(human1.school,human1.name, human1.age)    
# print(human1.school,human2.name, human2.age)    
# print(human1.school,human3.name, human3.age)    
# print(human1.school,human4.name, human4.age)    

# human1.school = "RATM"
# print(human1.school,human1.name, human1.age)    


# class company:
#     company_name = "Apple"
#     def __init__(self,employee_name,employee_salary):
#         self.name = employee_name
#         self.salary = employee_salary

#     def show_info(self):
#         print(f"Name : {self.name} | Salary : {self.salary} | Company : {self.company_name}")


# Anita = company("Anita",100000)
# Anita.show_info()
# # Anita.company_name = "NASA"
# # Anita.salary = 200000000
# Dhruv = company("Dhruv",90000)
# Dhruv.show_info()

# # print(Anita.company_name,Anita.name,Anita.salary)
# # print(Dhruv.company_name,Dhruv.name,Dhruv.salary)

# class car:
#     # def __init__(self):
#     #     print("Hello World!")
#     def add_car_info(self,car_name,car_brand):
#         self.name = car_name
#         self.brand = car_brand
#     def show_info(self):
#         print(f"Car Name : {self.name} and Car Brand : {self.brand}")



# obj = car()
# # print(obj.name)
# obj.add_car_info("Tesla Model X","Tesla")
# print(obj.name)
# obj.show_info()
# obj1 = car()
# obj2 = car()
# obj3 = car()
# obj4 = car()
# obj5 = car()
# obj6 = car()
# obj7 = car()

# class dog:
#     breed = "Labrador"
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     @classmethod
#     def change_breed(cls,breed1):
#         cls.breed = breed1    
#     def show_kutte_ki_info(self):
#         print(f"Name : {self.name} | Age : {self.age} | Breed : {self.breed}") 

#     def barking(self):
#         print(f"{self.name} Is barking") 

# rocky = dog("rocky",7)  
# rocky.show_kutte_ki_info() 
# rocky.change_breed("Pomelion")      
# rocky.show_kutte_ki_info() 
# rocky.barking()  



#-- Single Inheritance
# class animal:
#     def sound(self):
#         print(f"{self.name} Making Sound")

# class dog(animal):
#     def __init__(self,name):
#         self.name = name


# dog1 = dog("Shishimanu")
# print(f"{dog1.name}")
# dog1.sound()


#--Multilevel Inheritance


# class animal:
#     def make_sound(self):
#         print(f"{self.name} Making Sound")

# class dog(animal):
#     def __init__(self,name):
#         self.name = name

# class cat(dog):
#     def show_info(self):
#         print(f"{self.name} is a cat")


# obj1 = cat("Kio")
# print(obj1.name)
# obj1.make_sound()

#-- Heirarchial Inheritance

# class pitashree:
#     pitaji_salary = 100000 
#     def earning(self):
#         print(f"Pitaji Is Earning ${self.pitaji_salary} | {self.name} is Earning ${self.salary}")

# class betaji1(pitashree):
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def show_info1(self):
#         print(self.earning())

# class betaji2(pitashree):
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def show_info2(self):
#         print(self.earning())

# madhav = betaji1("Madhav",20000)
# dhruv = betaji2("Dhruv",50000)


# madhav.earning()
# dhruv.earning()



class dog:
    def sound(self):
        print("Bhau Bhau!")

class cat:
    def sound(self):
        print("Meow Meow!")

class frog:
    def sound(self):
        print("Tar Tar!")

Moti = dog()
Kio = cat()
Kartik = frog()

def make_sound(obj):
    print(obj.sound())
    

make_sound(Moti)    
make_sound(Kio)    
make_sound(Kartik)    