import discord
import a2s
from discord.ext import commands
from collections import defaultdict
import asyncio
import os

#Discord Bot token
token = "~~~###ENTER BOT TOKEN HERE###~~~"
intents = discord.Intents.default()
# Allows bot to read messages in discord (it can read commands and allat)
intents.message_content = True
# Defines bot command prefix
bot = commands.Bot(command_prefix=".", intents=intents)

mapUserAll = defaultdict(list)
mapUserEU = defaultdict(list)
mapUserUS = defaultdict(list)
mapUserAU = defaultdict(list)


# Get the directory of the current script and builds the full path of maps txt file
# (needed for most hosting websites)
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'allMaps.txt')

# Adds all maps from txt file to set
mapSet = set()
with open(file_path, 'r') as f:
    content = f.read()
    words = [w.strip() for w in content.split("surf_") if w.strip()]
    for name in words:
        if name.endswith("_fix"):
            name = name[:-4]
        mapSet.add(name)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

# use '.ping' in discord to test if bots working
@bot.command()
async def ping(ctx):
    await ctx.send("pong")

@bot.command()
async def addMap(ctx, *, mapName: str):
    # if users message starts with surf_ remove that from mapName string
    if mapName.startswith("surf_"):
        mapName = mapName[5:]
    endsWithFix = False
    # if map ends with _fix remove that from mapName string
    if mapName.endswith("_fix"):
        endsWithFix = True
        mapName = mapName[:-4]
    #Check if the edited mapName is in set
    if mapName not in mapSet:
        if endsWithFix:
            await ctx.send(f"`surf_{mapName}_fix` is not a map")
        else:
            await ctx.send(f"`surf_{mapName}` is not a map")
    else:
        try:
            mapUserAll[mapName].append(ctx.author)
            await ctx.send(f"{ctx.author} has subscribed to `{mapName}` on **all Regions**, you will recieve a DM when the map is active")
            print(f"{ctx.author} has subscribed to {mapName}")
        except Exception as e:
            print(f"Got error {e}")
            await ctx.send("Failed to add user to map.")
# Same thing but with for selected regions
@bot.command()
async def addMapEU(ctx, *, mapName: str):
    if mapName.startswith("surf_"):
        mapName = mapName[5:]
    endsWithFix = False
    if mapName.endswith("_fix"):
        endsWithFix = True
        mapName = mapName[:-4]
    if mapName not in mapSet:
        if endsWithFix:
            await ctx.send(f"`surf_{mapName}_fix` is not a map")
        else:
            await ctx.send(f"`surf_{mapName}` is not a map")
    else:
        try:
            mapUserEU[mapName].append(ctx.author)
            await ctx.send(f"{ctx.author} has subscribed to `{mapName}` on **EU Servers**, you will recieve a DM when the map is active")
            print(f"{ctx.author} has subscribed to {mapName}")
        except Exception as e:
            print(f"Got error {e}")
            await ctx.send("Failed to add user to map.")
@bot.command()
async def addMapUS(ctx, *, mapName: str):
    if mapName.startswith("surf_"):
        mapName = mapName[5:]
    endsWithFix = False
    if mapName.endswith("_fix"):
        endsWithFix = True
        mapName = mapName[:-4]
    if mapName not in mapSet:
        if endsWithFix:
            await ctx.send(f"`surf_{mapName}_fix` is not a map")
        else:
            await ctx.send(f"`surf_{mapName}` is not a map")
    else:
        try:
            mapUserUS[mapName].append(ctx.author)
            await ctx.send(f"{ctx.author} has subscribed to `{mapName}` on **US Servers**, you will recieve a DM when the map is active")
            print(f"{ctx.author} has subscribed to {mapName}")
        except Exception as e:
            print(f"Got error {e}")
            await ctx.send("Failed to add user to map.")

@bot.command()
async def addMapAU(ctx, *, mapName: str):
    if mapName.startswith("surf_"):
        mapName = mapName[5:]
    endsWithFix = False
    if mapName.endswith("_fix"):
        endsWithFix = True
        mapName = mapName[:-4]
    if mapName not in mapSet:
        if endsWithFix:
            await ctx.send(f"`surf_{mapName}_fix` is not a map")
        else:
            await ctx.send(f"`surf_{mapName}` is not a map")
    else:
        try:
            mapUserAU[mapName].append(ctx.author)
            await ctx.send(f"{ctx.author} has subscribed to `{mapName}` on **AU Servers**, you will recieve a DM when the map is active")
            print(f"{ctx.author} has subscribed to {mapName}")
        except Exception as e:
            print(f"Got error {e}")

#Checks all public servers and their current maps
async def checkServers():
    try:
        # US Central Beginner
        t1uscAddy = ("74.91.115.159", 27015)
        t1uscConnect = "connect 74.91.115.159:27015"
        t1uscName = "US Central Beginner"
        t1uscInfo = a2s.info(t1uscAddy)
        t1uscMap = t1uscInfo.map_name[5:]
        await sendDms(mapUserAll, t1uscMap, t1uscName, t1uscConnect)
        await sendDms(mapUserUS, t1uscMap, t1uscName, t1uscConnect)

        # US East Beginner
        t1useAddy = ("74.91.123.51", 27030)
        t1useConnect = "connect 74.91.123.51:27030"
        t1useName = "US East Beginner"
        t1useInfo = a2s.info(t1useAddy)
        t1useMap = t1useInfo.map_name[5:]
        await sendDms(mapUserAll, t1useMap, t1useName, t1useConnect)
        await sendDms(mapUserUS, t1useMap, t1useName, t1useConnect)

        # EU Beginner
        t1euAddy = ("185.107.96.64", 27019)
        t1euConnect = "connect 185.107.96.64:27019"
        t1euName = "EU Beginner"
        t1euInfo = a2s.info(t1euAddy)
        t1euMap = t1euInfo.map_name[5:]
        await sendDms(mapUserAll, t1euMap, t1euName, t1euConnect)
        await sendDms(mapUserEU, t1euMap, t1euName, t1euConnect)

        # US Regular
        regUsAddy = ("74.91.123.51", 27015)
        regUsConnect = "74.91.123.51:27015"
        regUsName = "US Central Regular"
        regUsInfo = a2s.info(regUsAddy)
        regUsMap = regUsInfo.map_name[5:]
        await sendDms(mapUserAll, regUsMap, regUsName, regUsConnect)
        await sendDms(mapUserUS, regUsMap, regUsName, regUsConnect)

        # EU Regular
        regEuAddy = ("185.107.96.64", 27016)
        regEuConnect = "connect 185.107.96.64:27016"
        regEuName = "EU Regular"
        regEuInfo = a2s.info(regEuAddy)
        regEuMap = regEuInfo.map_name[5:]
        await sendDms(mapUserAll, regEuMap, regEuName, regEuConnect)
        await sendDms(mapUserEU, regEuMap, regEuName, regEuConnect)

        # AU Regular
        regAuAddy = ("139.99.149.210", 27015)
        regAuConnect = "139.99.149.210:27015"
        regAuName = "AU Regular"
        regAuInfo = a2s.info(regAuAddy)
        regAuMap = regAuInfo.map_name[5:]
        await sendDms(mapUserAll, regAuMap, regAuName, regAuConnect)
        await sendDms(mapUserAU, regAuMap, regAuName, regAuConnect)

    except (TimeoutError, TypeError) as e:
        print(f"Got error {e}")

# Send dm functions with all parameters
async def sendDms(hashMap, mapName, serverName, serverConnect):
    for userId in hashMap[mapName]:
        try:
            await userId.send(f"{mapName} is now active on {serverName} \n {serverConnect}")
        except Exception as e:
            print(f"Failed to DM {userId}: {e}")
    del hashMap[mapName]


# Asynchrously calls the check server function every 10 seconds
async def background_check():
    await bot.wait_until_ready()
    while not bot.is_closed():
        await checkServers()
        await asyncio.sleep(10)  # wait 10 seconds between checks

# Allows background tasks to be called with bot
@bot.event
async def setup_hook():
    bot.loop.create_task(background_check())

bot.run(token)
