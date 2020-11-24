import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('NzgwNjg2MTE2MjQzNjM2MjY1.X7ysmg.R4RqDcP2fPqnUUaojf7xLjLlT8o')
