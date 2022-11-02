from datetime import datetime

class User():
    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password
    
    def welcome(self):
        print("Welcome, {}".format(self.user_name))
    
    def check_password(self,password):
        if password == "12345":
            return True
        else:
            return False
    

class SubscribedUser(User):
    def __init__(self,user_name,password,time_subscribe):
        User.__init__(self,user_name,password)
        self.time_subscribe = time_subscribe
    
    def check_password(self,password):
        if password == "1234":
            return True
        else:
            return False

    def is_expired(self):
        if self.time_subscribe > datetime.now():
            return True
        else:
            return False
    
# user = User('mindx', '12345')
# user.welcome()
# print(user.check_password('12345'))

s_user = SubscribedUser('s_mindx', '1234', datetime(2021, 3, 3))
s_user.welcome()
print(s_user.check_password('1234'))
print(s_user.is_expired())

    