import asyncio
import discord
from discord.ext import commands
from main import MyBot  # Assuming you're using a custom MyBot class


class EditSelectMenu(discord.ui.Select):
    def __init__(self, bot, member: discord.Member, ctx):
        self.bot = bot
        self.member = member
        self.ctx = ctx

        options = [
            discord.SelectOption(label="Change Nickname", description="Change the nickname of the user.", value="nick"),
            discord.SelectOption(label="Remove Nickname", description="Remove the user's nickname.", value="remove_nick")
        ]

        super().__init__(
            placeholder="Choose an option...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):
        action = self.values[0]

        if action == "nick":
            await interaction.response.send_message(f"Enter the new nickname for <@{self.member.id}>", ephemeral=True)

            def check(m):
                return m.author == self.ctx.author and m.channel == self.ctx.channel

            try:
                msg = await self.bot.wait_for('message', check=check, timeout=30)
                await self.member.edit(nick=msg.content)
                await self.ctx.send(f"✅ Nickname changed to `{msg.content}` for `{self.member}`")
            except asyncio.TimeoutError:
                await self.ctx.send("⏰ You took too long to respond!")
        elif action == "remove_nick":
            await interaction.response.defer(thinking=True)
            await self.member.edit(nick=None)
            await interaction.followup.send(f"✅ Removed nickname for `{self.member}`")
        


class Modify(discord.ui.View):
    def __init__(self, bot, member: discord.Member, ctx):
        super().__init__(timeout=60)
        self.add_item(EditSelectMenu(bot, member, ctx))


class EditUser(commands.Cog):
    def __init__(self, bot: MyBot):
        self.bot = bot

    @commands.command(aliases=["edit"])
    async def change(self, ctx: commands.Context, member: discord.Member):
        embed = discord.Embed(
            title="Edit User Details",
            description=f"What do you want to do to <@{member.id}>?",
            color=discord.Color.blue()
        )
        view = Modify(self.bot, member, ctx)
        await ctx.send(embed=embed, view=view)


async def setup(bot: commands.Bot):
    await bot.add_cog(EditUser(bot))
    print("EditUser cog loaded successfully.")
