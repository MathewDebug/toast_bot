import discord
from discord.ext import commands
import discord.utils
import time

client = commands.Bot(command_prefix = '.')
#Removes discord default help command
client.remove_command('help')

@client.event
async def on_ready():
    print('Bot is ready.')

@client.command()
async def help(ctx):
    await ctx.send("```1) ping: shows latency of the bot\n2) users: shows total amount of members in the server\n3) hello: says hello to you because nobody else will\n4)  ```")

@client.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(client.latency * 1000)}ms')

@client.command()
async def users(ctx):
    serverId = client.get_guild(704782563574546482)
    await ctx.send("``" + f"""Number of members in the server: {serverId.member_count}""" + "``") 

@client.command()
async def hello(ctx):
    await ctx.send('Hello!')

#@client.event
#async def on_message(message):
#    userId = 231896456095727618
#    if (message.author.id == userId):
#        msg = await message.channel.fetch_message(id)
#    if message.author.id == userId:
#        await message.channel.send('Shut up')
#   #Everyone
#    await message.channel.send('Shut up ' + str(message.author)[0:len(str(message.author)) - 5])

client.run('NzcxODg4MjkwMDYzODQzMzI4.X5yq_Q.QdTpPo2vPD-sy4CizAq0xxvMlkY')