#2018.04.30, 第4章.pptx, P39-41, program using a subclass

import time

#parent class User
class User:
        username = ""
        
        def __init__( self, username ):
            self.username = username

        #display the username
        def DisplayUsername( self ):
            print( self.username )
            
#subclass UserLogin whose parent is class User
class UserLogin( User ):
        loginTime = ""

        def __init__( self, username, loginTime ):
            User.__init__( self, username )

            self.loginTime = loginTime

        #display the login time
        def DisplayLoginTime( self ):
            print( "  Login time: " + self.loginTime )

loginTime = time.strftime( "%Y-%m-%d %H:%M:%S",time.localtime() )  #get the current time

user1 = UserLogin( "admin", loginTime )  #create a UserLogin object and assign it to "user1"
user2 = UserLogin( "Arvin", loginTime )  #create a UserLogin object and assign it to "user2"
user3 = UserLogin( "Zhao", loginTime )  #create a UserLogin object and assign it to "user3"

user1.DisplayUsername()  #call the specified function in class UserLogin (parent class User) to display the username of "user1"
user1.DisplayLoginTime()  #call the specified function in class UserLogin to display the login time of "user1"
user2.DisplayUsername()  #call the specified function in class UserLogin (parent class User) to display the username of "user2"
user2.DisplayLoginTime()  #call the specified function in class UserLogin to display the login time of "user2"
user3.DisplayUsername()  #call the specified function in class UserLogin (parent class User) to display the username of "user3"
user3.DisplayLoginTime()  #call the specified function in class UserLogin to display the login time of "user3"