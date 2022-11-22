import discord
import json
from discord.ext import commands, tasks
import io
import os
from discord.ext.commands import has_permissions, CheckFailure, check
from discord.utils import get
import random
from datetime import datetime
from itertools import cycle

intents = discord.Intents.default()
intents.members = True
os.chdir('D:\\pythonProjects\\Thresher')

with open('BadWords.txt', 'r') as f:
    global badwords  # You want to be able to access this throughout the code
    words = f.read()
    badwords = words.split()

dt = datetime.now()

#used to get API key, i was lazy to set it up as an environ
with open("api_file.bin", encoding="utf-8") as binary_file:
	# read the whole file at once
	api_key = binary_file.read()

str(api_key)

client = commands.Bot(case_insensitive=True, command_prefix = '$', help_command=None, intents=intents)


for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

def scrambled(orig):
    dest = orig[:]
    random.shuffle(dest)
    return dest

presence_list = [
				'mindgames', 
				'debug or die',
				'cognitive behaviour therapy',
			    'with shrimp',
			    'with your feelings',
			    'poker', 
			    'DOOM Eternal', 
			    'Ultrakill', 
				'Half Life 69', 
			    'with snakes', 
			    'with sharks',
			    'uhhh... nevermind',
			    'i forgor',
			    'with my twitch tier-3 subs',
			    'decoding what you just wrote',
			    'how do I make self-roles working???',
			    'ok google uncrap my pants']

scrambled_list = scrambled(presence_list)
scrambled_list = cycle(scrambled_list)

@client.event

async def on_ready():
	change_status.start()
	print('------')
	print('Logged in as:')
	print(client.user.name)
	print(client.user.id)
	print('------')
	


	#await client.change_presence(activity=discord.Game(name=f"{random.choice(presence_list)}"))


@tasks.loop(minutes=30)
async def change_status():
	await client.change_presence(activity=discord.Game(next(scrambled_list)))

@client.command()

async def help(ctx):
    helpEmbed = discord.Embed(title="❓ Help me step shark, I'm stuck! ❓", description="`[argument]` — is required to be included in a command.\n`argument` — isn't required to be included in a command.", color=0x3cfdc4)
    helpEmbed.add_field(name="📌BASIC COMMANDS", value="`$help` — you are here!\n`$ping` — gives you current connection speed in ms.", inline=False)
    helpEmbed.add_field(name="👮 MODERATOR COMMANDS ", value="`$ban [@user] reason` — bans the user off the server. ⁉️ REQUIRES **BAN PERMS**\n`$unban [@user]` — unbans the user. ⁉️ REQUIRES **BAN PERMS**\n`$kick [@user] reason` — boots the user oof the server. ⁉️ REQUIRES **KICK PERMS**\n`$clear [amount]` — purges [amount] messages ⁉️ REQUIRES **MANAGE MESSAGES**", inline=False)
    helpEmbed.add_field(name="🥳 MISCELLANEOUS COMMANDS", value="`$avatar @user` — gives you either your or user's avatar.\n`https://steamcommunity/id/{steam}` — return steam id64 of the user.", inline=False)
    await ctx.send(embed=helpEmbed)

@client.event
async def on_command_error(ctx, error):
		
		try:
			
			if isinstance(error, commands.CommandNotFound):
				ctx.send("This command is *Not Found*! Try using `$help`.")

			else:
				pass

		except Exception as error:
			pass


@client.command()

async def ping(ctx):
	await ctx.send(f'Pong!\n\📲 {round(client.latency * 1000)}ms')


@client.command(hidden=True)

async def load(ctx, extension):
	is_owner = await ctx.bot.is_owner(ctx.author)
	
	if not is_owner:
		await ctx.message.add_reaction('🟥')
		return
	
	elif is_owner:
		client.load_extension(f'cogs.{extension}')
		print("---")
		print(dt)
		print(f"!!! COG {extension} LOADED !!!")
		print("---")
		await ctx.message.add_reaction('🟩')


@client.command(hidden=True)

async def unload(ctx, extension):
	is_owner = await ctx.bot.is_owner(ctx.author)
	
	if not is_owner:
		await ctx.message.add_reaction('🟥')
		return
	
	elif is_owner:
		client.unload_extension(f'cogs.{extension}')
		print("---")
		print(dt)
		print(f"!!! COG {extension} UNLOADED !!!")
		print("---")
		await ctx.message.add_reaction('🟩')

@client.command(hidden=True)

async def reload(ctx, extension):
	is_owner = await ctx.bot.is_owner(ctx.author)

	if not is_owner:
		await ctx.message.add_reaction('🟥')
		return

	elif is_owner:
		client.unload_extension(f'cogs.{extension}')
		client.load_extension(f'cogs.{extension}')
		print("---")
		print(dt)
		print(f"!!! COG {extension} RELOADED !!!")
		print("---")
		await ctx.message.add_reaction('🟩')

@client.listen('on_message')
async def bad_mouth(message):
	badEmbed = discord.Embed(title="⚠️Warning!", description=f"**{message.author.mention} used a bad word!**", color=0x3cfdc4)
	badEmbed.set_author(name=f"{message.author}", icon_url=f"{message.author.avatar_url}")
	msg = message.content
	for word in badwords:
		if word in msg:
			await message.delete()
			await message.channel.send(embed=badEmbed)
    #await ctx.process_message(message)

''' THIS SHIT DOESN'T WORK I HATE DISCORD
@client.listen('on_member_join')
async def member_join(member):
    channel = discord.utils.get(member.guild.channels, name='test-join-channel')
    await channel.send(f'{member.mention} joined.')



client.listen('on_member_remove')
async def memeber_left(member):
	channel = discord.utils.get(member.guild.channels, name='test-join-channel')
	await channel.send(f'{member.name} left.')
'''


client.run(api_key)
