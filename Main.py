import discord
import constants as const
from urllib.parse import urlparse

intents = discord.Intents.all()
bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")

@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")

@bot.event
async def on_message(message):
    if "https://twitter.com/" in message.content:
        twitter_url = urlparse(message.content)
        tweet_path = twitter_url.path
        vxtwitter_url = "https://vxtwitter.com" + tweet_path
        await message.reply(vxtwitter_url)
        await message.edit(suppress=True)

bot.run(const.BOT_TOKEN) # run the bot with the token
