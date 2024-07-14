import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix='?', intents=intents)

@bot.command()
async def helping(ctx):
    await ctx.send('Команды: ?choice, ?recycling, ?advice, Другие команды в разработке...')

@bot.command()
async def choice(ctx):
    choises = ('Выбросить мусор', 'Поиграть в Комп', 'Сдать бумагу на переработку')  
    await ctx.send(random.choice(choises))

@bot.command()
async def recycling(ctx):
    await ctx.send('Если вы хотите переработать мусор, достаточно сдать его в пункт, где принимают разные материалы. Статья о переработке мусора: https://multifoto.ru/blog-lifestyle/sortirovka-musora-dlya-detey-kak-privit-privychku-detyam-berech-prirodu/')

@bot.command()
async def advice(ctx):
    await ctx.send('Совет по переработке бумаги: Собери ненужную мукулатуру по всему дому и сдай. Итог: и заработаешь немного, и чуть природу спасёшь).')
 

 

 

bot.run('token')
