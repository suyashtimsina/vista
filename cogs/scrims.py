import discord
from discord.ext import commands
from discord import app_commands
from main import MyBot

scrimsinguild = 0

class Scrims(commands.Cog):
    def __init__(self, bot: MyBot):
        self.bot = bot

    class CreateButtons(discord.ui.View):
        def __init__(self):
            super().__init__(timeout=None)

        @discord.ui.button(label="Reg. Channel", style=discord.ButtonStyle.blurple)
        async def reg_channel(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_message("📝 Set Reg. Channel here.")

        @discord.ui.button(label="Reg. Success Role", style=discord.ButtonStyle.blurple)
        async def reg_success_role(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_message("📝 Set Reg. Success Role here.")

        @discord.ui.button(label="Slot-list Channel", style=discord.ButtonStyle.blurple)
        async def slot_list_channel(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_message("📝 Set Slot-list Channel here.")

        @discord.ui.button(label="Total Slots", style=discord.ButtonStyle.blurple)
        async def total_slots(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_message("📝 Set Total Slots here.")

        @discord.ui.button(label="Opening time", style=discord.ButtonStyle.blurple)
        async def opening_time(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_message("📝 Set Opening Time here.")

        @discord.ui.button(label="Reg. Days", style=discord.ButtonStyle.blurple)
        async def reg_days(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_message("📝 Set Reg. Days here.")

        @discord.ui.button(label="Save", style=discord.ButtonStyle.green)
        async def save_scrim(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_message("✅ The scrim has been saved as `scrim #1`")

    class ScrimButtons(discord.ui.View):
        def __init__(self, cog):
            super().__init__(timeout=None)
            self.cog = cog

        @discord.ui.button(label="Create", style=discord.ButtonStyle.green)
        async def create_scrim(self, interaction: discord.Interaction, button: discord.ui.Button):
            embed = discord.Embed(
                title="Scrim Creator",
                description="Enter the details and save",
                color=discord.Color.blue()
            )
            embed.add_field(name="Reg. Channel", value="`nil`", inline=True)
            embed.add_field(name="Reg. Success Role", value="`nil`", inline=True)
            embed.add_field(name="Slot-list Channel", value="`nil`", inline=True)
            embed.add_field(name="Total Slots", value="`nil`", inline=True)
            embed.add_field(name="Opening time", value="`nil`", inline=True)
            embed.add_field(name="Reg. Days", value="`nil`", inline=True)

            view = Scrims.CreateButtons()
            await interaction.response.send_message(embed=embed, view=view)

        @discord.ui.button(label="View Scrims", style=discord.ButtonStyle.blurple)
        async def view_scrims(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_message("📋 Here's a list of scrims (none yet).")

    @commands.command(aliases=["s", "sc"])
    async def scrim(self, ctx):
        embed = discord.Embed(
            title="Scrim Manager Menu",
            description="```Click on Create button to create a new scrim```",
            color=discord.Color.blue()
        )
        embed.set_footer(text=f"The scrims in this server: {scrimsinguild}")
        view = self.ScrimButtons(self)
        await ctx.send(embed=embed, view=view)

async def setup(bot: commands.Bot):
    await bot.add_cog(Scrims(bot))
    print("Scrims cog loaded successfully")

