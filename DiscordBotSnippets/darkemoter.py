import discord,time
from discord.ext import commands

client = discord.Client()
darkemoji = None
channel = "760509524833599539"
emojiname = "darkalpha"
serverid = "685469328929587268"

@client.event
async def on_ready():
    global darkemoji,client
    print('We have logged in as {0.user}'.format(client))
    statustxt = "Dark is daddy"
    activity = discord.Game(name=statustxt)
    for ej in client.emojis:
            if(ej.name == emojiname):
                darkemoji = ej
                print("emoji found!")
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.event
async def on_message(message):
    global darkemoji,client,channel
    if message.author == client.user:
        return

    for role in message.author.roles:
        if(role.name == "smolpp"):
            print("yes he has small pp")
            await message.add_reaction('🤏')
            await message.add_reaction('🍆')
        



'''@commands.has_role("smolpp")
async def on_message(message):
    global darkemoji,client,channel
    if message.author == client.user:
        return

    print("ping-wanted")
    await message.add_reaction('🤏')
    time.sleep(0.2)
    await message.add_reaction('🍆')
    
    '''


client.run('TOKEN')