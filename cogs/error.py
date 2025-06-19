import discord
from discord.ext import commands
from discord import app_commands
from main import MyBot


class ErrorCog(commands.Cog):
    def __init__(self, bot: MyBot):
        self.bot = bot
        bot.tree.on_error = self.on_app_command_error

    async def on_app_command_error(self, interaction: discord.Interaction, error:app_commands.AppCommandError):
        ...


    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error : commands.CommandError ):
        if isinstance(error, commands.MissingRequiredArgument):
            return await ctx.send(f"Missing required arguments.{error.param.name}")




async def setup(bot: commands.Bot):
    await bot.add_cog(ErrorCog(bot))
    print("Error cog loaded successfully.")
