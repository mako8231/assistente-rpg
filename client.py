from discord.ext import commands 
client = commands.Bot(command_prefix="$")
    
def connection_client(token):
    @client.event
    async def on_ready():
        print('Logged on as {0}!'.format(client.user))

    @client.event
    async def on_message(message):
      print('Message from {0.author}: {0.content}'.format(message))

    @client.command()
    async def test(ctx, *args):
        await ctx.send("{} argumento(s): {}".format(len(args), ', '.join(args)))

    @client.command()
    async def echo(ctx, *, arg):
        await ctx.send(arg)

    client.run(token)    
