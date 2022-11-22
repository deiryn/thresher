import scpscraper

@commands.command()
	async def scp(self, ctx, *, scp = None):
		if scp.startswith('0'):
			await ctx.send("Please remove any zeroes before the number of SCP.")
			break
		else:
			name = scpscraper.scp_get_name(scp)
			if len(scp) < 3:
				if len(scp) < 2:
					url = f"https://scp-wiki.wikidot.com/scp-00{scp}"
				else:
				url = f"https://scp-wiki.wikidot.com/scp-0{scp}"
			
			else:
				url = f"https://scp-wiki.wikidot.com/scp-{scp}"

		await ctx.send(f"["{name}"]({url})")
