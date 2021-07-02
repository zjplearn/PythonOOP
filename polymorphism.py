# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 20:49:00 2020
本部分讨论多态特性
@author: ASUS
"""
# =============================================================================
# class AudioFile:
#     def __init__(self, filename):
#         if not filename.endswith(self.ext):
#             raise Exception("Invalid file format")
#         
#         self.filename = filename
#         
# class MP3File(AudioFile):
#     ext = "mp3"
#     def play(self):
#         print("playong {} as mp3".format(self.filename))
# 
# class WavFile(AudioFile):
#     ext = "wav"
#     def play(self):
#         print("playing {} as wav.".format(self.filename))
# 
# class OggFile(AudioFile):
#     ext = "ogg"
#     def play(self):
#         print("playing {} as ogg".format(self.filename))
# =============================================================================
#鸭子类型
class FlacFile:
    def __init__(self, filename):
        if not filename.endswith(".flac"):
            raise Exception("Invalid file format")
        
        self.filename = filename
    
    def play(self):
        print("playing {} as flac".format(self.filename))



