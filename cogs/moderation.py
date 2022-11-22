import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

'''with open('D:\\pythonProjects\\Thresher\\cogs\\badwords.txt', 'r') as f:
	global badwords
	words = f.read()
	badwords = words.split()'''

class Moderation(commands.Cog):

	def __init__(self, client):
		self.client = client


	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		try:
			
			if isinstance(error, commands.CommandNotFound):
				pass
			
			elif isinstance(error, commands.MissingRequiredArgument):
				await ctx.send("You are missing one or more required arguments!")
			
			elif isinstance(error, commands.MissingPermissions):
				await ctx.send("You are lacking permissions to use this command.")
			
			else:
				await ctx.send(f"{error}")
			
		except Exception as error:
			print(f"{error} occured.")

	'''@commands.Cog.listener()
	async def on_message(self, message):
		msg = message.content.lower()
		for word in badwords:
			if word in msg:
				await message.delete()
				await message.channel.send(f"Hi, {message.author.mention}! Please do not slurs!")'''
		

	@commands.command(aliases=['purge', 'delete'])

	@has_permissions(administrator=True, manage_messages=True)

	async def clear(self, ctx, limit:int):
			await ctx.channel.purge(limit=limit+1)
			await ctx.send(f'{limit} messages have been cleared.')

	'''@clear.error
	async def clear_error(self, error, ctx):
	    if isinstance(error, MissingPermissions):
	        await ctx.send("Looks like you don't have the perm.")'''



	@commands.command(aliases=['banhammer', 'hammer'])

	@has_permissions(administrator=True, ban_members=True)
	async def ban(self, ctx, member: discord.Member, reason=None):        
	    await member.ban(delete_message_days=0, reason=reason)
	    banEmbed = discord.Embed(title="🔨User Banned", description=f"**{member}** has been banned.\nReason: `{reason}`", color=0x3cfdc4)
	    banEmbed.set_author(name=f"{ctx.message.author}", icon_url=f"{ctx.author.avatar_url}")
	    #await ctx.send(f'🔨**{member}** has been banned.\nReason: `{reason}`\nModerator: {ctx.message.author}')
	    await ctx.send(embed=banEmbed)

	'''@ban.error
	async def ban_error(self, error, ctx):
	    if isinstance(error, commands.MissingPermissions):
	        await ctx.send("Looks like you don't have the perm.")'''



	@commands.command(aliases=['unbanhammer', 'unhammer'])

	@has_permissions(administrator=True, ban_members=True)
	async def unban(self, ctx, *, member):
		banned_users = await ctx.guild.bans()
		member_name, member_discriminator = member.split('#')

		for ban_entry in banned_users:
			user = ban_entry.user

			if (user.name, user.discriminator) == (member_name, member_discriminator):
				await ctx.guild.unban(user)
				unbanEmbed = discord.Embed(title="☑️User Unbanned", description=f"**{user.name}#{user.discriminator}** has been unbanned.", color=0x3cfdc4)
				unbanEmbed.set_author(name=f"{ctx.message.author}", icon_url=f"{ctx.author.avatar_url}")
				await ctx.send(embed=unbanEmbed)
				#await ctx.send(f"unbanned")
				return



	@commands.command(aliases=['boot'])

	@has_permissions(administrator=True, kick_members=True)
	async def kick(self, ctx, member: discord.Member, *, reason=None):
		await member.kick(reason=reason)
		kickEmbed = discord.Embed(title="👢User Kicked", description=f"**{member}** has been kicked.\nReason: `{reason}`", color=0x3cfdc4)
		kickEmbed.set_author(name=f"{ctx.message.author}", icon_url=f"{ctx.author.avatar_url}")
		#await ctx.send(f'👢**{member}** has been kicked.\nReason: `{reason}`\nModerator: {ctx.message.author}')
		await ctx.send(embed=kickEmbed)

	'''@kick.error
	async def kick_error(self, error, ctx):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send("Looks like you don't have the perm.")'''

def setup(client):
	client.add_cog(Moderation(client))
