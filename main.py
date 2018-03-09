import asyncio as asyncio
import discord
import config
from discord import Game, Server, Member, Embed
from discord.ext import commands
from bot_commands import cmd_ping, cmd_status

client = discord.Client()

commands = {
    "ping": cmd_ping,
    "status": cmd_status,
}


@client.event
@asyncio.coroutine
def on_ready():
    print("Bot is logged in successfully. Running on servers:\n")
    for s in client.servers:
        print("  - %s (%s)" % (s.name, s.id))
    yield from client.change_presence(game=Game(name="ALL HAIL ANNA!"))

@client.event
@asyncio.coroutine
def on_message(message, ctx):
    if message.content.startswith(config.PREFIX):
        invoke = message.content[len(config.PREFIX):].split(" ")[0]
        args = message.content.split(" ")[1:]
        if commands.__contains__(invoke):
            yield from commands.get(invoke).ex(ctx, args, message, client, invoke)
        else:
            yield from client.send_message(message.channel, embed=Embed(color=discord.Color.red(), description=("The command `%s` is not valid!" % invoke)))

client.run(config.TOKEN)