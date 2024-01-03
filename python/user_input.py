name =int(input("Enter Your Username: "))
# name = int(name)
print(type(name))

password = input("Enter Your Password: ")

login_success = name == 'ram' and password == "ram@123"
print(login_success)

