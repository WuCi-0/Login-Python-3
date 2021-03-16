Login_info = ['Login_info',]

def  Clogin():
    Username = input('Create A Username: ')
    Login_info.append(Username)
    Password = input('Create A Password: ')
    Login_info.append(Password)
    print('DOne!')

def Login():
    Lusername = input('Enter Your Username: ')
    if Lusername == (Login_info[1]):
        print('Correct!')
    Lpassword = input('Enter Your Password: ')
    if Lpassword == (Login_info[2]):
        print('Succesful Login!')
        


def AYRU():
    AYR = input('Are You Regestered  yes/no ')
    if AYR == ('no'):
        Clogin()
    if AYR == ('yes'):
        Login()

code_run = (True)

while code_run == (True):
    AYRU()
 #This Was Made By WuCi-0  This Is My GitHub File
