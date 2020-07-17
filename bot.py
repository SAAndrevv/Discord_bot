import os
import time

import discord
from dotenv import load_dotenv
import top_chart_request as tcr

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "chart!":
        await message.channel.send("Это займет какое-то вермя...")

        chart = tcr.chart()
        if not chart:
            chart_send  = "Возникли проблемы на сервере"
    
        else:
            now = time.strftime("---%B %Yг.---")
            number = 1
            chart_send = "\n".join(
                    [str(chart.index(song) + 1)+ ") " + song for song in chart])
            chart_send = (f'{now}\n{chart_send}')

        await message.channel.send(chart_send)

client.run(TOKEN)
