#Parent Class "User"
class User:
    name = "Mark"
    email = "mark@gmail.com"
    password = "1234abcd"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(entry_name))
        else:
            print("The password or email is incorrect.")


