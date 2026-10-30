correct_password = "Python123"

name = input("Enter your name: ")
surname = input("Enter your surname: ")
entered_password = input("Enter your password:")

while entered_password != correct_password:
    print("Incorrect password. Try again.")
    entered_password = input("Enter your password:")

message = "Hi %s %s, your password is correct." % (name, surname)
print(message)