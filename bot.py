import guilded, random, sys, time
from guilded.ext import commands
from guilded import Message

pasta = [
    "FUCKED BY T.G.T"
] #описания для ембедов
imgs = [
    "https://media.discordapp.net/attachments/927631452554793010/933809167330857000/standard.gif",
    "https://cdn.discordapp.com/attachments/942518862082080848/991625170102005811/1561765551_ezgif-5-4a52584cd17a.gif",
    "https://cdn.discordapp.com/attachments/942518862082080848/991625169846157372/16208348175771.gif",
    "https://cdn.discordapp.com/attachments/942518862082080848/991625127810826260/1462735619_dickflash.gif",
    "https://cdn.discordapp.com/attachments/942518862082080848/991624391542722650/image0-15-1-1.gif",
    "https://cdn.discordapp.com/attachments/942518862082080848/991624266934145065/786964654009483284.gif",
    "https://cdn.discordapp.com/attachments/942518862082080848/991624266481143879/valakas-glad.gif",
    "https://cdn.discordapp.com/attachments/942518862082080848/991624267903025222/d.gif"
] #гифки и пикчи для ембедов
invite = "https://www.guilded.gg/i/2VV7W792"#приглос на ваш серв
email = sys.argv[1]
passwd = sys.argv[2]

client = commands.UserbotBot(command_prefix=".")

@client.event
async def on_ready():
    print(f'client {client.user_id} is ready')


@client.command()
async def a(ctx):
    ctx.send("a") 

@client.event
async def on_message(message):
    #await client.process_commands(message)
    if message.content == 'ping':
        await message.channel.send('pong!')
    elif message.content == 'qg65':
        ican = True
        print("ebashy")
        i = 0
        while message.guild in client.guilds:
            i += 1
            try:
                embed = guilded.Embed(title=f"{invite} <-- Join TGT", description = random.choice(pasta)+f" \n {invite} \n {invite} \n {invite} \n {invite}", url = invite)
                embed.set_image(url = random.choice(imgs))
                #await channel.send(embed)
                if (len(message.guild.members) == 0):
                    a = "suck dick"
                else:
                    a = random.choice(message.guild.members).mention
                if random.randint(1,3) > 1 and ican:
                    await message.channel.send(embed = embed,content = guilded.Mention.everyone)
                else:
                    await message.channel.send(embed = embed,content = a)
                time.sleep(0.6)
            except Exception as e:
                print(e)
                if str(e).lower().__contains__("mention"):#idk how to do that
                    ican = False
            print(f"{i} Message Sent ({client.user.name})")
    elif message.content == 'FUCKED by TGT':
        e = guilded.Embed(title = "a")
        #e.set_image(url=random.choice(imgs))
        msg = guilded.Mention.everyone
        await message.channel.send(link = invite)

client.run(email,passwd)
