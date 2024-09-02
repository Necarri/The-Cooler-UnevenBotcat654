import discord, random
from time import sleep
import asyncio
from discord.ext import commands

ffmpeg_options = {'options': '-vn'}

class Soundboard(commands.Cog):

    is_hungry = False

    def __init__(self, bot):
        self.bot = bot
    
    async def play_mp3(self, ctx, file):
        await self.ltg(ctx)
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None
        if not voice_channel and not ctx.voice_client:
            return await ctx.send("You aren't in a voice chat, idiot")
        if not ctx.voice_client:
            await voice_channel.connect()
        
        ctx.voice_client.play(discord.FFmpegPCMAudio(f"./soundbites/{file}", **ffmpeg_options))

    
    async def ltg(self, ctx):
        try:
            if random.randrange(0,200) == 1:
                await self.play_mp3(ctx, "ltg.mp3")
                await ctx.send("kill yourself")
                await ctx.send("https://tenor.com/view/low-tier-god-awesome-mario-twerking-gif-23644561")
                return
        except Exception as e:
                print(e) 

    @commands.command(name="hboxmode", description="Toggle Hbox popoff mode")
    async def hboxmode(self, ctx):
        await ctx.send("Popoff mode enabled")

        self.is_hungry = not self.is_hungry
        if self.is_hungry:
            while (1<2):
                await self.hbox(ctx)
                x = random.randrange(150,600)
                await asyncio.sleep(x)
                if not self.is_hungry:
                    return
        await ctx.send("Popoff mode disabled")

    @commands.command(name="badoop", description="Discord notification sound")
    async def badoop(self, ctx):
        await self.play_mp3(ctx, "ping.mp3")
        
            
    @commands.command(name="bruh", description="Bruh")
    async def bruh(self, ctx):
        await self.play_mp3(ctx, "bruh.mp3")

    @commands.command(description="Knocking sound effect")
    async def knock(self, ctx):
        await self.play_mp3(ctx, "knock.mp3")

    @commands.command(description="Lego Star Wars Lando death sound")
    async def lando(self, ctx):
        await self.play_mp3(ctx, "lando.mp3")

    @commands.command(description="I am the eggman, it's what I am")
    async def eggman(self, ctx):
        await self.play_mp3(ctx, "eggman.mp3")
    
    @commands.command(description="Lego Star Wars Yoda death sound")
    async def yoda(self, ctx):
        await self.play_mp3(ctx, "yoda.mp3")
    
    @commands.command(description="Gay (with reverb)")
    async def gay(self, ctx):
        await self.play_mp3(ctx, "gay-echo.mp3")
    
    @commands.command(description="The sisyphus meme song")
    async def sisyphus(self, ctx):
        await self.play_mp3(ctx, "sisyphus.mp3")
    
    @commands.command(description="You know what this is")
    async def fart(self, ctx):
        await self.play_mp3(ctx, "fart_reverb.mp3")
    
    @commands.command(description="Huh cat")
    async def huh(self, ctx):
        await self.play_mp3(ctx, "huh.mp3")
    
    @commands.command(description="Lego Star Wars IG-88 death sound")
    async def ig88(self, ctx):
        await self.play_mp3(ctx, "ig88.mp3")
    
    @commands.command(description="Trump saying I\"m gonna come\"")
    async def come(self, ctx):
        await self.play_mp3(ctx, "imgonnacome.mp3")
    
    @commands.command(description="Cat doorbell meme MEAURGH")
    async def meow(self, ctx):
        await self.play_mp3(ctx, "meowrgh.mp3")
    
    @commands.command(description="Old TV ad with the old guy with the fishing pole and the 1 dollar bill")
    async def q(self, ctx):
        await self.play_mp3(ctx, "quickerthanthat.mp3")
        await ctx.send("https://tenor.com/view/allstate-gotta-be-quicker-than-that-fishing-gif-11607646")

    @commands.command(description="Caseoh saying \"shrimp alfredo\" then singing")
    async def caseoh(self, ctx):
        await self.play_mp3(ctx, "shrimpalfredo.mp3")
    
    @commands.command(description="The Rock saying \"shut up bitch\"")
    async def rock(self, ctx):
        await self.play_mp3(ctx, "shutupb.mp3")

    @commands.command(description="Biden saying \"SODAAAAAAA!\"")
    async def soda(self, ctx):
        await self.play_mp3(ctx, "soda.mp3")
    
    @commands.command(description="Earthbound \"what, how\" meme")
    async def how(self, ctx):
        await self.play_mp3(ctx, "what.mp3")
    
    @commands.command(description="Hatsune Miku does NOT talk to british people")
    async def ohno(self, ctx):
        await self.play_mp3(ctx, "no.mp3")

    @commands.command(description="Randomly selects a Michael Jackson noise")
    async def mj(self, ctx):
        mj_sound_names = [
            'hehe',
            'yow',
            'wow',
            'oh',
            'shamone',
            'hoooo',
            'huoo',
            'uul',
            'dah',
            'aow',
            'heeee'
        ]
            #Needs a way to not roll the same thing twice.
        choice = random.choice(mj_sound_names)
        await self.play_mp3(ctx, f"mj/{choice}.mp3")
    
    @commands.command(description="Randomly selects an hbox popoff")
    async def hbox(self, ctx):
        hb_sound_names = [
            'AAAAAAAAAAA su',
            'ahh i got it i effing hit it',
            'calm yourself down juan',
            'i did it i effing did it',
            'omg oh my no effing way',
            'omg ok ok ok',
            'OOHh mY gOOOD',
            'remember my name remember the effing name dont taunt me',
            'WAAAAAAAAAaaaaaaaaaaaaaaaaaauuuuuuuuuuuuuuu',
            'wait omg aaAAAA',
            'what are you gonna do',
            'what the eff',
            'YAAAAAAAAASS passes out',
            'YAAAAAS WAAAAUuUuuuuu',
            'yeaaas yeas motherfricker',
            'yes eff yes yes yes WOOO',
            'yes eff you camping yellow eff',
            'yes f that character',
            'yes yeah yes yeaaaaaah eff'
        ]
            #Needs a way to not roll the same thing twice.
        choice = random.choice(hb_sound_names)
        await self.play_mp3(ctx, f"hbox/{choice}.mp3")   
    
    

    @commands.command(description="Counts down from 3, stars at drop after LET\'S GO")
    async def countdown(self, ctx):
        await self.play_mp3(ctx, "letsgo.mp3")
        sleep(0.5)
        await ctx.send("3...")
        sleep(1)
        await ctx.send("2...")
        sleep(1)
        await ctx.send("1...")
        sleep(1)
        await ctx.send("https://tenor.com/view/shocking-jar-jar-star-wars-cringe-gif-13662647")
        