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
    print(f'Entrando no canal #{canal_de_mensagens}')
    return ctx

@canal.error
async def canal_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Insira um canal!')

@tasks.loop(days=1)
async def apagadiario():
    if canal_de_mensagens is None:
        print(f"Atuando em nenhum canal!")
        pass
    else:
        amount=10
        print(f'Apagando mensagens em #{canal_de_mensagens}.\nTaxa: {amount} mensagens/dia')
        await canal_de_mensagens.purge(limit=amount)
        await canal_de_mensagens.send("MENSAGEM DO CANAL")

@apagadiario.before_loop
async def before():
    await client.wait_until_ready()
    print("Acabou a espera!")

apagadiario.start()

client.run('TOKEN')
