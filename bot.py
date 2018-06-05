import discord
from discord.ext import commands
import asyncio
import os
import sys
import time
import random
import datetime as dt
import datetime
import json, asyncio
import copy
import logging
import traceback
import aiohttp
from collections                import Counter


command_prefix = "s" #CHANGE IT TO WHAT YOU WANT
description = "Sinful Sinifs" #ALSO CHANGE THIS
bot = commands.Bot(command_prefix, description = description)
bot.remove_command('help')
tu = datetime.datetime.now()

@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')



############################################################################################################################################################################################################



@bot.command(aliases = ['cmds', 'commands'], description = 'Sends a message with commands in DM')
async def help(ctx):

	developer = bot.get_user(385419569558323202) # commands.get_user(commands.owner_id)

	if developer.avatar_url[54:].startswith('a_'):
		avi = 'https://cdn.discordapp.com/avatars/' + developer.avatar_url[35:-10]
	else:
		avi = developer.avatar_url

	embed = discord.Embed(colour = discord.Colour(0xE4D7FF))
	embed.set_thumbnail(url = avi)
	embed.set_author(name = developer, url = "https://discord.gg/efF93Gz", icon_url = avi)
	embed.description = f"Hi everyone! I'm **{developer.name}**, the creator of **Sinful** <:bot:453635744960086026> \nI'm a Bot Developer but I'm also a Web Designer & Designer. \nI made that <:bot:453635744960086026> because *~~I love Kyu and Fae and have a crush on them~~* >.> *(yea I don't hide)*"
	embed.add_field(name="Having Issues/Problems?", value="If you have any problems with **Sinful** <:bot:453635744960086026>,\nthen you can send a message to developer with `sfeedback [message]`", inline=False)

	help1 = discord.Embed(colour = discord.Colour(0xE4D7FF))
	help1.title = f"Sinful Commands List~♡"
	help1.description = f"**Sinful** <:bot:453635744960086026>'s prefix is **s**.\n\n"
	help1.add_field(name="Core Commands", value="`shelp` **|** `ssetgame`", inline=False)
	help1.add_field(name="Utility Commands", value="`sping` **|** `sprofile` **|** `sabout` **|** `savatar` **|** `sgicon`", inline=False)
	help1.add_field(name="Fun Commands", value="`ssnowball` **|** `svhug`", inline=False)
	help1.add_field(name="Kawaii Commands", value="`shug` **|** `sblush` **|** `sscared` **|** `sdance` **|** `skiss` **|** `slewd` **|** `slick` **|** `spet` **|** `ssmug` **|** `scry` **|** `shappy` **|** `sfun` **|** `ssing` **|** `sattack` **|** `seat` **|** `skms` **|** `swink` **|** `snom`", inline=False)
	help1.add_field(name="Extra Commands", value="`sfeedback` **|** `sowner`", inline=False)
	help1.set_footer(text = "Have fun using Sinful~♡")

	await ctx.send(embed = embed)
	await ctx.send(embed = help1)



############################################################################################################################################################################################################



@bot.command(aliases = ['creator', 'dev', 'developer'], description = 'Who is my creator?')
async def owner(ctx):

	developer = bot.get_user(385419569558323202) # commands.get_user(commands.owner_id)

	if developer.avatar_url[54:].startswith('a_'):
		avi = 'https://cdn.discordapp.com/avatars/' + developer.avatar_url[35:-10]
	else:
		avi = developer.avatar_url

	embed = discord.Embed(colour = discord.Colour(0xE4D7FF))

	embed.set_thumbnail(url = avi)
	embed.set_author(name = developer, url = "https://discord.gg/efF93Gz", icon_url = avi)

	embed.description = f"Hi everyone! I'm **{developer.name}**, the creator of **Sinful** <:bot:453635744960086026> \nI'm a Bot Developer but I'm also a Web Designer & Designer. \nI made that <:bot:453635744960086026> because *~~I love Kyu and Fae and have a crush on them~~* >.> *(yea I don't hide)*"

	await ctx.send(embed = embed)



############################################################################################################################################################################################################



@bot.command(aliases = ['ping', 'ms'])
async def latency(ctx):
	pingms = "{}".format(int(ctx.bot.latency * 1000))
	message = await ctx.send("Ping - Calculating connection.")
	await message.edit(content = f"Ping - Calculating connection..")
	await asyncio.sleep(0.50)
	await message.edit(content = f"Ping - Calculating connection...")
	await asyncio.sleep(0.50)
	await message.edit(content = f"Ping - Calculating connection....")
	await asyncio.sleep(0.50)
	await message.edit(content = f"Ping - Calculating connection.")
	await asyncio.sleep(0.50)
	await message.edit(content = f"Ping - Calculating connection..")
	await asyncio.sleep(0.50)
	await message.edit(content = f"Ping - Calculating connection...")
	await asyncio.sleep(1.50)
	await message.edit(content = f"Pong! - My latency is **{pingms}**ms")



############################################################################################################################################################################################################



@bot.group()
async def game(self):

	if game == None:
		await self.send(f"Please use one of the following settings: `default`, `playing`, `streaming`, `watching`, `listenning` or `clear`")

@game.command(name = 'playing')
async def game_playing(self, *, game = None):

	if not game:
		await self.send(f"Please enter a status message")
	else:
		await self.bot.change_presence(game=discord.Game(name = game))
		await self.send(f"**{self.bot.user.name}**'s status succesfully changed to 'Playing **{game}**'")

@game.command(name = 'streaming')
async def game_streaming(self, *, game = None):

	if not game:
		await self.send(f"Please enter a status message")
	else:
		await self.bot.change_presence(game=discord.Game(name = game, url = "https://www.twitch.tv/spiritprod", type = 1))
		await self.send(f"**{self.bot.user.name}**'s status succesfully changed to 'Streaming **{game}**'")

@game.command(name = 'listenning')
async def game_listning(self, *, game = None):

	if not game:
		await self.send(f"Please enter a status message")
	else:
		await self.bot.change_presence(game=discord.Game(name = game, type = 2))
		await self.send(f"**{self.bot.user.name}**'s status succesfully changed to 'Listenning to **{game}**'")

@game.command(name = 'watching')
async def game_watching(self, *, game = None):

	if not game:
		await self.send(f"Please enter a status message")
	else:
		await self.bot.change_presence(game=discord.Game(name = game, type = 3))
		await self.send(f"**{self.bot.user.name}**'s status succesfully changed to 'Watching **{game}**'")

@game.command(name = 'default')
async def game_default(self):

	if not game:
		await self.send(f"Please enter a status message")
	else:
		bot_prefix = "s"
		server = self.guild
		games = [f"Use {bot_prefix}help for help!", f"{sum(1 for _ in self.bot.get_all_members())} users on server", f"Give us feedback? Use: {bot_prefix}feedback [message]"]
		current_number = 0
		await self.send(f"**{self.bot.user.name}**'s status succesfully changed to 'Default'")
		while True:
			if current_number == len(games):
				current_number = 0
			await self.bot.change_presence(game=discord.Game(name = games[current_number], url = "https://www.twitch.tv/spiritprod", type = 1))
			await asyncio.sleep(12)
			current_number += 1

@game.command(name = 'clear')
async def game_clear(self, *, game = None):

	if not game:
		await self.send(f"Please enter a status message")
	else:
		await self.bot.change_presence(game=discord.Game(name = None))
		await self.send(f"Cleared the status of **{self.bot.user.name}**")



############################################################################################################################################################################################################



@bot.command()
async def hug(ctx, *, member : discord.Member=None):
    if not member:
        await ctx.send(f"Please **mention** the person you want to ***hug*** !")
    elif member == ctx.author:
        author = ctx.message.author.mention
        hug1 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        hug1.description = f"{author} hugged themselves.... Sad..."
        list3 = [
            "https://media.giphy.com/media/sisfaf8ZIdSAU/giphy.gif",
            "http://image.noelshack.com/fichiers/2017/50/6/1513460592-miku-cuddling-yoshino.gif",
            ]
        choice3 = random.choice(list3)
        hug1.set_image(url = choice3)
        await ctx.send(embed = hug1)

    else:
        author = ctx.message.author.mention
        mention = member.mention
        hug2 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        hug2.description = f"{author} has hugged {mention}. Awwwww~~ 💝"
        list3 = [
            "https://media.giphy.com/media/sisfaf8ZIdSAU/giphy.gif",
            "http://image.noelshack.com/fichiers/2017/50/6/1513460592-miku-cuddling-yoshino.gif",
            ]
        choice3 = random.choice(list3)
        hug2.set_image(url = choice3)
        await ctx.send(embed = hug2)

@bot.command()
async def kiss(ctx, *, member : discord.Member=None):
    if not member:
        await ctx.send(f"Please **mention** the person you want to ***kiss*** !")
    else:
        author = ctx.message.author.mention
        mention = member.mention
        kiss2 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        kiss2.description = f"{author} is kissing {mention}. LOVE IS IN THE AIRRR~ 💝"
        list4 = [
            "https://media.giphy.com/media/11xP7QUQl8d02c/giphy.gif",
            "https://media.giphy.com/media/HSgkuMRab3fK8/giphy.gif",
            ]
        choice4 = random.choice(list4)
        kiss2.set_image(url = choice4)
        await ctx.send(embed = kiss2)

@bot.command()
async def blush(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        blush1 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        blush1.description = f"{author} is blushing! I wonder why hehe~"
        list5 = [
            "https://media.giphy.com/media/LIAoqLFnAvm6c/giphy.gif",
            "https://media.giphy.com/media/13aCm6Gp5bCsec/giphy.gif",
            "http://image.noelshack.com/fichiers/2017/50/6/1513460561-tumblr-n3ih37wl1v1sc9og8o1-500.gif",
            ]
        choice5 = random.choice(list5)
        blush1.set_image(url = choice5)
        await ctx.send(embed = blush1)
    else:
        author = ctx.message.author.mention
        mention = member.mention
        blush2 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        blush2.description = f"{mention} made {author} blush! Awwwww, cute~~ 💝"
        list5 = [
            "https://media.giphy.com/media/LIAoqLFnAvm6c/giphy.gif",
            "https://media.giphy.com/media/13aCm6Gp5bCsec/giphy.gif",
            "http://image.noelshack.com/fichiers/2017/50/6/1513460561-tumblr-n3ih37wl1v1sc9og8o1-500.gif",
            ]
        choice5 = random.choice(list5)
        blush2.set_image(url = choice5)
        await ctx.send(embed = blush2)

@bot.command()
async def scared(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        scared1 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        scared1.description = f"{author} is scared.... Let's help them"
        scared1.set_image(url = "https://media.giphy.com/media/NHNyT2CUTkjuw/giphy.gif")
        await ctx.send(embed = scared1)
    else:
        author = ctx.message.author.mention
        mention = member.mention
        scared2 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        scared2.description = f"{mention} scared {author}! What a mean person!"
        scared2.set_image(url = "https://media.giphy.com/media/NHNyT2CUTkjuw/giphy.gif")
        await ctx.send(embed = scared2)

@bot.command()
async def dance(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        dance1 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        dance1.description = f"{author} is dancing! What a professionnal!"
        list6 = [
            "https://media.giphy.com/media/ipfO8nyNQSVnq/giphy.gif",
            "https://media.giphy.com/media/100AQ5GepqTP3O/giphy.gif",
            "https://media.giphy.com/media/yEx3Lwfqx6Ap2/giphy.gif",
            "https://media.giphy.com/media/vWVfsA3VOhYMU/giphy.gif",
            ]
        choice6 = random.choice(list6)
        dance1.set_image(url = choice6)
        await ctx.send(embed = dance1)

@bot.command()
async def lick(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        lick1 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        lick1.description = f"{author} licked themselves, Uhhhh.."
        list7 = [
            "http://upload.inven.co.kr/upload/2013/05/23/bbs/i3871970273.gif",
            "http://image.noelshack.com/fichiers/2017/50/6/1513460656-kurumi-licks-shido-s-wound.gif",
            ]
        choice7 = random.choice(list7)
        lick1.set_image(url = choice7)
        await ctx.send(embed = lick1)
    else:
        author = ctx.message.author.mention
        mention = member.mention
        lick2 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        lick2.description = f"{author} is licking {mention}. W-Whut?"
        list7 = [
            "http://upload.inven.co.kr/upload/2013/05/23/bbs/i3871970273.gif",
            "http://image.noelshack.com/fichiers/2017/50/6/1513460656-kurumi-licks-shido-s-wound.gif",
            ]
        choice7 = random.choice(list7)
        lick2.set_image(url = choice7)
        await ctx.send(embed = lick2)

@bot.command()
async def pat(ctx, *, member : discord.Member=None):
    if not member:
        await ctx.send(f"Please **mention** the person you want to ***pat*** !")

    else:
        author = ctx.message.author.mention
        mention = member.mention
        pat2 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        pat2.description = f"{author} pats {mention}. Looks cute."
        list8 = [
            "https://media.giphy.com/media/q35hchQDS8ro4/giphy.gif",
            "https://cdn.discordapp.com/attachments/391697918106796032/391700185836945418/Shido_patting_kurumi.gif",
            ]
        choice8 = random.choice(list8)
        pat2.set_image(url = choice8)
        await ctx.send(embed = pat2)

@bot.command()
async def smug(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        smug1 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        smug1.description = f"{author} smugs. Uhm.. Okay?"
        smug1.set_image(url = "https://media.giphy.com/media/V6RBCgBmaGLXG/giphy.gif")
        await ctx.send(embed = smug1)

@bot.command()
async def cry(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        cry1 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        cry1.description = f"{author} is crying... ;~;"
        list8 = [
            "https://media.giphy.com/media/lHFzaDCFmbWWA/giphy.gif",
            "http://image.noelshack.com/fichiers/2017/50/6/1513460675-yoshino-crying-and-effect.gif",
            ]
        choice8 = random.choice(list8)
        cry1.set_image(url = choice8)
        await ctx.send(embed = cry1)
    else:
        author = ctx.message.author.mention
        mention = member.mention
        cry2 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        cry2.description = f"{mention} made {author} cry! Kill that boi!"
        list8 = [
            "https://media.giphy.com/media/lHFzaDCFmbWWA/giphy.gif",
            "http://image.noelshack.com/fichiers/2017/50/6/1513460675-yoshino-crying-and-effect.gif",
            ]
        choice8 = random.choice(list8)
        cry2.set_image(url = choice8)
        await ctx.send(embed = cry2)

@bot.command()
async def happy(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        happy1 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        happy1.description = f"{author} is happy! Their smile looks so nice~"
        list9 = [
            "https://media.giphy.com/media/TLJtXsSxLgisw/giphy.gif",
            "https://media.giphy.com/media/bwiimA1Qjw7Ru/giphy.gif",
            "https://i.pinimg.com/originals/d9/e6/d8/d9e6d8957a600ad7196e499097a89c86.gif",
            "http://image.noelshack.com/fichiers/2017/50/6/1513460575-02eb9c0a203a4f25972f42dbc3ac95093bc599c1-hq.gif",
            "https://cdn.discordapp.com/attachments/391697918106796032/391698034255331351/1450669692-d2d7880efb2193a206c9f1ceb9d4cec2.gif",
            ]
        choice9 = random.choice(list9)
        happy1.set_image(url = choice9)
        await ctx.send(embed = happy1)
    else:
        author = ctx.message.author.mention
        mention = member.mention
        happy2 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        happy2.description = f"{mention} made {author} happy! How did they do?!"
        list9 = [
            "https://media.giphy.com/media/TLJtXsSxLgisw/giphy.gif",
            "https://media.giphy.com/media/bwiimA1Qjw7Ru/giphy.gif",
            "https://i.pinimg.com/originals/d9/e6/d8/d9e6d8957a600ad7196e499097a89c86.gif",
            "http://image.noelshack.com/fichiers/2017/50/6/1513460575-02eb9c0a203a4f25972f42dbc3ac95093bc599c1-hq.gif",
            "https://cdn.discordapp.com/attachments/391697918106796032/391698034255331351/1450669692-d2d7880efb2193a206c9f1ceb9d4cec2.gif",
            ]
        choice9 = random.choice(list9)
        happy2.set_image(url = choice9)
        await ctx.send(embed = happy2)

@bot.command()
async def fun(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        fun1 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        fun1.description = f"{author} is having fun! YAAAS!"
        list10 = [
            "https://media.giphy.com/media/R6TwgUiaKINLq/giphy.gif",
            "https://media.giphy.com/media/G4FXmolmlyCzK/giphy.gif",
            ]
        choice10 = random.choice(list10)
        fun1.set_image(url = choice10)
        await ctx.send(embed = fun1)

@bot.command()
async def sing(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        sing1 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        sing1.description = f"{author} is singing! I'm crying of joy.. It's beautiful.."
        list11 = [
            "https://media.giphy.com/media/ipfO8nyNQSVnq/giphy.gif",
            "https://78.media.tumblr.com/ee4a0b429ef702595028100f8eb35202/tumblr_nrj1vvijQW1sz04cbo1_500.gif",
            "https://78.media.tumblr.com/e7fb4fb0110e125d5e30102d8754196e/tumblr_nf004blkOX1r3z16po1_500.gif",
            ]
        choice11 = random.choice(list11)
        sing1.set_image(url = choice11)
        await ctx.send(embed = sing1)

@bot.command()
async def attack(ctx, *, member : discord.Member=None):
    if not member:
        await ctx.send(f"Please **mention** the person you want to ***attack*** !")
    else:
        author = ctx.message.author.mention
        mention = member.mention
        att2 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        att2.description = f"{author} is fighting with {mention}! RUN FOR YOUR LIIIIIFE!"
        list12 = [
            "https://media.giphy.com/media/oSA0F3aL22xGw/giphy.gif",
            "https://media.giphy.com/media/OWK5xYGK0ynNm/giphy.gif",
            "https://cdn.discordapp.com/attachments/391697918106796032/391698034175508480/Tohkas_multiple_punches.gif",
            "https://media.giphy.com/media/KXqBJPZyLjeVy/giphy.gif",
            ]
        choice12 = random.choice(list12)
        att2.set_image(url = choice12)
        await ctx.send(embed = att2)

@bot.command(aliases = ['nom'])
async def eat(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        eat1 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        eat1.description = f"{author} is eating.. Can I have some too please?"
        list13 = [
            "https://media.giphy.com/media/hhZUIO4Yvux44/giphy.gif",
            ]
        choice13 = random.choice(list13)
        eat1.set_image(url = choice13)
        await ctx.send(embed = eat1)

@bot.command()
async def kms(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        kms1 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        kms1.description = f"{author} is killing themselves! STOP THEM BEFORE IT'S TOO LATE!!!"
        list14 = [
            "https://media.giphy.com/media/nzU8Fc5eSybx6/giphy.gif",
            "https://media.giphy.com/media/57aSQAl3FNjwc/giphy.gif",
            ]
        choice14 = random.choice(list14)
        kms1.set_image(url = choice14)
        await ctx.send(embed = kms1)

@bot.command()
async def wink(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        wink1 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        wink1.description = f"{author} is winking. I wonder to who~"
        list15 = [
            "https://media.giphy.com/media/viYADNUVlGSUU/giphy.gif",
            "https://78.media.tumblr.com/ee4a0b429ef702595028100f8eb35202/tumblr_nrj1vvijQW1sz04cbo1_500.gif",
            ]
        choice15 = random.choice(list15)
        wink1.set_image(url = choice15)
        await ctx.send(embed = wink1)

    else:
        author = ctx.message.author.mention
        mention = member.mention
        wink2 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        wink2.description = f"{author} winked to {mention}! I wanna know their secret!"
        list15 = [
            "https://media.giphy.com/media/viYADNUVlGSUU/giphy.gif",
            "https://78.media.tumblr.com/ee4a0b429ef702595028100f8eb35202/tumblr_nrj1vvijQW1sz04cbo1_500.gif",
            ]
        choice15 = random.choice(list15)
        wink2.set_image(url = choice15)
        await ctx.send(embed = wink2)

@bot.command()
async def lewd(ctx, *, member : discord.Member=None):
    if not member:
        author = ctx.message.author.mention
        lewd1 = discord.Embed(colour = discord.Colour(0xE4D7FF))
        lewd1.description = f"{author} is being lewd! Hide your eyes!"
        list16 = [
            "https://media.giphy.com/media/k3T8QjpJ4Z2TK/giphy.gif",
            "https://media.giphy.com/media/X3blcgNZBPD8s/giphy.gif",
            "http://pa1.narvii.com/5819/7acae4a641987e2c3c002a91d8bb738f4f2aaa2b_hq.gif",
            "http://image.noelshack.com/fichiers/2017/50/6/1513460587-tohka-asking-shido-a-favor.gif",
            ]
        choice16 = random.choice(list16)
        lewd1.set_image(url = choice16)
        await ctx.send(embed = lewd1)



############################################################################################################################################################################################################



@bot.command(aliases = ['stats'])
async def about(self):
    stat1 = discord.Embed(colour = discord.Colour(0xE4D7FF))
    servers = len(bot.guilds)
    members=0
    for guild in bot.guilds:
        members+=len(guild.members)
    total_online = len({m.id for m in self.bot.get_all_members() if m.status is not discord.Status.offline})
    total_unique = len(self.bot.users)
    total_bots = len([m.id for m in self.bot.get_all_members() if m.bot])
    categories=0
    for guild in bot.guilds:
        categories+=len(guild.categories)
    channels=0
    for guild in bot.guilds:
        channels+=len(guild.channels)
    texts=0
    for guild in bot.guilds:
        texts+=len(guild.text_channels)
    voices=0
    for guild in bot.guilds:
        voices+=len(guild.voice_channels)

    stat2 = bot.get_user(390478999828037632)

    stat1.set_author(name= stat2)
    stat1.add_field(name= "Members in serverㅤ", value=f"Total Users: **{members}** \nTotal Uniques: **{total_unique}** \nTotal Online: **{total_online}** \nTotal BOTS: **{total_bots}**", inline=True)
    stat1.add_field(name= "Channels in server", value=f"Total Categories: **{categories}** \nTotal Channels: **{channels}** \nText Channels: **{texts}** \nVoice Channels: **{voices}**", inline=True)
    stat1.add_field(name= "Program Informations", value=f"Program Language: **<:Python:453634265197051934> 3.6.3** \nDiscord Program: **Discord.py** \nProgram Version: **1.0.0a**", inline=True)
    stat1.add_field(name= "ㅤRun/Bot Informations", value=f"ㅤRunning on: **Heroku** <:Heroku:453634258041438210>\nㅤEdited with: **Sublime Text 3** <:Sublime:453634264248877056>\n\nㅤ*More with `shelp` command*", inline=True)
    await self.send(embed = stat1)



############################################################################################################################################################################################################



@bot.command(aliases = ['sb'])
async def snowball(ctx, *, member : discord.Member = None):

    number = random.randint(1, 5)

    if not member:
        await ctx.send(f"**{ctx.author.name}**, maybe an option to throw it at someone!")
    elif member is ctx.author:
        await ctx.send(f"**{ctx.author.name}**, maybe an option to throw it at someone else!")
    else:
        if number == 1:
            snowball_hit = [
                f":snowflake: **| {ctx.author.name}**, throws a snowball in **{member.name}**'s face! *ouchh*",
                f":snowflake: **| {ctx.author.name}**, throws a snowball in **{member.name}**'s face! *ouchh*",
                f":snowflake: **| {ctx.author.name}**, throws a snowball in **{member.name}**'s face! *ouchh*",
                f":snowflake: **| {ctx.author.name}**, throws an __iceball__ in **{member.name}**'s face! *ouchh... these ones hurt...*",
                ]

            choice_hit = random.choice(snowball_hit)
            hit = discord.Embed(colour = discord.Colour(0xE4D7FF))
            hit.description = f"{choice_hit}"
            await ctx.send(embed = hit)
        else:
            snowball_miss = [
                f":snowflake: **| {member.name}** dodged the snowball thrown by **{ctx.author.name}**!",
                f":snowflake: **| {ctx.author.name}**, tried to throw a snowball at **{member.name}** and missed!",
                f":snowflake: **| {ctx.author.name}**, missed and threw the snowball through a window! *Oops*",
                f":snowflake: **| {member.name}** laughed at **{ctx.author.name}**, how can you miss me?",
                f":snowflake: **| {ctx.author.name}** tries to use all their energy, and fell on the ground! *definitely a miss*",
                f":snowflake: **| {ctx.author.name}**, tried to throw an __iceball__ at **{member.name}** and missed! Lucky you, **{member.name}**!",
                ]

            choice_miss = random.choice(snowball_miss)
            miss = discord.Embed(colour = discord.Colour(0xE4D7FF))
            miss.description = f"{choice_miss}"
            await ctx.send(embed = miss)



############################################################################################################################################################################################################



@bot.command(aliases =  ['info', 'uinfo', 'user', 'profile'])
async def userinfo(ctx, *, member: discord.Member = None):

    if member is None:
        member = ctx.author

    if member.game is None or member.game.url is None:
        if str(member.status) == "online":
            status_colour = 0x43B581
            status_name = "<:On:453634263926177823> Online"
        elif str(member.status) == "idle":
            status_colour = 0xFAA61A
            status_name = "<:AFK:453634258217598977> Away / Idle"
        elif str(member.status) == "dnd":
            status_colour = 0xF04747
            status_name = "<:dnd:453634258221924372> Do Not Disturb"
        elif str(member.status) == "offline":
            status_colour = 0x000000
            status_name = "<:Off:453634264089755658> Offline"
        elif str(member.status) == "invisible":
            status_colour = 0x000000
            status_name = "<:Invisible:453634258443960321> Invisible"
        else:
            status_colour = member.colour
            status_name = "N/A"
    else:
        status_colour = 0x593695
        status_name = "<:Stream:453634263892623371> Streaming"

    if member.game is None:
        activity = f"**Doing**: Completely nothing!"
    elif member.game.url is None:
        activity = f"**Playing**: {member.game}"
    else:
        activity = f"**Streaming**: [{member.game}]({member.game.url})"

    e = discord.Embed(description = f"**Nickname**: {member.nick}\n{activity}", colour = status_colour)
    roles = [role.name.replace('@', '@\u200b') for role in member.roles]
    shared = sum(1 for m in ctx.bot.get_all_members() if m.id == member.id)

    highrole = member.top_role.name
    if highrole == "@everyone":
        role = "N/A"

    if member.avatar_url[54:].startswith('a_'):
        avi = 'https://cdn.discordapp.com/avatars/' + member.avatar_url[35:-10]
    else:
        avi = member.avatar_url

    if avi:
        e.set_thumbnail(url = avi)
        e.set_author(name = str(member), icon_url = avi)
    else:
        e.set_thumbnail(url = member.default_avatar_url)
        e.set_author(name = str(member), icon_url = member.default_avatar_url)

    if not member.voice:
        mute1 = ":question:"
    else:
        if ctx.author.voice.self_mute == False:
            if ctx.author.voice.mute == True:
                mute1 = "<:mute1:453634259136282635><:mute2:453634259815628800><:mute3:453634263926177802>"
            else:
                mute1 = ":sound:"
        elif ctx.author.voice.self_mute == True:
            if ctx.author.voice.mute == True:
                mute1 = "<:mute1:453634259136282635><:mute2:453634259815628800><:mute3:453634263926177802>"
            else:
                mute1 = ":mute:"

    if not member.voice:
        deaf1 = ":question:"
    else:
        if ctx.author.voice.self_deaf == False:
            if ctx.author.voice.deaf == True:
                deaf1 = "<:mute1:453634259136282635><:mute2:453634259815628800><:mute3:453634263926177802>"
            else:
                deaf1 = ":sound:"
        elif ctx.author.voice.self_deaf == True:
            if ctx.author.voice.deaf == True:
                deaf1 = "<:mute1:453634259136282635><:mute2:453634259815628800><:mute3:453634263926177802>"
            else:
                deaf1 = ":mute:"


    if not member.voice:
        voice = "Not Connected"
    else:
        voice = ctx.author.voice.channel

    e.set_footer(text = f"Member since: {member.joined_at.__format__('%d %b %Y at %H:%M:%S')}")#.timestamp = member.joined_at
    e.add_field(name = 'User ID', value = member.id)
    e.add_field(name = 'Servers', value = f'{shared} shared')
    e.add_field(name = 'Voice Status', value = f"Connected to: **{voice}**\nMicrophone: {mute1}\nSound: {deaf1}")
    e.add_field(name = 'Client Status', value = status_name)
    e.add_field(name = 'Account created at', value = member.created_at.__format__('Date: **%d %b %Y**\nTime: **%H:%M:%S**'))
    e.add_field(name = 'Highest Role', value = highrole)
    e.add_field(name = 'Roles', value = ' **|** '.join(roles) if len(roles) < 15 else f'{len(roles)} roles')

    await ctx.send(embed=e)



############################################################################################################################################################################################################



@bot.command(pass_context = True, aliases = ['feedback', 'fb', 'msgdev'])
async def ctdev(ctx, *, pmessage : str = None):
    invite = await ctx.channel.create_invite(max_uses = 1, xkcd = True)
    bot_owner = 385419569558323202
    dev = bot.get_user(bot_owner)

    if pmessage == None:
        embed = discord.Embed(description = ""+ ctx.author.name +" my developers need to know something right? Type a feedback!", color = 0xE4D7FF)
        await ctx.send(embed = embed)
        await ctx.message.delete()
    else:
            msg = "User: {}\nServer: {}\nFeedBack: {}\nServer Invite: {}".format(ctx.author, ctx.guild, pmessage, invite.url)
            embed = discord.Embed(title = "Invite to {} discord server!".format(ctx.guild), colour = 0xE4D7FF, url = "{}".format(invite.url), description = "Feedback: {}".format(pmessage), timestamp = datetime.datetime.utcfromtimestamp(1507439238))
            embed.set_thumbnail(url = "{}".format(ctx.author.avatar_url))
            embed.set_author(name = "{} sent:".format(ctx.author), icon_url = "{}".format(ctx.author.avatar_url))
            await dev.send(embed = embed)
#            await dev.send(msg)
            embed = discord.Embed(description = "I have PMed **{}#{}** with your feedback! Thank you for your help!".format(dev.name, dev.discriminator), color = 0xE4D7FF)
            await ctx.send(embed = embed)
            await ctx.message.delete()
#            return await ctx.send(ctx.author.mention + " I have PMed my creator your feedback! Thank you for the help!")



############################################################################################################################################################################################################



@bot.command(aliases = ['pfp'])
async def avatar(ctx, *, member : discord.Member = None):
	author = ctx.author

	if not member:
		member = author

	if member.avatar:
		if member.avatar_url[54:].startswith('a_'):
			avi = 'https://cdn.discordapp.com/avatars/' + member.avatar_url[35:-10]
			avi_description = f"**{member.name}'s** avatar!\n[Click to open avatar!]({avi})"
		else:
			avi = member.avatar_url_as(static_format = "png", size = 1024)
			avi_description = f"**{member.name}'s** avatar!\n[Click to open avatar!]({avi})"
	else:
		avi_description = f"**{member.name}** has no avatar!\n"
		avi = "https://i.imgur.com/lkeELEJ.png"

	embed = discord.Embed(description = f"{avi_description}", color =  discord.Colour(0xE4D7FF))
	embed.set_image(url = f"{avi}")
	await ctx.send(embed = embed)



############################################################################################################################################################################################################



@bot.command(aliases = ['gicon'])
async def guildicon(ctx):
	guild = ctx.guild

	if guild.icon_url:
		embed = discord.Embed(description = f"**{guild.name}'s** guild icon!\n[Click to open {guild.name}'s guild icon!]({guild.icon_url})", color =  discord.Colour(0xE4D7FF))
		embed.set_image(url = f"{guild.icon_url}")
		await ctx.send(embed = embed)
	else:
		embed = discord.Embed(description = f"**{guild.name}** has no icon!\n", color =  discord.Colour(0xE4D7FF))
		embed.set_image(url = "https://i.imgur.com/lkeELEJ.png")
		await ctx.send(embed = embed)



############################################################################################################################################################################################################



@bot.command(aliases = ['virtualhug'])
async def vhug(ctx, *, member : discord.Member = None):

	author = ctx.author
	if not member:
		await ctx.send("Please mention a user to send a hug to")
	else:
		member = member.mention

		message = await ctx.send(f"[⠀▓▓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀] / virtual-hug.exe Packing files..")
		await asyncio.sleep(1)
		await message.edit(content = f"[⠀▓▓▓▓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀] / virtual-hug.exe Packing files..")
		await asyncio.sleep(1)
		await message.edit(content = f"[⠀▓▓▓▓▓▓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀] / virtual-hug.exe Packing files..")
		await asyncio.sleep(2)
		await message.edit(content = f"[⠀▓▓▓▓▓▓▓▓▓▓▓▓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀] / virtual-hug.exe Packing files..")
		await asyncio.sleep(1)
		await message.edit(content = f"[⠀▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓⠀⠀⠀⠀] / virtual-hug.exe Packing files..")
		await asyncio.sleep(1)
		await message.edit(content = f"[⠀▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓⠀] / virtual-hug.exe Packing files..")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Sending Virtual Hug.")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Sending Virtual Hug..")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Sending Virtual Hug...")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Sending Virtual Hug....")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Sending Virtual Hug.")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Sending Virtual Hug..")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Sending Virtual Hug...")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Sending Virtual Hug....")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Sending Virtual Hug.")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Sending Virtual Hug..")
		await asyncio.sleep(0.50)
		await message.edit(content = f"Sending Virtual Hug...")
		await asyncio.sleep(2)
		await message.edit(content = f"Successfully sent ***__virtual-hug.exe__***  to **{member}**")



############################################################################################################################################################################################################



@bot.group(invoke_without_command = True)
async def cute(ctx):

	await ctx.send(f"**{ctx.author.name}**, please use one of the following options: `cats`, `dogs` or `neko`")

@cute.command(name = 'cats')
async def cute_cats(ctx):

	async with aiohttp.ClientSession() as session:
		async with session.get("https://random.cat/meow") as r:
			if r.status == 200:
				response = await r.json()
				embed = discord.Embed(description = "Here is your random cute Cat.", color =  discord.Colour(0xE4D7FF))
				embed.set_image(url = response['file'])
				await ctx.send(embed = embed)	
			else:
				await ctx.send(f'**{ctx.author.name}**, could not access the random.cat API!')

@cute.command(name = 'dogs')
async def cute_dogs(ctx):

	async with aiohttp.ClientSession() as session:
		async with session.get("https://api.thedogapi.co.uk/v2/dog.php") as r:
			if r.status == 200:
				response = await r.json()
				embed = discord.Embed(description = "Here is your random cute Dog.", color =  discord.Colour(0xE4D7FF))
				embed.set_image(url = response['data'][0]["url"])
				await ctx.send(embed = embed)
			else:
				await ctx.send(f'**{ctx.author.name}**, could not access the random.dog API!')

@cute.command(name = 'neko')
async def cute_neko(ctx):

	async with aiohttp.ClientSession() as session:
		async with session.get("https://nekos.life/api/neko") as r:
			if r.status == 200:
				nekos = await r.json()
				embed = discord.Embed(description = "Here is your random cute Neko Girl.", color =  discord.Colour(0xE4D7FF))
				embed.set_image(url = nekos['neko'])
				await ctx.send(embed = embed)
			else:
				await ctx.send(f'**{ctx.author.name}**, could not access the Nekos.life API!')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if not os.environ.get('TOKEN'):
        print("No token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))
