import discord
from discord.ext import commands
settings = {
    'token': 'ODM2MzA0ODkxNDI0MDE0NDI2.YIcDnw.fSMeowGtnZB9UQ_YN0b401KAzSA',
    'bot': '__Chill_Bot__',
    'id': 836304891424014426,
    'prefix': '!'
}
bot = commands.Bot(command_prefix = settings['prefix'])
@bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Привет маленький {author.mention}!')
async def ass(ctx):
    author = ctx.message.author
    await ctx.send(f'У тебя есть 300 bucks {author.mention}, тогда я сделаю тебе fisting ass')
bot.run(settings['token'])