# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 22:01:53 2020

@author: ASUS
"""
# =============================================================================
# from collections import Container
# 
# class OddContainer:
#     def __contains__(self, x):
#        if not isinstance(x, int) or not x % 2:
#            return False
#        return True
# =============================================================================
import abc
class MediaLoader(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def play(self):
        pass
    
    @abc.abstractproperty
    def ext(self):
        pass
    
    @classmethod
    def __subclassshook__(cls, C):
        if cls is MediaLoader:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented
