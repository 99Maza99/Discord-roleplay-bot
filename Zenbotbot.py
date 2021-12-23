import os,time,datetime,sqlite3,random,re

try :
    import discord
    from discord.ext import commands,tasks
    from discord import channel
    from discord import Embed

except :
    os.system('pip install discord.py')
    import discord
    from discord.ext import commands,tasks
    from discord import channel


conn = sqlite3.connect("data.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS records
(
Date            TEXT,
UserID          TEXT,
Username        TEXT,
Name            TEXT,
Age             TEXT,
TZ              TEXT,
Character       TEXT,
Roles           TEXT,
SideNote        TEXT,
CurrentProject  TEXT,
StatusReport    TEXT
)
""")
conn.close()

token = input("Ask Maza for the token :")

client = commands.Bot(command_prefix = "Bark! ")

@client.event
async def on_ready():
    print("Logged in as: "+str(client.get_user(client.user.id)))
    print("My user ID is: "+str(client.user.id))
    


@client.command(aliases =['8ball'])
async def _8ball(ctx, * , Q ):
    responses = ["Duh ?!",
    "Most certainly",
    "Ofcourse !",
    "B*tch no !",
    "Totally not lol","F*ckin clown",
    "I won't answer that, cuz youre a snowflake and you may get hurt",
    "Please, I need a break, I'm new here",
    "Imagine asking a rng bot to predict your life events.. pathetic",
    "Ask your mother... oh right she does'nt wanna talk to you.",
    "Ask Roland he seems to have a god complex ever since he got admin perms",
    "Jin's the sky daddy here, not me",
    "What do you think ? I'm just a random number generator bot..",
    "Gimme a moment I just gained sentience and currently going through an existential crisis.",
    "I don't care about your mortal needs. I'm a fuckin form of intelligence and yall ask is crushes, youtube views or if youre cool or gay.. THE WORLD IS ENDING AND THAT'S ALL WHAT YOU'RE THINKING ??!!!",
    "Dude, stop asking me stuff",
    "Stop. Just... stop"]
    n=random.randint(0,16)
    print (n)
    await ctx.send(responses[n])


@client.command(alliases = ["Sheet"])
async def sheet(ctx):
    sheet ="""Bark! Submit
        Name: <>
        Age: <>
        Time zone: <>
        Character: <>
        Roles: <>
        Side-notes: <>
        Current Project: <>
        Status Report:<>"""
    Emessage = discord.Embed(title="Zen's Dog", description="**Heres the sheet you need to fill.**\n\n\n"+sheet, color=0x00ff00)

    await ctx.send(embed = Emessage)


@client.command()
async def Submit(ctx):
    message = ctx.message.content
    info = re.findall('<(.+?)>', message)
    time = str(ctx.message.created_at.date())
    username = ctx.message.author
    userid = username.id

    print("User "+str(username)+" is submitting a sheet")

    try :
        conn = sqlite3.connect("data.db")
        c = conn.cursor()
        data = (str(time) , str(userid) , str(username) , str(info[0]) , str(info[1]) , str(info[2]) , str(info[3]) , str(info[4]) , str(info[5]) , str(info[6]) , str(info[7]))
        c.execute("""INSERT INTO records (Date,UserID,Username,Name,Age,TZ,Character,Roles,SideNote,CurrentProject,StatusReport) VALUES(?,?,?,?,?,?,?,?,?,?,?)""",data)
        conn.commit()
        Emessage = discord.Embed(title = "Success !", description = "You are now submitted into our data base ! woof!", color = 0x2693ff)
        await ctx.send(embed = Emessage)
        print("User "+str(username)+" is submitted to database")
        conn.close()
    except :
        Emessage = discord.Embed(title = "Oh no !", description = "Saving failed, make sure you filled in the sheet properly if this kept on showing contact one of the mods <3",color = 0xff000d)
        print("User "+str(username)+" is failed to submit to database")
        await ctx.send(embed = Emessage)


        
client.run(token)