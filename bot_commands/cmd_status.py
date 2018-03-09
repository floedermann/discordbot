import discord
from discord import Server, Client


def ex(ctx, args, message, client, invoke):
    args_out = ""
    if len(args) > 0:
        args_out = "\n\n__**Coalition-Ping**__ \n%s" % args.__str__()[1:-1].replace("'", "").replace(",", "")
    yield from client.send_message(message.channel, embed=Embed(color=discord.Color.red(), description=("The command `%s` is not valid!" % invoke)))
