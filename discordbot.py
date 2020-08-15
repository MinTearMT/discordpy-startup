from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def MinT(ctx):
    await ctx.send('ぬん')


@bot.command()
async def あ(ctx):
    await ctx.send('あ！')


// Response for Uptime Robot
const http = require('http');
http.createServer(function(request, response)
{
  response.writeHead(200, {'Content-Type': 'text/plain'});
  response.end('Discord bot is active now \n');
}).listen(3000);
client.on('ready', message =>
{


  client.user.setPresence({ game: { name: 'MinT.net' } });  
  console.log('bot is ready!');
});


import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('おはよう'):
        await message.channel.send('おはよ！　つД｀)')

client.run('your token here')


bot.run(token)
