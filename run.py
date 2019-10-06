#!/usr/bin/env python3.6
from passlock import Credential

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
    credential.save_credentials()
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