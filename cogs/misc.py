import discord
from discord.ext import commands
import requests
from os import environ

STEAMKEY = environ['STEAMEKEY']

def steam_id(STEAM_URL):
    response = requests.get(f"https://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={STEAMKEY}&vanityurl={STEAM_URL}")
    temp_id = response.json()
    steamid = temp_id["response"]["steamid"]
    return steamid

def scpinfo(scp):
	name = scpscraper.get_scp_name(scp)
	url = f"https://scp-wiki.wikidot.com/scp-{scp}"

	return name, url

class Miscellaneous(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.Cog.listener()
	async def on_message(self, msg):
		steamProfile = msg.content
		steamProfile = steamProfile.lower()
		if steamProfile.startswith("https://steamcommunity.com/id/"):
			temp_msg1 = steamProfile[30:]
			temp_msg2 = temp_msg1.replace('/', '')
			steamProfile = temp_msg2
			await msg.channel.send(steam_id(steamProfile))

	@commands.command(aliases=['pfp'])
	async def avatar(self, ctx, *, user : discord.Member=None):
		if user == None:
			userAvatarUrl = ctx.author.avatar_url

		else:
			userAvatarUrl = user.avatar_url

		await ctx.send(userAvatarUrl)

	@commands.command()
	async def snake(self, ctx):
		snake_response = requests.get("http://127.0.0.1:7777/snake/")
		temp_json = snake_response.json()
		snake_pic = temp_json["image"]
		await ctx.send(file=discord.File(f'D:\\pythonProjects\\SnakeAPI\\images\\{snake_pic}'))


def setup(client):
	client.add_cog(Miscellaneous(client))