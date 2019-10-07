class User:
    '''
    class that generates new instances of users
    '''
    users = []
    status=""
    
    def __init__(self,name,password):
        '''
        __init__ method that allows us to define properties for our objects.

        Args:
            name: New user name
            password: New user password
        '''
        self.name = name
        self.password = password

    def save_users(self):
        '''
        save_users method saves users objects into users list
        '''

        User.users.append(self)
    @classmethod
    def existing_user(cls,name):
        '''
        Existing user method checks if the user exists in the user list
        Args: name - to search whether the name exists in the user list
        Returns:
        Boolean: true or false depending on whether or not a user account exists.
        '''
        for user in cls.users:
            if user.name == name:
                return True
        return False
    

        