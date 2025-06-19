import discord
from discord.ext import commands
from discord import app_commands
from main import MyBot 
import json

class Welcomer(commands.Cog):
    def __init__(self, bot: MyBot):
        self.bot = bot

    @app_commands.command(name="welcome",description="Welcome a new member in the guild")
    async def welcome(self, interation: discord.Interaction):
        with open("./db.json","r") as f:
            records = json.load(f)
        
        records[str(interation.guild_id)] = str(interation.channel_id)
        with open("./data.json","w") as f:
            json.dump(records, f)

        await interation.response.send_message("Sucess! {interaction.channel.mention} is your welcome channel.")

async def setup(bot: commands.Bot):
    await bot.add_cog(Welcomer(bot))
    print("Welcomer cog loaded successfully.")
