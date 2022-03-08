import discord
import time
from utils import joke as jk
from utils import dictionary as dis
from utils import meme
from utils import fb 

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('Bot is online')
    past = ['a']

    while True:
        time.sleep(30)
        data = fb.scrape()
    
        if data['post_id'] != past[0]:
            past.pop()
            past.append(data['post_id'])

            ch = client.get_channel(948215784788881439)
            edata = discord.Embed(title='New post',
                        description=data['text'],
                        color=0xffffff)
            edata.set_image(url = data['image'])
            await ch.send(embed=edata)

        time.sleep(300)

##################################################################################

@client.event
async def on_member_join(member):
    ch = client.get_channel(947855619728220161)
    data = discord.Embed(title='Welcome to White House clz server',
                        description=f'<@{member.id}>Enjoy your stay here and take respective roles from <#948019433094398002>',
                        color=0x206694)
    await ch.send(embed=data)                    


@client.event
async def on_message(message):
    msg = message.content
    if message.author == client.user:
        return

    if msg.startswith('..hello'):
        await message.channel.send('Hi')

    if msg.startswith('..joke'):
        jok = jk.get_joke()
        data = discord.Embed(title=jok[0]['question'],
                             description='**'+jok[0]['punchline']+'**',
                             color=discord.Color.blue())
        await message.channel.send(embed=data)

    if msg.startswith('..find'):
        word = msg.split("..find ",1)[1]
        data = dis.find(word)
        await message.channel.send(data[0]['meanings'][0]['definitions'][0]['definition'])  

    if msg.startswith('..meme'):
        data = discord.Embed()
        data.set_image(url = meme.get_meme())
        await message.channel.send(embed=data)
    



#########################################################################################
client.run('token')
