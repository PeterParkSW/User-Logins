#dictionary containing paired usernames and passwords that have been created
#keys are usernames, values are passwords
credentials = {}

#asks user for a new username and password to sign up and put into credentials dictionary
def signup():
    new_user = input('Please enter a username you would like to use: ')
    while new_user in credentials:
        print('That username already exists.')
        new_user = input('Please enter a different username you would like to use: ')
    if new_user not in credentials:
        new_pw = input('Please enter a password you would like to use: ')
        credentials[new_user] = new_pw #adds the key-value pair to the credentials dictionary 
        print('You have successfully chosen a username and password!')
                  

signup()

#asks the user to choose a username and password
user = input('Please enter your username: ')
pw = input('Please enter your password: ')



#checks if username and password match to an account
# if username == 'robert' and password == 'password123':
#     return 'Nice, you\'re in!'
# else:
#     return 'Get outta here!'

def is_valid_credentials(username, password):
    if username in credentials and password == credentials.get(username):
        print('Your credentials have been verified.')
        return True
    else:
        print('Your username and password do not match.')
        return False
        
is_valid_credentials('peter', 'park') #example to check if there is a matching username & password in credentials dictionary