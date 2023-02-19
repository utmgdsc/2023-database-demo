# from pymongo import MongoClient

global current_user
# Press the green button in the gutter to run the script.
def does_user_exist(username):
    # TODO implement this function
    pass

def register_user(username, password):
    # TODO implement this function
    pass

def signup():
    username = input("Please enter your username:")
    user_exists = does_user_exist(username)
    while does_user_exist(username):
        username = input("Sorry! This user already exists\nPlease enter your username:")
    password = input("Please enter your password:")

    register_user(username, password)
    print("User registered successfully!")

def fetch_user(username):
    # TODO fetch the user from the database
    pass

def signin():
    username = input("Please enter your username:")
    user = fetch_user(username)
    while not user:
        username = input("Sorry! This user does not exist\nPlease enter your username:")
        user = fetch_user(username)
    password = input(f"Please enter the password for user {username}")
    while password != user["password"]:
        password = input(f"Password incorrect! Please enter the password for user {username}")
    global current_user
    current_user = user
    print(f"Welcome {username}!")

def deposit():
    # TODO
    pass

user_functions = {
    "deposit": deposit,

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
    print("Welcome my cool bank, you can make your account an manage your money!")
    user_inp = ""
    while user_inp != 'exit':
