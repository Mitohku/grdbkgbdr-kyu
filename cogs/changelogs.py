###########################################
############ Changelog Command ############
###########################################

import discord
import random
import json
from discord.ext import commands

class Changelog():
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command = True, aliases=['changelog', 'updates', 'changes'])
    async def changelogs(self, ctx):
        data = json.load(open('cogs/data/changelogs.json'))
        
        logs_author         = self.bot.get_user(self.bot.owner_id)
        json_log_date       = data["data"]["changelogs"][0]["date"]
        json_log_added      = data["data"]["changelogs"][0]["added"]
        json_log_removed    = data["data"]["changelogs"][0]["removed"]
        json_log_changed    = data["data"]["changelogs"][0]["changed"]
        json_log_fixed      = data["data"]["changelogs"][0]["fixed"]
        json_log_extra      = data["data"]["changelogs"][0]["extra"]

        embed = discord.Embed(colour = 0xA522B3)
        embed.set_thumbnail(url = f"{self.bot.user.avatar_url}")
        embed.set_author(name = f"Changelog: {json_log_date}.", icon_url = f"{self.bot.user.avatar_url}")
        embed.set_footer(text = f"Created by {logs_author.name} on {json_log_date}", icon_url = f"{logs_author.avatar_url}")

        if json_log_added:
            embed.add_field(name = "Added:", value = f"{json_log_added}", inline=False)
        else:
            pass

        if json_log_removed:
            embed.add_field(name = "Removed: ", value = f"{json_log_removed}", inline=False)
        else:
            pass

        if json_log_changed:
            embed.add_field(name = "Changed: ", value = f"{json_log_changed}", inline=False)
        else:
            pass

        if json_log_fixed:
            embed.add_field(name = "Fixed: ", value = f"{json_log_fixed}", inline=False)
        else:
            pass

        if json_log_extra:
            embed.add_field(name = "Extra Information: ", value = f"{json_log_extra}", inline=False)
        else:
            pass

        try:
            await ctx.message.delete()
        except:
            pass        
        await Channel.send((390546585161039872), embed=embed)

    @changelogs.command(name = 'tag')
    async def changelogs_tag(self, ctx, *, role : discord.Role = None):
        
            data = json.load(open('cogs/data/changelogs.json'))

            logs_author         = self.bot.get_user(self.bot.owner_id)
            json_log_date       = data["data"]["changelogs"][0]["date"]
            json_log_added      = data["data"]["changelogs"][0]["added"]
            json_log_removed    = data["data"]["changelogs"][0]["removed"]
            json_log_changed    = data["data"]["changelogs"][0]["changed"]
            json_log_fixed      = data["data"]["changelogs"][0]["fixed"]
            json_log_extra      = data["data"]["changelogs"][0]["extra"]

            embed = discord.Embed(colour = 0xA522B3)
            embed.set_thumbnail(url = f"{self.bot.user.avatar_url}")
            embed.set_author(name = f"Changelog: {json_log_date}.", icon_url = f"{self.bot.user.avatar_url}")
            embed.set_footer(text = f"Created by {logs_author.name} on {json_log_date}", icon_url = f"{logs_author.avatar_url}")

            if json_log_added:
                embed.add_field(name = "Added:", value = f"{json_log_added}", inline=False)
            else:
                pass

            if json_log_removed:
                embed.add_field(name = "Removed: ", value = f"{json_log_removed}", inline=False)
            else:
                pass

            if json_log_changed:
                embed.add_field(name = "Changed: ", value = f"{json_log_changed}", inline=False)
            else:
                pass

            if json_log_fixed:
                embed.add_field(name = "Fixed: ", value = f"{json_log_fixed}", inline=False)
            else:
                pass

            if json_log_extra:
                embed.add_field(name = "Extra Information: ", value = f"{json_log_extra}", inline=False)
            else:
                pass

            try:
                await ctx.message.delete()
            except:
                pass
            await Channel.send((390546585161039872), f"@everyone, heyy there is a new update!")
            await Channel.send((390546585161039872), embed=embed)

def setup(bot):
    bot.add_cog(Changelog(bot))
