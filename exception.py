# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# =============================================================================
# class EvenOnly(list):
#     def append(self, integer):
#         if not isinstance(integer, int):
#             raise TypeError("Only integers can be added")
#         if integer%2:
#             raise ValueError("Only even numbers can be added")
#         super().append(integer)
# =============================================================================
# =============================================================================
# def no_return():
#     print("I am about to raise an exception")
#     raise Exception("This is always raised")
#     print("This line will never execute")
#     return "I won't be returned"
# 
# def call_exceptor():
#     print("call_exxceptor starts here...")
#     no_return()
#     print("an exception was raised...")
#     print("..so these linees don't run")
# 
# try:
#     no_return()
# except:
#     print("I caught an exception!")
# print("excecuted after exception")
# =============================================================================
# =============================================================================
# def funny_division(anumber):
#     try:
#         if anumber == 13:
#             raise ValueError("13 is an un lucky number")
#         return 100/anumber
#     except ZeroDivisionError:
#         return "Enter a number other than zero"
#     except TypeError:
#         return "Enter a numeric value"
#     except ValueError:
#         print("No, No, not 13!")
#         raise
# 
# for val in (0, "hello", 50.0, 13):  
#     print("Testing {}:".format(val), end=" ")
#     print(funny_division(val))
# =============================================================================
# =============================================================================
# =============================================================================
# import random
# some_exceptions = [ValueError, TypeError,IndexError, None]
# 
# try:
#     choice = random.choice(some_exceptions)
#     print("raising {}".format(choice))
#     if choice:
#         raise choice("An error")
# except ValueError:
#     print("caught a valueerror")
# except TypeError:
#     print("caught a typeerror")
# except Exception as e:
#     print("Caught some other error: %s"%(e.__class__.__name__))
# else:
#     print("This code called if there is no exception")
# finally:
#     print("This cleanup coed is always called")
# =============================================================================
class InvalidWithdrawal(Exception):
    def __init__(self, balance, amount):
        super().__init__("account doesn't have ${}".format(amount))
        self.amount = amount
        self.balance = balance
    
    def overage(self):
        return self.amount - self.balance

try:
    raise InvalidWithdrawal(25, 50)
except InvalidWithdrawal as e:
    print("I'm sorry, but your withdrwal is more than your balance by ${}".format(e.overage()))