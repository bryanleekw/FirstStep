# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 21:06:56 2017

@author: LKW084
"""

from recsys.algorithm.factorize import SVD
from recsys.datamodel.data import Data
from game import Game, get_preference

import json
import urllib
import urllib2
import math
import cStringIO
import matplotlib.pyplot as plt
from operator import itemgetter, attrgetter, methodcaller

def get_user_list():
    url='http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?\
key=147CBF377C6B648EC3DC73499CE73D32&steamid=76561197960435530&relationship=friend'
    response = urllib2.urlopen(url)
    friends_Data = json.loads(response.read().decode('utf-8-sig'))
    user_List=[]
    user_List.append('76561198119879419')
    num=0
    for friends in friends_Data['friendslist']['friends']:
        user_List.append(friends['steamid'])   
        num=num+1
    #print num
    return user_List


class User:
        def __init__(self, userid):
            url='http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?\
key=147CBF377C6B648EC3DC73499CE73D32&steamids='+user_map[item[0]]
            response = urllib2.urlopen(url)
            friends_Data = json.loads(response.read().decode('utf-8-sig'))
            #print avatar
            #urllib.urlretrieve(friends_Data['response']['players'][0]['avatarfull'], "local.jpg")
            #image = plt.imread("local.jpg")
            #plt.imshow(image)
            #plt.show()
        
        #print name
            self.name=friends_Data['response']['players'][0]["personaname"]
            self.avatar=friends_Data['response']['players'][0]['avatarfull']
        def print_avatar(self):
            urllib.urlretrieve(sefl.avatar, "local.jpg")
            image = plt.imread("local.jpg")
            plt.imshow(image)
            plt.show()

def recommend_friends(user_map):
    
    
    for item in svd_r.similar(1):
        if item[1]>0.2:
            print item[0]
            url='http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?\
key=147CBF377C6B648EC3DC73499CE73D32&steamids='+user_map[item[0]]
            response = urllib2.urlopen(url)
            friends_Data = json.loads(response.read().decode('utf-8-sig'))
        #print avatar
            urllib.urlretrieve(friends_Data['response']['players'][0]['avatarfull'], "local.jpg")
            image = plt.imread("local.jpg")
            plt.imshow(image)
            plt.show()
        
        #print name
            print friends_Data['response']['players'][0]["personaname"]