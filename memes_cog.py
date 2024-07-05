import discord, random
from time import sleep
from discord.ext import commands

ffmpeg_options = {'options': '-vn'}

class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def play_mp3(self, ctx, file):
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None
        if not voice_channel:
            return await ctx.send("You aren't in a voice chat, idiot")
        if not ctx.voice_client:
            await voice_channel.connect()
        
        ctx.voice_client.play(discord.FFmpegPCMAudio(f"./soundbites/{file}", **ffmpeg_options))
    
    @commands.command()
    async def dug(self, ctx):
        await ctx.send("https://tenor.com/view/side-eye-dog-suspicious-look-suspicious-doubt-dog-doubt-gif-23680990")
    
    @commands.command()
    async def dag(self, ctx):
        await ctx.send("https://tenor.com/view/side-eye-dog-worried-scared-look-gif-23041456")
        
    @commands.command()
    async def cet(self, ctx):
        await ctx.send("https://media.discordapp.net/attachments/944047767288954950/1251883420141879346/Screenshot_20240616_085726_Instagram.jpg?ex=6672d5ca&is=6671844a&hm=889a2c026171cb43adb6701e2adda5b1738cbf8cf7920a06f4d92b68e7155f7b&=&format=webp&width=663&height=663")
       
    @commands.command()
    async def eepy(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/724815563246796820/1257152475761213470/AP1GczMijr0kKgdSxQggfC-o2me1XNZ6N_Xc_vKUK6Svyiubvd85XQspQUS8w746-h995-s-no-gm.png?ex=668406ba&is=6682b53a&hm=3904c105f7e69326bd70fe8b6a14e9d0dbd656c597a4a94caed422c46adbe124&")
        
    @commands.command()
    async def deg(self, ctx):
        await ctx.send("https://cdn.discordapp.com/attachments/724815563246796820/1257153143666638898/PXL_20210705_191440911.jpg?ex=6684075a&is=6682b5da&hm=dc5e8d35a48da924542fba39f37b61d345b0599046087ee99cb90fef0b57bed9&")
