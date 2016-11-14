
import time
import random
import datetime
import telepot
import weather
import score0



def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print ('Got command: %s' % command)
    brkcmdx=command.lower()
    brkcmd=brkcmdx.split()



    if brkcmd[0] == '#weather':
        bot.sendMessage(chat_id, str(weather.execute(brkcmd[1])))
        if brkcmdp[1] == 'help':
            bot.sendMessage(chat_id, str("Commands: #weather (PlaceName) "))

    elif brkcmd[0] == '#football':
        if brkcmd[1] == 'league' :
            fullmsg=score0.league(brkcmd[2])
            bot.sendMessage(chat_id, str("-->League name , Matchday, League id"))
            for i in fullmsg :
                bot.sendMessage(chat_id, str((i["caption"],i["currentMatchday"],i["id"])))
        elif brkcmd[1] == 'teams' :
            fullmsg=score0.teams(brkcmd[2])
            bot.sendMessage(chat_id, str("-->Team name , Team id"))
            tmx=fullmsg["teams"]
            for i in tmx :
                bot.sendMessage(chat_id, str((i["name"],i["id"])))

        elif brkcmd[1] == 'table' :
            fullmsg=score0.table(brkcmd[2],brkcmd[3])
            standing=fullmsg["standing"]
            bot.sendMessage(chat_id, str(("-->League Name:"+fullmsg['leagueCaption'])))
            bot.sendMessage(chat_id, str("-->Match day:"+str(fullmsg['matchday'])))
            bot.sendMessage(chat_id, str(">>> Teams + Points"))
            for i in standing :
                bot.sendMessage(chat_id, str((i["team"],i["points"])))

        elif brkcmd[1] == 'fixtures':
            fullmsg=score0.fixtures(brkcmd[2],brkcmd[3],brkcmd[4])
            #bot.sendMessage(chat_id, str("Total Fixtures:"+str(fullmsg["count"])))
            print(fullmsg)
#            fixtures =fullmsg["fixtures"]
#            a=0
#            for i in fixtures :
#                a+=1
#                bot.sendMessage(chat_id, str((">>Fixture"+str(a))))
#                bot.sendMessage(chat_id, str(i["homeTeamName"]+"  \t  "+str(i["homeTeamId"])))
#                bot.sendMessage(chat_id, str(("Date"+str(i["date"][0:10])+"  \t  "+"Time"+str(i["date"][12:20])+str(i["matchday"]))))
#                print("Date",i["date"][0:10]+"Time",i["date"][12:20],i["matchday"])
#                print(i["result"],i["status"])

        elif brkcmd[1] == 'players' :
            fullmsg=score0.players(brkcmd[2])
            for i in fullmsg :
                bot.sendMessage(chat_id, str((i["name"],i["nationality"],i["position"])))
        elif brkcmd[1] == 'help' :
            bot.sendMessage(chat_id, str("Commands: #football "))
            bot.sendMessage(chat_id, str("league (season)"))
            bot.sendMessage(chat_id, str("teams (teamid)"))
            bot.sendMessage(chat_id, str("table (leagueid) (MatchDay)"))
            bot.sendMessage(chat_id, str("fixtures -- not working"))
            bot.sendMessage(chat_id, str("players (teamid)"))

        else:
            bot.sendMessage(chat_id, str("Type '#football help' for finding football commands"))

    elif brkcmd[0]== 'yo':
        bot.sendMessage(chat_id, str("Commands:"))
        bot.sendMessage(chat_id, str("#football help"))
        bot.sendMessage(chat_id, str("#weather (place)"))
    else:
        bot.sendMessage(chat_id, str("Enter Valid Response, Type 'Yo' for help"))


bot = telepot.Bot('token')
bot.message_loop(handle)
print ('I am listening ...')

while 1:
    time.sleep(10)
