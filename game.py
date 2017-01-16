# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 16:03:02 2017
"""


from recsys.algorithm.factorize import SVD
from recsys.datamodel.data import Data
#from recsys import SVD
#from recsys import Data

#from recsys.algorithm.factorize import SVD
#from recsys.datamodel.data import Data

#from io import StringIO as cStringIO
from urllib.request import urlopen


import json
import urllib
#import urllib2
import math
#import cStringIO
import matplotlib.pyplot as plt
#from operator import itemgetter, attrgetter, methodcaller

#get a full list on steam and test if certain game exists
def get_game_list(appid):
    url = "http://api.steampowered.com/ISteamApps/GetAppList/v2"
    response = urlopen(url)
    global gamelist
    gameList = json.loads(response.read().decode('utf-8-sig'))
    found=0
    num=0
    for item in gameList['applist']['apps']:
        if item['appid']==appid:
            print (item['name'])
            found=1
            num=num+1

    if found!=1:
        return False

class Game:
        def __init__(self, appid):
                self.appid = appid
                url = "http://api.steampowered.com/ISteamApps/GetAppList/v2"
                response = urlopen(url)
                gameList = json.loads(response.read().decode('utf-8-sig'))
                for item in gameList['applist']['apps']:
                    if item['appid']==self.appid:
                        #print (item['name'])
                        found=1
                if found!=1:
                    raise Exception('Error! No such game found')
                self.owned=False
                index=str(appid)
                #get app name from Steam Web API
                url="http://store.steampowered.com/api/appdetails/?appids="+index
                response = urlopen(url)
                gameData = json.loads(response.read().decode('utf-8-sig'))
                self.success=0
                if((gameData[index]['success']==True)):
                    #some games are dead 
                    try:
                        self.genre=gameData[index]['data']['genres']
                        self.name=gameData[index]['data']['name']
                        self.rec=gameData[index]['data']['recommendations']['total']
                        self.img=gameData[index]['data']['header_image']
                        self.success=1
                    except:
                        #print ('failed to load a game')                        
                        pass
        def owned():
                self.owned=True


def get_preference(user_List):
    #generate list of users
    
    preference_dict={}
    user_map={}
    data = Data() #saving rating data
    i=1
    for user in user_List:
        user_id=(str(user))
        url = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?\
key=147CBF377C6B648EC3DC73499CE73D32&steamid="+user+"&format=json"
        response = urlopen(url)
        owned_gameData = json.loads(response.read().decode('utf-8-sig'))
        user_Pref={}
        #print (user)
        try: 
            if owned_gameData['response']['game_count']!=0:
                user_Pref={}
                for games in owned_gameData['response']['games']:
                    if games['playtime_forever']>0:
                        user_Pref[games['appid']]= math.log(games['playtime_forever'])
                        data.add_tuple((math.log(games['playtime_forever'], 10), games['appid'], i))
                        user_map[i]=user
        except:
            continue
        i=i+1
        preference_dict[user]=user_Pref
    data.save('rating.dat')
    
def recommend(dimension=100): 
    svd = SVD()
    svd.load_data(filename='rating.dat',
                sep='\t',
                format={'col':2, 'row':1, 'value':0, 'ids': int})

    k = dimension
    svd.compute(k=k, min_values=1, pre_normalize=None, mean_center=True, post_normalize=True)
    
    game_recdict={}
    for item in svd.recommend(1, is_row=False):
        appid=item[0]
        game=Game(appid)
        if (game.success==1):
            game_recdict[game.rec]=[game.appid, game.genre, game.name, game.img]
        
    sorted_list=sorted(game_recdict.keys(), reverse=True)
    print ("Games Recommended:")
    for i in sorted_list:
        # image
        urllib.urlretrieve(game_recdict[i][3], "local-filename.jpg")
        image = plt.imread("local-filename.jpg")
        plt.imshow(image)
        plt.show()
    
        #name
        print(game_recdict[i][2])


