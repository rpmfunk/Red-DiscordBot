

import json
from redbot.core import commands
from plexapi.server import PlexServer


plex = PlexServer(baseurl, token)
class plex(commands.Cog):
    """My custom cog"""

    @commands.command()
    async def mycom(self, ctx):
        """This does stuff!"""
        # Your code will go here
        await ctx.send("I can do stuff!")

plex = PlexServer(baseurl, token)

