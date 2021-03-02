#Version 1.1.3.2
#Ralul
#2021_03_01_18_50

import discord
import time

# define the countdown func.
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

Bananenbrot = str("ODEyMTExMzM3MTIyODI0MjEy.YC7_nw.0psLbsWOrjMEOHRM4rbLexCsyR8_LOL")
Currywurst = Bananenbrot[:-4]

class MyClinet(discord.Client):
    #Einloggen
    async def on_ready(self):
        print("Ich habe mich Eingeloggt")


    #Reactions
    async def on_message (self,message):
        #Locking das ih nöd uf mis züg reagierö
        if message.author == client.user:
            return
        else:
            # Wenn Nachricht gepostet wird, dann drucke ich sie aus
            print("Da hat jemand etwas geschrieben" + " \ " + str(message.author) + " \ " + str(message.content))

            await message.channel.send("Lets go!, The Final Countdown has Started!")

            daily = 0
            hourly = 1
            minutely = 0
            secondary = 5

            message_hourly = hourly

            legendsecondary = ((daily * 86400)+(hourly * 3600)+(minutely * 60)+(secondary * 1))

            print(legendsecondary)

            while legendsecondary >= 1:

                countdown(1)
                legendsecondary = legendsecondary - 1

                #Time OUtput in Day Hour Minutest Second

                a_daily = legendsecondary // 86400
                rest = legendsecondary % 86400
                a_hourly = rest // 3600
                rest = rest % 3600
                a_minutely = rest // 60
                rest = rest % 60
                a_secondary = rest

                print (a_daily,"¦",a_hourly,"¦",a_minutely,"¦",a_secondary)

                #Hourly message

                if a_hourly != message_hourly:
                    message_hourly = a_hourly
                    await message.channel.send ("finally only left")

                if (a_secondary + a_minutely + a_hourly + a_daily == 0):
                    message_hourly = a_hourly
                    await message.channel.send("end of all")
                    print ("null")




client = MyClinet()
client.run(Currywurst)