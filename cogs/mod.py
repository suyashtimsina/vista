import discord
from discord.ext import commands
from datetime import timedelta
from discord import app_commands
from main import MyBot

class Mod(commands.Cog):
    def __init__(self, bot: MyBot):
        self.bot = bot

    # < ____________________________ TIMEOUT COMMAND ____________________________ >
    @app_commands.command(name="timeout",description="Timeout aa user from the guild.")
    @app_commands.describe(member="Mention the member", reason="Reason for timeout")
    @app_commands.checks.has_permissions(moderate_members = True)
    @app_commands.checks.bot_has_permissions(moderate_members = True)
    async def timeout(self, interaction: discord.Interaction, member: discord.Member, *, minutes: int, reason: str
        ):  
        delta = timedelta(minutes=minutes)
        await interaction.response.defer(thinking=True)
        await member.timeout(delta,reason=reason)
        await interaction.followup.send(f"{member} has been timed out for `{reason}`.")

    @timeout.error
    async def on_error(interaction: discord.Interaction, error: commands.CommandError):
        if isinstance(error, commands.MissingPermissions):
            await interaction.response.send_message("You don't have permission to use this command!")
        elif isinstance(error, commands.BotMissingPermissions):
            await interaction.response.send_message("Bot has no permissions!")



    # # < ____________________________ BAN COMMAND ____________________________ >
    # @app_commands.command(name="ban", description="Ban a user from the guild.")
    # @app_commands.describe(member="Mention the member", reason="Reason for ban")
    # @commands.has_permissions(ban_members = True)
    # @commands.bot_has_permissions(ban_members = True)
    # async def ban(interaction: discord.Interaction, member: discord.Member, *,reason:str):
    #     await member.ban(reason=reason)
    #     await interaction.response.send_message(f"{member} has been banned for `{reason}`.")

    # @ban.error
    # async def on_error(interaction: discord.Interaction, error: commands.CommandError):
    #     if isinstance(error, commands.MissingPermissions):
    #         await interaction.response.send_message("You don't have permission to use this command!")
    #     elif isinstance(error, commands.BotMissingPermissions):
    #         await interaction.response.send_message("Bot has no permissions!")


    
    # # < ____________________________ KICK COMMAND ____________________________ >
    # @app_commands.command(name="kick", description="Kick a user from the guild.")
    # @app_commands.describe(member="Mention the member", reason="Reason for kick")
    # @commands.has_permissions(kick_members = True)
    # @commands.bot_has_permissions(kick_members = True)
    # async def kick(interaction: discord.Interaction, member: discord.Member, *,reason:str):
    #     await member.kick(reason=reason)
    #     await interaction.response.send_message(f"{member} has been kicked for `{reason}`.")

    # @kick.error
    # async def on_error(interaction: discord.Interaction, error: commands.CommandError):
    #     if isinstance(error, commands.MissingPermissions):
    #         await interaction.response.send_message("You don't have permission to use this command!")
    #     elif isinstance(error, commands.BotMissingPermissions):
    #         await interaction.response.send_message("Bot has no permissions!")




async def setup(bot: commands.Bot):
    await bot.add_cog(Mod(bot))
    print("Mod cog loaded successfully.")