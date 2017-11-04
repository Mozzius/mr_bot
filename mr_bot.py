import discord
import asyncio
import string

class mr_bot:
    def __init__(self):
        self.conversing = False
        self.context = []
        self.joke

        global client
        client = discord.Client()
        with open("token.txt") as o:
            client.run(o.readline())

    def restring(self, stringle):
        temp = ""
        for word in stringle:
            temp += word
            temp += " "
        return temp[:-1]
    
    def parse(self, message):
        self.message = message
        msg = message.content.translate(None, string.punctuation)
        if msg.startswith('hey') or msg.startswith('yo') or msg.startswith('excuse me'):
            split = msg.split(" ")
            if (split[1] == "@mr" and split[2] == "bot#0848") or (split[1] == "mr" and split[2] == "bot"):
                print(msg)
                print(msg[3:])
                if msg:
                    self.interpret(msg[3:])
                else:
                    await client.send_message(message.channel, 'hey, what\'s up?')
                    self.conversing = True
        elif msg.startswith('mr bot') or msg.startswith('@mr bot'):
            msg = msg.split(" ")
            if msg:
                self.interpret(msg[2:])
            else:
                await client.send_message(message.channel, 'what')
        elif self.conversing == True:
            if msg.startswith('thanks') or msg.startswith('thank you') or msg.startswith('thx'):
                await client.send_message(message.channel, 'you\'re welcome :)')
            else:
                msg = msg.split(" ")
                self.interpret(msg)
        else:
            conversing = False

    def interpret(self, msg):
        msg = restring(msg)
        if "tell me a joke" in msg or "tell a joke" in msg or ("another one" in msg and "joke" in self.context and self.conversing == True):
            await client.send_message(message.channel, '@Leprechaun#4633')
            if "joke" not in self.context:
                self.context = ["joke"]
        elif self.conversing == True and "feedback" in self.context and "yes" in msg:
            await client.send_message(message.channel, 'Oops! I\'ll take a look at it, thanks')
            print(self.context[1])
        elif self.conversing == False:
            await client.send_message(message.channel, 'Not sure I got that, should I have done?')
            self.conversing = True
            self.context = ["feedback", msg]

    @client.event
    async def on_ready():
        print('Logged in as')
        print(client.user.name)
        print(client.user.id)
        print('------')

    @client.event
    async def on_message(message):
        bot.parse(message)

bot = mr_bot()
