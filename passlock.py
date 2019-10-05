class User:
    '''
    Class that allows users to sign up and create a 
    password and username for themselves
    '''
    sign_up_info = []
    def __init__(self,username,password):

        self.username = username
        self.password = password