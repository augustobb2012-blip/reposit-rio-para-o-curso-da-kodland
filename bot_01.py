import discord
from discord.ext import commands

# Permissões
intents = discord.Intents.default()
intents.message_content = True

# Criando o bot
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f'Fizemos login como {bot.user}')

# Mantendo o MESMO comportamento do seu on_message
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(f"Hello! i am {bot.user}!")

    elif message.content.startswith('$bye'):
        await message.channel.send("🙂")

    elif message.content.startswith('$hoje'):
        await message.channel.send("ebaa!!! aula de python!!!")

    else:
        await message.channel.send(message.content)

    # ESSA LINHA É MUITO IMPORTANTE
    await bot.process_commands(message)

@bot.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send(f'{member} joined on {member.joined_at}')
