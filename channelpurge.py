import discord
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Pronto para apagar segredos.')

canal_de_mensagens = None

@client.command()
async def canal(ctx, target_channel_id):
    global canal_de_mensagens
    canal_de_mensagens = client.get_channel(int(target_channel_id))
    await ctx.send(f'Novo canal selecionado.\nCanal: #{canal_de_mensagens}\nChannel ID: {target_channel_id}')
    print(f'Atualmente no canal #{canal_de_mensagens}')
    return int(target_channel_id)

@canal.error
async def canal_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Insira um canal!')

@tasks.loop(seconds=10)
async def apagadiario():
    print(f"Loopando em #{canal_de_mensagens}")
    if canal_de_mensagens is None:
        pass
    else:
        print(f'Apagando mensagens em #{canal_de_mensagens}')
        await canal_de_mensagens.channel.purge(2)

@apagadiario.before_loop
async def before():
    await client.wait_until_ready()
    print("Acabou a espera!")

apagadiario.start()


"""
@client.command(aliases=['cc'])
async def cleanchat(ctx, amount=10):
    await ctx.channel.purge(limit=amount)
    await ctx.send("MENSAGEM DE REGRA DO CANAL")

"""

client.run('TOKEN')
