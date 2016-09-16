#!/usr/bin/env python
# encoding: utf-8

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#def login():
#    print('in login')
#
#def printdebug(func):
#    print "enter the login"
#    func()
#    print "exit the login"



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#def printdebug(func):
#    def __decorator(user):      # add parameter receive the user information
#        print "enter the login"
#        func(user)              # pass user to func
#        print "exit the login"
#    return __decorator          # function as return value
#
#@printdebug                     # combine the printdebug and login
#def login(user):
#    print "{user} in login".format(user=user)
#
#
#if __name__ == "__main__":
#    login("ljj")



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#def printdebug_level(level):
#    def printdebug(func):
#        def __decorator(user):
#            print "enter the login, and debug level is: " + str(level)      # print debug level
#            func(user)
#            print "exit the login"
#        return __decorator
#    return printdebug               # return original decorator
#
#@printdebug_level(level=5)          # decorator's parameter, debug level set to 5
#def login(user):
#    print "{user} is login ~".format(user=user)
#
#login("lijing")



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def printdebug(func):
    def __decorator(user):
        print "enter the login"
        result = func(user)             # receive the native function call result
        print "exit the login"
        return result
    return __decorator

@printdebug
def login(user):
    print "{user} is login".format(user=user)
    msg = "success" if user =="lijing" else "fail"
    return msg          # login with a return value

result1 = login("lijing")
print result1
print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
result2 = login("li")
print result2






































