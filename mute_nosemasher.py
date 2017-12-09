import asyncio
import discord

print("Initialising...")

bot = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):
    if str(message.author) == "Nosemasher#1438":
        print(message.content)
        await bot.delete_message(message)
                

with open("token.txt") as o:
    token = o.readline()

bot.run(token)