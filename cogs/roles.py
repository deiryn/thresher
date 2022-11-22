import discord
from discord.ext import commands

ROLES_LIST = [
			  911333635506974750, # nana
 			  911333658844090439, # baba
 			  911333684060237855  # gagag
 			  ]

class Roles(commands.Cog):

	def __init__(self, client):

		self.client = client




	@commands.command(aliases=["self-role", "add-role", "giverole", "give-role"])
	
	async def addrole(self, ctx , role : discord.Role):


		if role.id in ROLES_LIST:
			await ctx.author.add_roles(role)
			addroleEmbed = discord.Embed(title="📥 Role Added", description=f"**{role}** has been added to your role list!", color=0x3cfdc4)
			addroleEmbed.set_author(name=f"{ctx.message.author}", icon_url=f"{ctx.author.avatar_url}")
			await ctx.send(embed=addroleEmbed)

		if role.id not in ROLES_LIST:
			await ctx.send("You cannot assign this role.")

	@commands.command(aliases=["remove-role", "take-role", "takerole"])

	async def removerole(self, ctx, role : discord.Role):
		author_roles = [str(roles) for roles in ctx.author.roles]

		if (role.id in ROLES_LIST) and (role in ctx.author.roles):
			await ctx.author.remove_roles(role)
			removeroleEmbed = discord.Embed(title="📤 Role Removed", description=f"**{role}** has been removed from your role list!", color=0x3cfdc4)
			removeroleEmbed.set_author(name=f"{ctx.message.author}", icon_url=f"{ctx.author.avatar_url}")
			await ctx.send(embed=removeroleEmbed)


def setup(client):
	client.add_cog(Roles(client))
