import certifi
from pymongo import MongoClient
from pymongo.server_api import ServerApi

# TODO Connect to the database and get the users collection

current_user = None


def does_user_exist(username) -> bool:
    """
    Checks if the <username> already exists in the database
    :param username: the username to check
    :return: True if it does exist, otherwise False
    """
    # TODO implement this function
    pass


def register_user(username, password):
    """
    Register the user with <username> and <password> into the database
    :param username: the user's username
    :param password: the user's password
    :return: None
    """
    # TODO implement this function
    pass


def signup():
    """
    Allows a user to register an account if the username does not already exist
    :return: None
    """
    username = input("Please enter your username:")
    while does_user_exist(username):
        username = input("Sorry! This user already exists\nPlease enter your "
                         "username:")
    password = input("Please enter your password:")

    register_user(username, password)
    print("User registered successfully!")


def fetch_user(username):
    """
    Get the user with <username> fromt the database
    :param username: username to fetch
    :return: the document with the <username>
    """
    # TODO fetch the user from the database
    pass


def signin():
    """
    Signs in to the user's bank account, confirms whether their username and
    password are valid
    :return: None
    """
    username = input("Please enter your username: ")
    user = fetch_user(username)
    while not user:
        username = input("Sorry! This user does not exist\nPlease enter your "
                         "username: ")
        user = fetch_user(username)
    password = input(f"Please enter the password for user {username}: ")
    while password != user["password"]:
        password = input(f"Password incorrect! Please enter the password for "
                         f"user {username}: ")
    global current_user
    current_user = user
    print(f"Welcome {username}!")


def get_valid_int_input(request: str):
    """
    A helper function to get an input from a user and check if it is numeric
    :param request: a string message for the requested input
    :return: the valid integer input
    """
    inp = input(request)
    while not inp.isnumeric():
        inp = input(f'Please enter a valid non-negative int!\n{request}: ')
    return int(inp)


def deposit():
    """
    Prompt the user to enter an amount they want to deposit to their account,
    then update the user's balance in the database
    :return: none
    """
    # TODO: update the database
    pass


def withdraw():
    """
    Prompt the user to enter an amount they want to withdraw to their account,
    then update the user's balance in the database
    :return: none
    """
    # TODO: update the database
    pass


def signout():
    """
    Signs out of the user's account
    :return: none
    """
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
            user_inp = input("Would you like to sign-in (SI) or sign-up (SU)?: "
                             "")
            if user_inp.lower() == 'si':
                signin()
            elif user_inp.lower() == 'su':
                signup()
            elif user_inp.lower() == 'exit':
                break
            else:
                print('Please enter a valid option')
        else:
            print(f"Hi {current_user['username']}, your balance is "
                  f"${current_user['balance']}")
            user_inp = input("Please either withdraw (WD), deposit (DE), "
                             "signout (SO) or exit: ")
            if user_inp.lower() in user_functions:
                user_functions[user_inp.lower()]()
            elif user_inp.lower() == 'exit':
                break
            else:
                print('Please enter a valid option')
