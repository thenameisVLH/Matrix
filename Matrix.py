import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

client.remove_command('help')

@client.event

async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('FTC'))
    print("Matrix by VLH is now online.")
    print (client.user.name)

@client.event
    
async def on_message(message):
    
    if client.user.mentioned_in(message):
        await message.channel.send("Hello! My prefix is !.")

        
    if message.content.startswith('!help'):
        await message.channel.send('Hello! My Prefix is "!". I am a simple poll bot. I have six commands: !help, !help command, !poll, !help poll, !ping, and if you ping me, I will send the server prefix.')

        
    if message.content.startswith('!help poll'):
        await message.channel.send('To create a poll, type: !poll. The format is !poll (message of your poll) (what the two reactions mean or represent.)')

    await client.process_commands(message)

@client.command()

async def ping(ctx):
     await ctx.send(f'Pong! In {round(client.latency * 1000)}ms')

     
@client.command()
async def poll(ctx,*,message):
    embed = discord.Embed(title=f"Poll by {ctx.author.name}", description=message, color=0x9208ea)
    embed.set_footer(text="Created by thenameisVLH#8637")
    react_message = await ctx.send(embed=embed)

    await react_message.add_reaction("1️⃣")
    await react_message.add_reaction("2️⃣")

    await ctx.message.delete()

async def ping(ctx):
     await ctx.send(f'Pong! In {round(client.latency * 1000)}ms')

client.run("Bot_Token")
