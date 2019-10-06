class Credential :
    '''
    class that generates new instances of credentials
    '''
    credential_list = [] 
    def __init__(self,title,username, password):
        '''
        __init__ method that allows us to define properties for our objects.

        Args:
            title: New credential title
            username: New credential username
            password: New credential password
        '''
        self.title = title
        self.username = username
        self.password = password

    def save_credential(self):
        '''
        save_credential method saves contact objects into credential_list
        '''

        Credential.credential_list.append(self)

    def delete_credential(self):

        '''
        delete_credential method deletes a saved contact from the contact_list
        '''

        Credential.credential_list.remove(self)

    @classmethod
    def find_by_title(cls,title):
        '''
        Method that takes in the title and returns a credential that matches that title.

        Args:
            title: title to search for
        Returns :
            Credential hat matches that title
        '''
        for credential in cls.credential_list:
            if credential.title == title:
                return credential

    @classmethod
    def credential_exist(cls,title):
        
        '''
        Method that checks if a contact exists from the contact list.

        Args :
            title : title to search if it exists
        Returns : 
        Boolean: True or false
        depending if the credential exists
        '''
        for credential in cls.credential_list:
            if credential.title == title:
                return True

        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns a list of credentials
        '''

        return cls.credential_list