import discord
from discord import Server, Client


def ex(args, message, client, invoke):
    args_out = ""
    if len(args) > 0:
        args_out = "\n\n__**Coalition-Ping**__ \n%s" % args.__str__()[1:-1].replace("'", "").replace(",", "")
    for s in client.servers:
        client.send_message(client.get_server(s).get_channel("1234"), "@everyone" + args_out)
