from cryptography.fernet import Fernet

'''def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_f:
        key_f.write(key)
write_key()'''

'''by using {with}keyword you dont need close file'''


def return_key():
    with open('key.key', 'rb') as key_f:
        key = key_f.read()
    return key


print("Welcome to the password manager !!")

'''encode is used to convert from string to bytes and decode vice versa'''
key = return_key().decode()
fer = Fernet(key)


def add():
    user_name = input("UserName : ")
    pwd = input("Password : ")

    with open('pass.txt', 'a') as f:
        f.write(user_name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")
    f.close()


def view():
    with open("pass.txt", 'r') as f:
        for line in f.readlines():
            data = line.strip()
            user_name, password = data.split("|")
            print("Username: " + user_name + "|" + "Password: " + fer.decrypt(password.encode()).decode())


while True:
    val = input("\n\nWould you like to \n1.add\n2.view\n3.quit\nfrom password manager ? Enter the choice: ").lower()
    if val == 'quit':
        print("Password manager is exited")
        break
    elif val == 'add':
        add()
    elif val == 'view':
        view()
    else:
        print("Invalid !!")
