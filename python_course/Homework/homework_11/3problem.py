# Create a class to manage passwords

class Password_Manager:

    # add the most recent password to a list of passwords
    def __init__(self,n: str):
        self.oldpasswords = ['password1','password2','password3'] + [n]
    
    # return the most recent password
    def get_password(self) -> str:
        return self.oldpasswords[-1]
    
    # adds a new most recent password
    def set_passoword(self, newp: str):
        if self.oldpasswords.count(newp) != 0:
            return "Already a password"
        self.oldpasswords.append(newp)
    
    # checks if password entered is the most recent passowrd
    def is_correct(self, guess: str) -> bool:
        if guess == self.oldpasswords[-1]:
            return True
        return False


# main function
if __name__ == '__main__':

    # ask user for the most recent password and then add it to the list of old passwords
    recent = input("What is your most recent passoword? ")
    password = Password_Manager(n = recent)

    # find out which method to run
    todo = input("What do you want to do: ")
    if todo == "get my password":

        # get their most recent password
        print(password.get_password())
    elif todo == "login":

        # make them enter a password and tell it to them if they got it wrong
        login = input("What is the passoword: ")
        if password.is_correct(guess = login) == True:
            print('correct')
        else:
            print(f'wrong it is {password.get_password()}')
    elif todo == 'set password':

        # find what there new password is and if it hasn't been repeated before, add it to the list
        newp = input('What do you want your new password to be? ')
        if password.set_passoword(newp = newp) != None:
            print(password.set_passoword(newp = newp))
        else:
            print(f'your new password is {password.oldpasswords[-1]}')
