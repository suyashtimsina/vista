import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()


exts = {
    "cogs.modify",
    "cogs.welcomer",
    "cogs.error",
    "cogs.scrims"
}


class MyBot(commands.Bot):
    def __init__(self, command_prefix:str, intents: discord.Intents, **kwargs):
        super().__init__(command_prefix, intents=intents, **kwargs)
    
    async def setup_hook(self) -> None:
        
        for ext in exts:
            await self.load_extension(ext)
        
        # await self.tree.sync()
        print("Slash commands synced.")

        

    async def on_ready(self):
        print(f"✅ Logged in as {bot.user}")
        
bot = MyBot(command_prefix=".", intents=discord.Intents.all())

@bot.command(name='add')
async def add(ctx, num1: float, num2: float):
    result = num1 + num2
    await ctx.send(f"The sum of {num1} and {num2} is **{result}**")

if __name__=="__main__":
        bot.run(os.getenv("DISCORD_TOKEN"))