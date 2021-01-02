import discord
import re
import random
import ast
import datetime
from discord.ext import commands

token = open("token.txt", "r").read()

client = discord.Client()
fd = ['b', '-', '+', 'b', '-', '+']
fd_value = {'b' : 0, "-": -1, "+": 1}

@client.event
async def on_ready():
    print("{} online".format(client.user))

@client.event
async def on_message(message):
    pattern = ("^(\/rf [0-9]){1}((\+|\-)[0-9])*")
    pattern2 = "ilu"

    if message.author == client.user:
        return
    if message.content == "fate help":
        response = "`/rf [# of dice] [+/-modifiers]`"
        await message.channel.send(response)
        return
    if re.match(pattern2, str(message.content)) and (message.author != client.user):
        response = "I probably love you too " + message.author.mention
        await message.channel.send(response)
        return

    elif re.match(pattern, str(message.content)):
        response = roll_fate(message)
        if message.author == "WC#9964":
            response.append(", I hope no one died")
        await message.channel.send(response)
        return

def roll_fate(message):
    value = message.content[4:]
    rolls = []
    matches = []
    total = 0
    for x in range(int(value[0])):
        roll = roll_dice("f")
        rolls.append(roll)
        total += fd_value[roll]
    temp = value[1:]
    temp_val = total
    if len(temp) > 1:
        pattern = "(\+[0-9]|\-[0-9])"
        matches = re.findall(pattern, temp)
        for match in matches:
            eval = ast.literal_eval(match)
            total += eval

    response = message.author.mention + " `Roll " + message.content[4] + " dice " + message.content[5:] + "` = (" + str(rolls)[1:-1].replace("'", "") + ') ' + str(matches)[1:-1].replace("'", "") + " = " + str(total)
    return response
def roll_dice(type):
    roll = None
    if type == "f":
        roll = random.choice(fd)
    else:
        roll = random.choice([range(type)])
    return roll


client.run(token)
