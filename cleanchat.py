import discord
from discord.ext import commands, tasks

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('Pronto para apagar segredos.')
target_channel_id = None
@client.command(pass_context=True)
async def canal(ctx, target_channel_id):
    if target_channel_id is None:
        return ctx.send('Insira um canal!')
    else:
        canal_de_mensagens = client.get_channel(target_channel_id)
        await ctx.send(f'Novo canal selecionado.\nCanal: #{canal_de_mensagens}\nChannel ID: {target_channel_id}')
        print(f'Atualmente no canal #{canal_de_mensagens}')
        return canal

"""
@tasks.loop(seconds= 10)
async def called_once_a_day():
    message_channel = client.get_channel(737011020446433404)
    print(f"Got channel #{message_channel}")
    await message_channel.send("Your message")

@called_once_a_day.before_loop
async def before():
    await client.wait_until_ready()
    print("Finished waiting")

called_once_a_day.start()

""
@tasks.loop(seconds=5)
async def apagadiario():
    while True:
        #canalz = client.get_channel(canal)
        #print(f'Atualmente no canal {canalz}')
        await canal.channel.purge(limit=2)
        await asyncio.sleep(1)

@apagadiario.before_loop
async def before():
    await client.wait_until_ready()
    print('A espera acabou!')

apagadiario.start()

------------
@client.command(aliases=['cc'])
async def cleanchat(ctx, amount=10):
    await ctx.channel.purge(limit=amount)
    await ctx.send("MENSAGEM DE REGRA DO CANAL")

"""

client.run('NzM3MDA4NzAzMTk0MjY3NzQ5.Xx3G1w.LpdmGkDNGmVeM6Fsqf0kTUdAsTM')