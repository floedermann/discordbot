import discord
import config
from discord import Server, Client, ChannelType, Embed

def ex(args, message, client, invoke, config):
    args_out = ""
    author = message.author.name
    if len(args) > 0:
        args_out = "\n\n__**C o a l i t i o n - P i n g**__\nFrom: "+ author + "\n\n%s" % args.__str__()[1:-1].replace("'", "").replace(",", "")
    for s in client.servers:
        channel = discord.utils.get(s.channels, name=config.PINGCHANNEL, type=ChannelType.text)
        if channel is not None:
            yield from client.send_message(client.get_server(s.id).get_channel(channel.id),embed=Embed(color=discord.Color.gold(), description=("@everyone" + args_out)))