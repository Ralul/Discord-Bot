#Version 1.1.2.1
#Ralul
#2021_03_01_13_30

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

            await message.channel.send("Lets go")

            daily = 1
            hourly = 1
            minutely = 2
            secondary = 30

            legendsecondary = ((daily * 86400)+(hourly * 3600)+(minutely * 60)+(secondary * 1))

            print(legendsecondary)

            while legendsecondary >= 1:

                countdown(1)
                legendsecondary = legendsecondary - 1

                rest = 0
                a_daily = ((legendsecondary / 86400) - (legendsecondary % 86400))
                rest = legendsecondary % 86400
                a_hourly = ((rest / 3600)-(rest % 3600))
                rest = rest % 3600
                a_minutely = ((rest / 60) - (rest % 60))
                rest = rest % 60
                a_secondary = rest




                print (a_daily,"¦",a_hourly,"¦",a_minutely,"¦",a_secondary)



















client = MyClinet()
client.run(Currywurst)