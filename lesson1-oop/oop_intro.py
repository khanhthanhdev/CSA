# class Person():
#     def __init__(self, name, age, height, weight):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight

# person = Person("Thanh", 15, 175, 63)
# print("My name is " + person.name)
# print(f"I am {person.age} years old")
# print(f"I am {person.height} m tall")
# print(f"I am {person.weight} kg heavy")


# class Dog():
#     # Public: name
#     # Protected: _name
#     # Private: __name

#     def __init__ (self):
#         self.name = "Dog"
#         self.__age = 15

# from unicodedata import name


# class Person():
#     def __init__ (self, name, age, address,cls='DDD'):
#         self.__name = name
#         self.__age = age
#         self.address = address
#         self.cls = cls
#     # default parameter đứng cuối cùng, không được đứng trước tham số khác

#     def info(self):
#         return "hello, my name is " + self.__name + " and I am " + str(self.__age) + " years old " + "I live in " + self.address

# person = Person("Thanh", 15, "HN")
# print(person.info())

# EX1:
# name = input("Input your name: ")
# age = int(input("Input your age: "))
# phone_number = input("Input your phone number: ")
# email = input("Input your email: ")
# Id = input("Input your Id: ")
# country = input("Input your country: ")
# class Student():

#     # def __init__(self, name, age, phone_number, email, Id, country):
#     #     self.__name = name
#     #     self.__age = age
#     #     self.__phone_number = phone_number
#     #     self.__email = email
#     #     self.__Id = Id
#     #     self.__country = country


#     __name = "thanh"
#     # Getter
#     @property
#     def get_name(self):
#         return self.__name

#     @get_name.setter
#     def set_name(self, name):
#         self.__name = name

#     # def info(self):
#     #     return "My name is " + self.__name + " and I am " + str(self.__age) + " years old " + "I live in " + self.__country + " and my phone number is " + self.__phone_number + " and my emil is " + self.__email + " and my Id is " + self.__Id

# student = Student()
# student.set_name = "Thanh"
# print(student.get_name)

# EX3:
name = input("Input your name: ")
age = int(input("Input your age: "))
Id = int(input("Input your Id: "))
class Student():
    def __init__(self, name, age, Id):
        self.__name = name
        self.__age = age
        self.__Id = Id
    # Getter
    def get_name(self, name):
        return self.__name

    def get_age(self, age):
        return self.__age

    def get_Id(self,Id):
        return self.__Id

    def setter(self, name, age, Id):
        if name == name and age == age and Id == id:
            print("Trùng")
        else:
            print("ko")
student = Student(name,age,Id)
student.get_name(name)
student.get_age(age)
student.get_Id(Id)

