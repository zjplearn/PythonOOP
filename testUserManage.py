# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 10:29:10 2020

@author: ASUS
"""

import userManage

userManage.authenticator.add_user("joe", "joepassword")
userManage.authorizor.add_permisssion("test program")
userManage.authorizor.add_permisssion("chnage program")
userManage.authorizor.permit_user("test program", "joe")

class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
            "login": self.login,
            "test": self.test,
            "change":self.change,
            "quit": self.quit
            }
    
    def login(self):
        logged_in = False
        while not logged_in:
            username = input("username: ")
            password = input("password: ")
            try:
                logged_in = userManage.authenticator.login(username, password)
            except userManage.InvalidUsername:
                print("Sorry, that username does nnot exist")
            except userManage.InvalidPassword:
                print("Sorry, incorrect password")
            else:
                self.username = username
    
    def is_permiitted(self, permission):
        try:
            userManage.authorizor.check_permission(permission, self.username)
        except userManage.NotLoggedInError as e:
            print("{} is not logged in".format(e.username))
            return False
        except userManage.NotPerrmittedError as e:
            print("{} cannot {}".format(e.username, permission))
            return False
        else:
            return True
    
    def test(self):
        if self.is_permiitted("test program"):
            print("Testing program now...")
        
    def change(self):
        if self.is_permiitted("change program"):
            print("Changing program now...")
    
    def quit(self):
        raise SystemExit()
    
    def menu(self):
        try:
            answer = ""
            while True:
                print("""Please enter a command:
                      \tlogin\tlogin
                      \ttest\tTest the the program
                      \tchange\tChange the program
                      \tquit\tQuit
                      """)
                answer = input("enter a commaand: ").lower()
                try:
                    func = self.menu_map[answer]
                except KeyError:
                    print("{} is not a valid option".format(answer))
                else:
                    func()
        finally:
            print("Thank you for testing the auth module")
                      
Editor().menu()        