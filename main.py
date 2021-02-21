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


            #Wenn Nachricht gepostet wird, dann drucke ich sie aus
            print("Da hat jemand etwas geschrieben" +" \ "+ str(message.author) +" \ "+ str(message.content))

            #Help
            if message.content.startswith("<help"):
                await message.channel.send ("i'm t800 bot, you can me be use with < ")

            if message.content.startswith("WaPaDuDeLiDu"):
                await message.channel.send("ThinkOutSideTheBox55555")

            #Wenn mich jemand Begrüsst
            if message.content.startswith("<hello t800"):
                await message.channel.send("Hello!!! my future slave")


            if message.content.startswith("<tic tac toe t800"):
                await message.channel.send("--------Tic Tac Toe--------")

                # Tic Tac Toe game

                playerInput = [1,2,3,4,5,6,7,8,9]


                await message.channel.send(str(playerInput[0]) + "|" + str(playerInput[1]) + "|" + str(playerInput[2]))
                await message.channel.send(str(playerInput[3]) + "|" + str(playerInput[4]) + "|" + str(playerInput[5]))
                await message.channel.send(str(playerInput[6]) + "|" + str(playerInput[7]) + "|" + str(playerInput[8]))

                await message.channel.send("select a field, player One ")

                #spiler eins eingabe und ihn palyerinput speichern




                return

            if message.content.startswith("<play"):
                await message.channel.send("Playing...")

                # Playing yt link

                return






client = MyClinet()
client.run("ODEyMTExMzM3MTIyODI0MjEy.YC7_nw.QqzY9YMCXu_IqtcxM0RH66YtjFQ")
