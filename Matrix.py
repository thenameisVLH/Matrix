import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Hello'))
    print("Matrix by VLH is now online.")
    print (client.user.name)

@client.command(pass_context = True)
async def poll(ctx,*,message):
    embed = discord.Embed(title=f"Poll by {ctx.author.name}", description=message, color=0x9208ea)
    embed.set_footer(text="Created by thenameisVLH#8637")
    react_message = await ctx.send(embed=embed)

    await react_message.add_reaction("1️⃣")
    await react_message.add_reaction("2️⃣")

    await ctx.message.delete()

client.run("ODQ4NzExMzg0MDMxNTU5Njky.YLQmEg.8azVrz_z6x9D4CboliiknZgZcuI")
                                           
