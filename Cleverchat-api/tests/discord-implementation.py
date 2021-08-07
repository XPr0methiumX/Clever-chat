import discord
from discord.ext import commands
from cleverchat import Client

client = commands.Bot(command_prefix='amogus')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == 854342237461676073:
        response = Client.get_response(message.content, message.author.id, "Male", "Oxy")
        await message.channel.send(response)

@client.event
async def on_ready():
    print(f'{client.user.name} is ready!')

client.run(TOKEN)