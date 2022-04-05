import os
import random
import discord


def aufruf(c, d):
    my_filey = open(c, d)
    contenty = my_filey.read()
    content_wort = contenty.split(",")
    my_filey.close()
    return content_wort


def make_random():
    content_cards = aufruf("D:/Program Files/ProgrammingStuff/Python/Python Stuff/CAHOrakel/Cards.txt", "r")
    a = len(content_cards) - 1
    n = random.randint(0, a)
    ora = content_cards[n]

    return ora


client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if '?' in message.content:
        response = make_random()
        await message.channel.send(response)


TOKEN = open("D:/Program Files/ProgrammingStuff/Python/Python Stuff/CAHOrakel/Token.txt", "r").readline()
client.run(TOKEN)
