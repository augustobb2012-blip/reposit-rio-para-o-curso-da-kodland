import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')

# Comandos

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello! I am {bot.user}!")

@bot.command()
async def bye(ctx):
    await ctx.send("Bye!")

@bot.command()
async def hoje(ctx):
    await ctx.send("Ebaa!!! Aula de Python!!!")

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member} entrou em {member.joined_at}')

# COMANDO DE AJUDA
@bot.command()
async def help(ctx):
    comandos = """
Comandos do Bot:

$hello -> O bot te cumprimenta  
$bye -> O bot se despede  
$hoje -> Mensagem sobre a aula  
$joined @usuario -> Mostra quando o usuário entrou no servidor  
$help -> Mostra essa lista de comandos
"""
    await ctx.send(comandos)
