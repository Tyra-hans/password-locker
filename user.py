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

    def login(self):
        '''
        login method allows users to login
        '''
        


