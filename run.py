#!/usr/bin/env python3.6
from passlock import Credential
from user import User

def create_users(name,password):
    '''
    Function to  create new users
    '''
    new_user = User(name,password)
    return new_user

def save_users(user):
    '''
    Function to save Users
    '''
    user.save_users(user)
def create_credentials(title,username,password):
    '''
    Function to create new Credentials
    '''
    new_credential = Credential(title,username,password)
    return new_credential

def save_credentials(credential):
    '''
    Function to save credentials
    '''
    credential.save_credential()
def del_credential(credential):
    '''
    Function to delete credentials
    '''
    credential.delete_credential()

def find_credential(title):
    '''
    Funtion that finds a credential by title and returns
    the credential
    '''
    return Credential.find_by_title(title)


def check_existing_credentials(title):
    '''
    function that checks if the credential exists
    with that title and return a boolean
    '''
    return Credential.credential_exist(title)

def display_credentials():
    '''
    Function that returns all the saved credentials 
    '''
    return Credential.display_credentials()


def main():
   
    status = input("Hello Welcome to Password locker. Already have an account? (y/n) q:exit")
    if status == 'y': 
        name = input('Enter login name: ')
        password = input ('Enter password: ')

        if name in User.users and User.users == password:
            print('Login successful!')
            print(f"Hello {name}. what would you like to do?")
            print('\n')
        else:
            print('\n This user doesnt exist or incorrect password \n')
            status = input("Hello Welcome to Password locker. Already have an account? (y/n)")
            

    elif status == 'n': 
        create_name = input('Create username: ')

        if create_name in User.users:
            print('Name already exists!')
            name = input('Enter login name: ')
            password = input ('Enter password: ')
            
            if name in User.users and User.users == password:
                print('Login successful!')
                print(f"Hello {name}. what would you like to do?")
                print('\n')

        else :
            password = input('Create password: ')
            # User.users = create_password
            save_users(create_users(name,password))

            print('\n account created !\n')
            login = input('Enter login name: ')
            password = input ('Enter password: ')

            if login in User.users and User.users[login] == password:
                print('Login successful!')
                print(f"Hello {login}. what would you like to do?")
                print('\n')
            else:
                print('\n This user doesnt exist or incorrect password \n')
                status = input("Hello Welcome to Password locker. Already have an account? (y/n)")
            

    while status != 'q':
            print("Use these short codes : cc - create a new credential, dc - display credential, fc -find a credential, ex -exit the credential list ")

            short_code = input().lower()

            if short_code == 'cc':
                    print("New Credential")
                    print("-"*10)

                    print ("Title ....")
                    title = input()

                    print("Username")
                    user_name = input()

                    print("Password ...")
                    password = input()

                    


                    save_credentials(create_credentials(title,user_name,password)) # create and save new contact.
                    print ('\n')
                    print(f"New Credential {title} {user_name} created")
                    print ('\n')

            elif short_code == 'dc':

                    if display_credentials():
                        print("Here is a list of all your credentials")
                        print('\n')

                        for credential in display_credentials():
                                    print(f"{credential.title} {credential.username} .....{credential.password}")

                        print('\n')
                    else:
                                    print('\n')
                                    print("You dont seem to have any credentials saved yet")
                                    print('\n')

            elif short_code == 'fc':

                            print("Enter the title you want to search for")

                            search_credential = input()
                            if check_existing_credentials(search_credential):
                                    search_credential = find_credential(search_credential)
                                    print(f"{search_credential.username} {search_credential.password}")
                                    print('-' * 20)

                                
                            else:
                                    print("That credential does not exist")

            elif short_code == "ex":
                    print("Bye .......")
                    break
            else:
                    print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()