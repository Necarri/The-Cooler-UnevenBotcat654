import discord
import random
from time import sleep
from discord.ext import commands

ffmpeg_options = {'options': '-vn'}

class commands_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def sbping(self, ctx):
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None
        if not voice_channel:
                return await ctx.send("You aren't in a voice chat, idiot")
        if not ctx.voice_client:
             await voice_channel.connect()
        ctx.voice_client.play(discord.FFmpegPCMAudio("soundbites/ping.mp3", **ffmpeg_options))
    
    @commands.command()
    async def bruh(self, ctx):
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None
        if not voice_channel:
                return await ctx.send("You aren't in a voice chat, idiot")
        if not ctx.voice_client:
            await voice_channel.connect()
        ctx.voice_client.play(discord.FFmpegPCMAudio("soundbites/bruh.mp3", **ffmpeg_options))

    @commands.command()
    async def knock(self, ctx):
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None
        if not voice_channel:
                return await ctx.send("You aren't in a voice chat, idiot")
        if not ctx.voice_client:
             await voice_channel.connect()
        ctx.voice_client.play(discord.FFmpegPCMAudio("soundbites/knock.mp3", **ffmpeg_options))

    @commands.command()
    async def lando(self, ctx):
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None
        if not voice_channel:
                return await ctx.send("You aren't in a voice chat, idiot")
        if not ctx.voice_client:
             await voice_channel.connect()
        ctx.voice_client.play(discord.FFmpegPCMAudio("soundbites/lando.mp3", **ffmpeg_options))

    @commands.command()
    async def eggman(self, ctx):
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None
        if not voice_channel:
                return await ctx.send("You aren't in a voice chat, idiot")
        if not ctx.voice_client:
             await voice_channel.connect()
        ctx.voice_client.play(discord.FFmpegPCMAudio("soundbites/eggman.mp3", **ffmpeg_options))
    
    @commands.command()
    async def yoda(self, ctx):
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None
        if not voice_channel:
                return await ctx.send("You aren't in a voice chat, idiot")
        if not ctx.voice_client:
             await voice_channel.connect()
        ctx.voice_client.play(discord.FFmpegPCMAudio("soundbites/yoda.mp3", **ffmpeg_options))
    
    @commands.command()
    async def gay(self, ctx):
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None
        if not voice_channel:
                return await ctx.send("You aren't in a voice chat, idiot")
        if not ctx.voice_client:
             await voice_channel.connect()
        ctx.voice_client.play(discord.FFmpegPCMAudio("soundbites/gay-echo.mp3", **ffmpeg_options))
    
    @commands.command()
    async def sisyphus(self, ctx):
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None
        if not voice_channel:
                return await ctx.send("You aren't in a voice chat, idiot")
        if not ctx.voice_client:
             await voice_channel.connect()
        ctx.voice_client.play(discord.FFmpegPCMAudio("soundbites/sisyphus.mp3", **ffmpeg_options))
    
    @commands.command()
    async def soda(self, ctx):
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None
        if not voice_channel:
                return await ctx.send("You aren't in a voice chat, idiot")
        if not ctx.voice_client:
             await voice_channel.connect()
        ctx.voice_client.play(discord.FFmpegPCMAudio("soundbites/soda.mp3", **ffmpeg_options))
    
    @commands.command()
    async def mj(self, ctx,):
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None
        if not voice_channel:
                return await ctx.send("You aren't in a voice chat, idiot")
        if not ctx.voice_client:
             await voice_channel.connect()
        
        #I want to try making all 11 in a row so it won't start again until every one has been played
        choice = random.choice(range(0,11))
        match choice:
            case 0:
                ctx.voice_client.play(discord.FFmpegPCMAudio("soundbites/mj/hehe.mp3", **ffmpeg_options))
            case 1:
                ctx.voice_client.play(discord.FFmpegPCMAudio("soundbites/mj/yow.mp3", **ffmpeg_options))
            case 2:
                ctx.voice_client.play(discord.FFmpegPCMAudio("soundbites/mj/wow.mp3", **ffmpeg_options))
            case 3:
                ctx.voice_client.play(discord.FFmpegPCMAudio("soundbites/mj/oh.mp3", **ffmpeg_options))
            case 4:
                ctx.voice_client.play(discord.FFmpegPCMAudio("soundbites/mj/shamone.mp3", **ffmpeg_options))
            case 5:
                ctx.voice_client.play(discord.FFmpegPCMAudio("soundbites/mj/hoooo.mp3", **ffmpeg_options))
            case 6:
                ctx.voice_client.play(discord.FFmpegPCMAudio("soundbites/mj/huoo.mp3", **ffmpeg_options))
            case 7:
                ctx.voice_client.play(discord.FFmpegPCMAudio("soundbites/mj/uul.mp3", **ffmpeg_options))
            case 8:
                ctx.voice_client.play(discord.FFmpegPCMAudio("soundbites/mj/dah.mp3", **ffmpeg_options))
            case 9:
                ctx.voice_client.play(discord.FFmpegPCMAudio("soundbites/mj/aow.mp3", **ffmpeg_options))
            case 10:
                ctx.voice_client.play(discord.FFmpegPCMAudio("soundbites/mj/heeee.mp3", **ffmpeg_options))
            #case _:
            #    ctx.send("What")
    
    
    @commands.command()
    async def countdown(self, ctx):
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None
        if not voice_channel:
                return await ctx.send("You aren't in a voice chat, idiot")
        if not ctx.voice_client:
             await voice_channel.connect()
        
        ctx.voice_client.play(discord.FFmpegPCMAudio("soundbites/letsgo.mp3", **ffmpeg_options))
        sleep(0.5)
        await ctx.send("3...")
        sleep(1)
        await ctx.send("2...")
        sleep(1)
        await ctx.send("1...")
        sleep(1)
        await ctx.send("https://tenor.com/view/shocking-jar-jar-star-wars-cringe-gif-13662647")
        ctx.voice_client.play(discord.FFmpegPCMAudio("soundbites/go.mp3", **ffmpeg_options))
    
    @commands.command()
    async def dug(self, ctx):
        try:
            await ctx.send("https://tenor.com/view/side-eye-dog-suspicious-look-suspicious-doubt-dog-doubt-gif-23680990")
        except Exception as e:
            print(e)
    @commands.command()
    async def dag(self, ctx):
        try:
            await ctx.send("https://tenor.com/view/side-eye-dog-worried-scared-look-gif-23041456")
        except Exception as e:
            print(e)

    @commands.command()
    async def cet(self, ctx):
        try:
            await ctx.send("https://media.discordapp.net/attachments/944047767288954950/1251883420141879346/Screenshot_20240616_085726_Instagram.jpg?ex=6672d5ca&is=6671844a&hm=889a2c026171cb43adb6701e2adda5b1738cbf8cf7920a06f4d92b68e7155f7b&=&format=webp&width=663&height=663")
        except Exception as e:
            print(e)
    
    @commands.command()
    async def eepy(self, ctx):
        try:
            await ctx.send("https://cdn.discordapp.com/attachments/724815563246796820/1257152475761213470/AP1GczMijr0kKgdSxQggfC-o2me1XNZ6N_Xc_vKUK6Svyiubvd85XQspQUS8w746-h995-s-no-gm.png?ex=668406ba&is=6682b53a&hm=3904c105f7e69326bd70fe8b6a14e9d0dbd656c597a4a94caed422c46adbe124&")
        except Exception as e:
            print(e)

    @commands.command()
    async def deg(self, ctx):
        try:
            await ctx.send("https://cdn.discordapp.com/attachments/724815563246796820/1257153143666638898/PXL_20210705_191440911.jpg?ex=6684075a&is=6682b5da&hm=dc5e8d35a48da924542fba39f37b61d345b0599046087ee99cb90fef0b57bed9&")
        except Exception as e:
            print(e)
