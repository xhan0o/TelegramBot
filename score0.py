import requests
from pprint import pprint
import http.client
import datetime
import json
import score

def apicall(url,payload):
    headers = { 'X-Auth-Token': '040594424f1144b892cc2f93b91a503a', 'X-Response-Control': 'minified' }
    result=requests.get('http://api.football-data.org/v1/competitions/'+url, params=payload,headers=headers)
    response = result.json()
    return response

def apiteam(url,payload):
    headers = { 'X-Auth-Token': '040594424f1144b892cc2f93b91a503a', 'X-Response-Control': 'minified' }
    result=requests.get('http://api.football-data.org/v1/teams/'+url, params=payload,headers=headers)
    response = result.json()
    return response

payload= {}

def league (season):
        payload["season"]=season
        result=apicall("",payload)
        #print(">>> Leagure Name + Current Match Day + League ID"
        return result

def table (matchid,number) :
    payload["matchday"]=number
    result=apicall(matchid+"/leagueTable/",payload)
    return result

def players (number) :
    result=apiteam(number+"/players",payload)
    players =result["players"]
    return players

def fixtures (matchid,np,number) :
    #matchid = input('League ID:')
    #np=input('Next(n)/Past(p):')
    #number = input('Days:')
    payload["timeFrame"]=np+number
    result=apicall(matchid+"/fixtures/",payload)
    return result
    #print("Total Fixtures",result["count"])
    #fixtures =result["fixtures"]
    #a=0
    #or i in fixtures :
    #    a+=1
    #    print("Fixture",a)
    #    print(i["awayTeamName"],i["awayTeamId"])
    #    print(i["homeTeamName"],i["homeTeamId"])
    #    print("Date",i["date"][0:10]+"Time",i["date"][12:20],i["matchday"])
    #    print(i["result"],i["status"])

def teams (leagueid) :
    result=apicall(leagueid+"/teams/",payload)
    return result
