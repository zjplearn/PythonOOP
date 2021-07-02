# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 16:36:27 2020

@author: ASUS
"""
#所有类都继承自特殊的object类
# =============================================================================
# class MysubClass(object):
#     pass
# 超类object,子类MySubClass
# =============================================================================
# =============================================================================
# class Contact:
#     all_contacts = []
#     
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         Contact.all_contacts.append(self)
# x = Contact('sa', 'sas')
# y = Contact('sas', 'ssssssssssssssss')
# 
# class Supplier(Contact):
#     def order(self, order):
#         print("If this  were a real system we would send "
#               "'{}' order to '{}'".format(order, self.name))
# =============================================================================
# =============================================================================
#扩展List类
# class ContactList(list):
#     def search(self, name):
#         '''Return all contacts that contain the search value in their name.'''
#         matching_contacts = []
#         for contact in self:
#             if name in contact.name:
#                 matching_contacts.append(contact)
#         return matching_contacts
#         
# 
# class Contact:
#     all_contacts = ContactList()
#      
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         Contact.all_contacts.append(self)
# =============================================================================
# =============================================================================
# class LongNameDict(dict):
#     def longest_key(self):
#         longest = None
#         for key in self:
#             if not longest or len(key) > len(longest):
#                 longest = key
#         return longest
# =============================================================================
# =============================================================================
# class BaseClass:
#     num_base_calls = 0
#     def call_me(self):
#         print("Calling method on Base Class")
#         self.num_base_calls += 1
# 
# class LeftSubclass(BaseClass):
#     num_left_calls = 0
#     def call_me(self):
#         BaseClass.call_me(self)
#         print("Calling method on Left Subclass")
#         self.num_left_calls += 1
# 
# class RightSubclass(BaseClass):
#     num_right_calls = 0
#     def call_me(self):
#         BaseClass.call_me(self)
#         print("Calling method on Right Subclass")
#         self.num_right_calls += 1
# 
# class Subclass(LeftSubclass, RightSubclass):
#     num_sub_calls = 0
#     def call_me(self):
#         LeftSubclass.call_me(self)
#         RightSubclass.call_me(self)
#         print("Calling method on Subclass")
#         self.num_sub_calls += 1
# 
# =============================================================================
# =============================================================================
# class BaseClass:
#     num_base_calls = 0
#     def call_me(self):
#         print("Calling method on Base Class")
#         self.num_base_calls += 1
# 
# class LeftSubclass(BaseClass):
#     num_left_calls = 0
#     def call_me(self):
#         super().call_me()
#         print("Calling method on Left Subclass")
#         self.num_left_calls += 1
# 
# class RightSubclass(BaseClass):
#     num_right_calls = 0
#     def call_me(self):
#         super().call_me()
#         print("Calling method on Right Subclass")
#         self.num_right_calls += 1
# 
# class Subclass(LeftSubclass, RightSubclass):
#     num_sub_calls = 0
#     def call_me(self):
#         super().call_me()
#         print("Calling method on Subclass")
#         self.num_sub_calls += 1
# =============================================================================
