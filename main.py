import certifi
from pymongo import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient("mongodb+srv://user:pzcPKYCyH3iTJl1y@cluster0.bvru9z5.mongodb.net/?retryWrites=true&w=majority",
                     server_api=ServerApi('1'), tlsCAFile=certifi.where())
db = client["database"]
collection = db["users"]
print(f"Database loaded with {collection.count_documents({})} users")
current_user = None


def does_user_exist(username) -> bool:
    # TODO implement this function
    return bool(collection.find_one({"username": username}))


def register_user(username, password):
    # TODO implement this function
    collection.insert_one({"username": username, "password": password, "balance": 0})


def signup():
    username = input("Please enter your username:")
    user_exists = does_user_exist(username)
    while does_user_exist(username):
        username = input("Sorry! This user already exists\nPlease enter your "
                         "username:")
    password = input("Please enter your password:")

    register_user(username, password)
    print("User registered successfully!")


def fetch_user(username):
    # TODO fetch the user from the database
    return collection.find_one({"username": username})


def get_valid_int_input(request):
    inp = input(request)
    while not inp.isnumeric():
        inp = input(f'Please enter a valid non-negative int!\n{request}')
    return int(inp)


def signin():
    username = input("Please enter your username:")
    user = fetch_user(username)
    while not user:
        username = input("Sorry! This user does not exist\nPlease enter your "
                         "username:")
        user = fetch_user(username)
    password = input(f"Please enter the password for user {username}")
    while password != user["password"]:
        password = input(f"Password incorrect! Please enter the password for "
                         f"user {username}")
    global current_user
    current_user = user
    print(f"Welcome {username}!")


def deposit():
    global current_user

    amount = get_valid_int_input("Please enter deposit amount")
    # TODO update database
    collection.update_one({"username": current_user["username"]}, {"$inc": {"balance": amount}})

    current_user = fetch_user(current_user["username"])


def withdraw():
    global current_user

    amount = get_valid_int_input("Please enter withdraw amount")
    # TODO update database
    collection.update_one({"username": current_user["username"]}, {"$inc": {"balance": -amount}})

    current_user = fetch_user(current_user["username"])


def signout():
    global current_user
    current_user = None


user_functions = {
    "deposit": deposit,
    "de": deposit,
    "withdraw": withdraw,
    "wd": withdraw,
    "signout": signout,
    "so": signout
}
if __name__ == '__main__':
    print("""
      __  __          _____            _   ____              _     
 |  \/  |        / ____|          | | |  _ \            | |    
 | \  / |_   _  | |     ___   ___ | | | |_) | __ _ _ __ | | __ 
 | |\/| | | | | | |    / _ \ / _ \| | |  _ < / _` | '_ \| |/ / 
 | |  | | |_| | | |___| (_) | (_) | | | |_) | (_| | | | |   <  
 |_|  |_|\__, |  \_____\___/ \___/|_| |____/ \__,_|_| |_|_|\_\ 
          __/ |                                                
         |___/                                                 
    """)
    print("Welcome my cool bank, you can make your account and manage your "
          "money!\nTo exit this application at any time just type \"exit\"")
    user_inp = ""
    while user_inp != 'exit':
        user_inp = ''
        if not current_user:
            user_inp = input("Would you like to sign-in (SI) or sign-up (SU)?: ")
            if user_inp.lower() == 'si':
                signin()
            elif user_inp.lower() == 'su':
                signup()
            elif user_inp.lower() == 'exit':
                break
            else:
                print('Please enter a valid option')
        else:
            print(f"Hi {current_user['username']}, your balance is ${current_user['balance']}")
            user_inp = input("Please either withdraw (WD), deposit (DE), signout (SO) or exit: ")
            if user_inp.lower() in user_functions:
                user_functions[user_inp.lower()]()
            elif user_inp.lower() == 'exit':
                break
            else:
                print('Please enter a valid option')
