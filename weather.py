import sys
import requests
import pprint

def execute(command):
    #place=input("Place:")
    #command=input("Data:")

    payload= {'q':command,'appid':'83b794dd984f92913172ca269b9d96ee'}
    r=requests.get('http://api.openweathermap.org/data/2.5/weather',params=payload)
    #print(r.text,r.status_code)
    w=r.json()
    #if command=='temp':
    #    print(w["main"]["temp"])
    #elif command=='humidity':
    #    print(w["main"]["humidity"])
    #else:
    return(w)
    #coment
