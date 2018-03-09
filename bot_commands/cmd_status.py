import discord
from discord import Server, Client, ChannelType, Embed

def ex(args, message, client, invoke, config):
    args_out = ""
    args = ""
    for s in client.servers:
        args += s.name + "\n"
    args_out = "\n\n__**Currently registered servers**__ \n\n%s" % args
    yield from client.send_message(message.channel, embed=Embed(color=discord.Color.green(), description=(args_out)))
