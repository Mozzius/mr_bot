import string
import asyncio
import discord

print("Initialising...")

bot = discord.Client()

def parse(msg):
    if msg.startswith('hey') or msg.startswith('yo'):
        splitmsg = msg.split(" ")
        if (splitmsg[1] == "@mr" and splitmsg[2] == "bot#0848") or (splitmsg[1] == "mr" and splitmsg[2] == "bot"):
            return 3
    elif msg.startswith('mr bot') or msg.startswith('@mr bot#0848'):
        return 2

def parsecommand(commandarr):
    if commandarr[0] == "textmute" or (commandarr[0] == "shut" and commandarr[1] == "up"):
        return "mute"
    elif commandarr[0] == "untextmute":
        return "unmute"
    elif commandarr[0] == "introduce":
        return "intro"
    elif commandarr[0] == "search" or (commandarr[0] == "look" and commandarr[1] == "up"):
        return "mute"
    elif commandarr[0] == "is" or commandarr[0] == "are":
        return "is"
    elif commandarr[0] == "fuck" and commandarr[1] == "me":
        return "fuck"
    else:
        return "unsure"

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    with open("muted.txt", "r") as m:
        if message.author in m.readlines():
            print("Deleted",message.author,"'s message")
            await bot.delete_message(message)
            return
    msg = message.content
    msg.strip(".,!?").lower()
    relevent = parse(msg)
    if relevent:
        splitmsg = msg.split(" ")
        if len(splitmsg) == relevent:
            await bot.send_message(message.channel, "hey, what's up?")
        else:
            command = ""
            commandarr = splitmsg[relevent:]
            #for word in commandarr[1:]:
            #    command += word
            #    command += " "
            keyword = parsecommand(commandarr)
            if keyword == "mute":
                if str(message.author.top_role) == "moddo":
                    await bot.send_message(message.channel, "Muting "+commandarr[1])
                    with open("muted.txt","r") as m:
                        lines = m.readlines()
                    with open("muted.txt","w") as m:
                        for line in lines:
                                m.write(line+"\n")
                        m.write(commandarr[1])
                else:
                    await bot.send_message(message.channel, "You don't have permission to do that, "+message.author.nick)
            elif keyword == "unmute":
                if str(message.author.top_role) == "moddo":
                    await bot.send_message(message.channel, "Unmuting "+commandarr[1])
                    with open("muted.txt","r") as m:
                        lines = m.readlines()
                    with open("muted.txt","w") as m:
                        for line in lines:
                            if line != command:
                                m.write(line+"\n")
                else:
                    await bot.send_message(message.channel, "You don't have permission to do that, "+message.author.nick)
            elif keyword == "intro":
                #if message.author.top_role == "moddo":
                await bot.send_message(message.channel, "Hey everybody! I'm your new bot friend, mr bot. Summond me using \"hey mr bot\"!")
                #else:
                #    await bot.send_message(message.channel, "No")
            elif keyword == "search":
                await bot.send_message(message.channel, "I would, but I don't know how :(")
            elif keyword == "is":
                await bot.send_message(message.channel, "Probably")
            elif keyword == "fuck":
                await bot.send_message(message.channel, "Bit gay")
            elif keyword == "unsure":
                await bot.send_message(message.channel, "Not sure what that means, sorry :/")
    elif "silly bot" in msg:
        await bot.send_message(message.channel, "Sorry :(")
                

with open("token.txt") as o:
    token = o.readline()

bot.run(token)
