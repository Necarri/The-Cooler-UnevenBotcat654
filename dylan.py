import discord
import os
from discord.ext import commands
from time import sleep
from dotenv import load_dotenv
import http.client as httplib
import yt_dlp
import asyncio
from commands_cog import commands_cog

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
client = commands.Bot(command_prefix="!", activity=discord.Game(name='type !help to list commands'), intents=intents)
#client.remove_command('help')

ffmpeg_options = {'options': '-vn'}
ydl_options = {'format' : 'bestaudio', 'noplaylist' : True}

while (1<2):
    conn = httplib.HTTPSConnection("8.8.8.8", timeout=5)
    try:
        conn.request("HEAD", "/")
        break
    except Exception:
        #print ("Sugma")
        sleep(1)
        continue
conn.close()
print('Connected to internet')

class MusicBot(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.queue = []
    
    @commands.command(name="play", description="play a song by search or pasting a link directly")
    async def play(self, ctx, *, search):
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None
        if not voice_channel:
            return await ctx.send("You aren't in a voice chat, idiot")
        if not ctx.voice_client:
            await voice_channel.connect()

        async with ctx.typing():
             with yt_dlp.YoutubeDL(ydl_options) as ydl:
                info = ydl.extract_info(f"ytsearch:{search}", download=False)
                if 'entries' in info:
                    info = info['entries'][0]
                    url = info['url']
                    title = info['title']
                    self.queue.append((url, title))
                    await ctx.send(f'Added **{title}**)')
        if not ctx.voice_client.is_playing():
            await self.play_next(ctx)

    async def play_next(self, ctx):
        if self.queue:
            url, title = self.queue.pop(0)
            source = await discord.FFmpegOpusAudio.from_probe(url, **ffmpeg_options)
            ctx.voice_client.play(source, after=lambda _:self.client.loop.create_task(self.play_next(ctx)))
            await ctx.send(f'Now playing **{title}**')
        elif not ctx.voice_client.is_playing():
            await ctx.send("Queue is empty")
    
    @commands.command(name="sop", description="sop")
    async def sop(self, ctx):
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None
        await ctx.send("sop\nhttps://tenor.com/view/sop-sign-simpsons-gif-9846341633978797724")
        try:
            await voice_channel.disconnect()
        except Exception as e:
            print(e)
   
    @commands.command(name="kill", description="Remove bot from voice channel")
    async def kill(self, ctx):
        try:
            del ctx.voice_client
        except Exception as e:
            print(e)
    
    @commands.command(name="skip", description="Skips current song in queue")
    async def skip(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.stop()
            await ctx.send("Skipped")
    
    @client.event
    async def on_ready():
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name='sick tunes'))
        print(f'{client.user} is now ballin\'')

async def main():
    await client.add_cog(MusicBot(client))
    await client.add_cog(commands_cog(client))
    await client.start(os.getenv('TOKEN'))

asyncio.run(main())