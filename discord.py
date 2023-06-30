import discord
from discord.ext import commands

prefixo = "!"

client_id = "meu client id"
client_secret = "Meu client secret"

intents = discord.Intents.default()
intents.typing = False  
intents.presences = False  

bot = commands.Bot(command_prefix=prefixo, intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')
    print('ID do bot:', bot.user.id)
    print('------')

@bot.command()
async def hello(ctx):
    await ctx.send('Olá, mundo! Esse é o trabalho do Professor Fernando ;) Para mais informações digite "!como_fui_feito"')

@bot.command()
async def como_fui_feito(ctx):
    await ctx.send('Fui desenvolvido em Python usando a biblioteca discord.py.Para mais informações digite "!como_funciono"')

@bot.command()
async def como_funciono(ctx):
    await ctx.send('Eu funciono como um bot Discord. Recebo comandos dos usuários e executo ações específicas com base nesses comandos. Sou programado para responder a certas palavras-chave e executar as tarefas associadas a elas.Para mais informações digite "!como_funciona_a_api"')

@bot.command()
async def como_funciona_a_api(ctx):
    await ctx.send('A API do Discord fornece funcionalidades para desenvolvedores criarem bots e interagirem com servidores e usuários do Discord. Ela permite enviar e receber mensagens, gerenciar permissões, entre outras coisas.')
    

bot.run('Meu Token')

