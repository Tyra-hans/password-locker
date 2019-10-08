#!/usr/bin/env python3.6
from passlock import Credential
from user import User

def create_users(name,password):
    '''
    Function to  create new users
    '''
    new_user = User(name,password)
    return new_user

def save_users(self,user):
    '''
    Function to save Users
    '''
    user.save_users(user)
def existing_userslist(name,password):
    '''
    Function to check if users exist
    '''
    exist = User.existing_user(name,password)
    return exist

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
        exist= existing_userslist(name,password)
        while True:
        # if name in User.users and User.users == password:
            print('Login successful!')
            print(f"Hello {name}. what would you like to do?")
            print('\n')
        else:
            print('\n This user doesnt exist or incorrect password \n')
            status = input("Hello Welcome to Password locker. Already have an account? (y/n)")
            if status == 'n':
                create_name = input('Create username: ')
                name = create_name
                create_password = input('Create password: ')
                password = create_password
                existing = existing_userslist(name,password)
                print('\n Please Login\n')
                name = input('Enter login name: ')
                password = input ('Enter password: ')
                print('Login successful!')
                print(f"Hello {name}. what would you like to do?")
                print('\n')
                #==== to input the create login logic ====
            

    elif status == 'n': 
        create_name = input('Create username: ')
        name = create_name
        create_password = input('Create password: ')
        password = create_password
        # existing = existing_userslist(name,password)
    while True:
        # if create_name in User.users:
        # print('Name already exists!')
            #the user is directed to login here
        print('*'*60)
        print(f"Account created successfully.You username is {name} and password is {password} ")
        print('*'*60)
        
        print('\n Proceed to login\n')
        name = input('Enter login name: ')
        password = input ('Enter password: ')
        existing = existing_userslist(name,password)
        if existing == name:
            # if name in User.users and User.users == password:
            print('Login successful!')
            print(f"Hello {name}. what would you like to do?")
            print('\n')
        else:
            print('Acount doesnt exist..Please create an account')
            create_name = input('Create username: ')
            name = create_name
            create_password = input('Create password: ')
            password = create_password

        
        # else :
        #     # print("your account doesnt exist..Create one")
        #     # password = input('Create password: ')
        #     # User.users = password
        #     # user = create_users(name, password)
            # user.save_users(user)
            

        # print('\n account created !\n')
        # name = input('Enter login name: ')
        # password = input ('Enter password: ')
        # print(f"Hello {name}. what would you like to do?")
        # print('\n')
        #     # else:
            #     print('\n This user doesnt exist or incorrect password \n')
            #     status = input("Hello Welcome to Password locker. Already have an account? (y/n)")
            

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
                                    print(f"title: {credential.title}.. username {credential.username}..password:{credential.password}")

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