import discord
import constants

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
        twitter_url = message.content
        vxtwitter_url = twitter_url.replace("twitter", "vxtwitter")
        await message.reply(vxtwitter_url)

bot.run(constants.bot_token) # run the bot with the token
