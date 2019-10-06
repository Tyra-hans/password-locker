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
