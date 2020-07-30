# add on_delete_message()

import discord
from discord.ext import commands
from discord.utils import get

import random, subprocess
import io, aiohttp

from googlesearch import search
import youtube_dl

import urbandictionary as ud

client = commands.Bot(command_prefix = "", case_insensitive = True)





#youtubesettings = {}
#ytdl = youtube_dl.YoutubeDL(youtubesettings)

#ffmpeg-settings = {}

@client.event
async def on_ready():
    print("-"*10)
    print("Bot loading...")
    print()
    print("All systems, good to go.")
    print("-"*10)

# Ping
@client.command(aliases=["whatistheping", "whatstheping", "wotisleping"])
async def ping(ctx):
    await ctx.send(f"Pong! The ping is {round(client.latency * 1000)}ms.")

# Magic 8-Ball
@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    responses = ["_Sure, honey, sure._", "You really need to ask?", "Of course, bruv.", "Bhai mai bhagwaan nahi hoon", "DUH.", "Never in a million years", "Koi chance hi nahi hai boss", "_Mayyyyybeeeee_", "Definitely", "Why even-", "Ghanta."]
    await ctx.send(random.choice(responses))

# Clear
@client.command()
async def clear(ctx, amount=0):
    await ctx.channel.purge(limit=amount)

# Chandler
@client.command()
async def chandler(ctx, name, *, adj):
    if name == "more" or name == "less" or adj == "more" or adj == "less":
        pass
    else:
        await ctx.channel.purge(limit=1)
        await ctx.send(f"Could {name} BE any {adj}?")

# Introduction
@client.command(aliases=["whatisedith, whatsedith, introduction"])
async def edith(ctx):
    await ctx.send("> Heyo, this is Edith. \n> A bot designed to mess around with you. \n> Bask in the sheer suffering that I shall wreak upon your puny existences, \n> And a little bit of fun, too. :)")

@client.command()
async def i(ctx, *, hopefullyaquote):
    if hopefullyaquote.lower() == "am inevitable":
        await ctx.send("And I... am... Iron Man.")
    elif hopefullyaquote.lower() == "am iron man":
        await ctx.send("Bhak gadhdhe, tu ni hai.")
    else:
        pass

@client.command(aliases=["googlesearch"])
async def google(ctx, *, query):
    for j in search(query, lang="en", safe="off", num=3, stop=3, pause=2, verify_ssl=True):
        await ctx.send(j)

@client.command(aliases=["urbandict", "define", "ud"])
async def urbandictionary(ctx, *, term):
    definitions = ud.define(term)
    await ctx.send(f"> **_{definitions[0].word.title()}_**")
    for i in range(0, 3):
        tempDef = definitions[i].definition.replace("[", "").replace("]", "").replace("\n", "\n> \t")
        tempEx = definitions[i].example.replace("[", "").replace("]", "").replace("\n", "\n> \t")
        await ctx.send(f"> **{i+1}.** \n> \t{tempDef} \n> \t_\"{tempEx}\"_")

@client.command(aliases=["philsosophy"])
async def dadjoke(ctx):
    dadjokes = eval(subprocess.check_output("curl -H \"Accept: application/json\" https://icanhazdadjoke.com/").decode('utf-8'))
    await ctx.send(dadjokes['joke'])

# <-----------SONGS-------------->
@client.command(aliases=["joinedith"])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command(aliases=["leaveedith"])
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command(aliases=["yt", "song", "music", "bajaa"])
async def youtube(ctx, *, song_name):
    for j in search(f"{song_name} song YouTube", lang="en", safe="off", num=1, stop=1, pause=2, verify_ssl=True):
        song_link = j






# <-------------GAME------------->
global gameSettings
gameSettings = {
    "isNACOn": False,
}

@client.command()
async def game(ctx, *, gameID):
    async def startNAC(ctx):
        gameSettings["isNACOn"] = True
        global positions
        positions = [
            # First Row
            [
                {
                    "position": "top-left",
                    "sign": "   ",
                    "isFilled": False,
                },
                {
                    "position": "top-center",
                    "sign": "   ",
                    "isFilled": False,
                },
                {
                    "position": "top-right",
                    "sign": "   ",
                    "isFilled": False,
                },
            ],
            # Second Row
            [
                {
                    "position": "mid-left",
                    "sign": "   ",
                    "isFilled": False,
                },
                {
                    "position": "mid-center",
                    "sign": "   ",
                    "isFilled": False,
                },
                {
                    "position": "mid-right",
                    "sign": "   ",
                    "isFilled": False,
                },
            ],
            # Third Row
            [
                {
                    "position": "bottom-left",
                    "sign": "   ",
                    "isFilled": False,
                },
                {
                    "position": "bottom-center",
                    "sign": "   ",
                    "isFilled": False,
                },
                {
                    "position": "bottom-right",
                    "sign": "   ",
                    "isFilled": False,
                },
            ]
        ]

        await ctx.send(f"**WELCOME TO TIC-TAC-TOE!** \nType \"_rules_\" in chat to hear the rules. \nWould you like to play versus a person or versus Edith?")

    games = {
        1: ["noughts and crosses", "noughtsandcrosses", "tic tac toe", "tic-tac-toe", "tictactoe", "zero katta", "zero-katta", "zerokatta"]
    }

    for i in games:
        if gameID in games[i]:
            await startNAC(ctx)
            break

@client.command(aliases=["vs"])
async def versus(ctx, *, competitor):
    if gameSettings["isNACOn"] == False:
        pass
    else:
        global NACEdith
        if competitor.title() == "Edith":
            NACEdith = True
        else:
            NACEdith = False

    if NACEdith == False:
        await ctx.send("Sorry, that feature is still in development. :(")
        gameSettings["isNACOn"] = False
    elif NACEdith == True:
        await ctx.send("LET THE GAMES BEGIN!")
        await ctx.send(makeGameBoardNAC())
        firstTurn = random.choice(["user", "Edith"])
        global isUserTurnNAC
        if firstTurn == "user":
            isUserTurnNAC = True
            await ctx.send("It's your turn.")
        elif firstTurn == "Edith":
            isUserTurnNAC = False
            await ctx.send("ISS MY TURN!!!")
            await EdithTurn(ctx)

# Rules for NAC
@client.command()
async def rules(ctx):
    if gameSettings["isNACOn"] == True:
        await ctx.send("If you don't know the rules to this game, then may the Lord help you. \nType \'fill\' and then a position, such as top-left, mid-right, bottom-center et cetera... \nIf you need more information, please go relive your childhood. Thank you. \n(Ooh also, if you wanna know why I\'m \'x\' and you\'re \'o\', that's because it\'s my game, honey...)")
    else:
        await ctx.send("No game has been started, though...")

@client.command()
async def fill(ctx, pos):
    if gameSettings["isNACOn"] == True and isUserTurnNAC == True:
        if fillUp(pos, "o") == "YAY":
            await ctx.send(makeGameBoardNAC())
            await checkVictory(ctx)
        else:
            await ctx.send("That position is invalid :/")

# Callable functions
def makeGameBoardNAC():
    # Making game board
    gameBoardNAC = f""
    for i in range(0, len(positions)):
        if i == 0:
            gameBoardNAC += "```"
        gameBoardNAC += "+---+---+---+ \n"
        for j in range(0, len(positions[i])):
            gameBoardNAC += f"|{positions[i][j]['sign']}"
            if j == 2:
                gameBoardNAC += f"| \n"
        if i == 2:
            gameBoardNAC += "+---+---+---+ \n```"
    return gameBoardNAC

def fillUp(pos, sign):
    toBeFilledUp = ""
    for i in positions:
        for j in i:
            if j['position'] == pos and j['isFilled'] == False:
                toBeFilledUp = j
            else:
                continue
    if toBeFilledUp == "":
        return "NAY"
    else:
        toBeFilledUp['sign'] = f" {sign} "
        toBeFilledUp['isFilled'] = True
        return "YAY"


async def EdithTurn(ctx): # ADD DIAGONAL FUNC.
    # Defining what happens during Edith's turn
    if gameSettings["isNACOn"] == True and NACEdith == True:
        if isUserTurnNAC == False:
            potentialMoves = []

            # Checks for potential moves in rows
            for i in positions:
                filledSpotsInRow = 0
                whichFilledSpots = []
                tempPos = []
                for j in i:
                    if j["isFilled"] == True:
                        filledSpotsInRow += 1
                        whichFilledSpots.append(j["sign"])
                    elif j["isFilled"] == False:
                        tempPos.append(j["position"])
                if filledSpotsInRow == 3:
                    # Full row be filled
                    continue
                elif filledSpotsInRow == 2:
                    # One spot left
                    if whichFilledSpots[0] == whichFilledSpots[1]:
                        # Blocking an enemy
                        if whichFilledSpots[0] == " o ":
                            potentialMoves.insert(0, (tempPos[0], "priority"))
                        # Making own trio
                        elif whichFilledSpots[0] == " x ":
                            potentialMoves.insert(0, (tempPos[0], "maximum priority"))
                    else:
                        # Differently filled two pos
                        potentialMoves.append((tempPos[0], "not a priority"))
                elif filledSpotsInRow == 1:
                    # Two spots left
                    for k in tempPos:
                        potentialMoves.append((k, "not a priority"))
                elif filledSpotsInRow == 0:
                    # Three empty sppots
                    for l in tempPos:
                        potentialMoves.append((l, "not a priority"))

            # Checks for potential moves in columns
            for i in range(0, len(positions[0])):
                filledSpotsInColumn = 0
                whichFilledSpots = []
                tempPos = []
                for j in range(0, len(positions)):
                    if positions[j][i]["isFilled"] == True:
                        filledSpotsInColumn += 1
                        whichFilledSpots.append(positions[j][i]["sign"])
                    elif positions[j][i]["isFilled"] == False:
                        tempPos.append(positions[j][i]["position"])
                if filledSpotsInColumn == 3:
                    # Full column be filled
                    continue
                elif filledSpotsInColumn == 2:
                    # One spot left
                    if whichFilledSpots[0] == whichFilledSpots[1]:
                        # Blocking an enemy
                        if whichFilledSpots[0] == " o ":
                            potentialMoves.insert(0, (tempPos[0], "priority"))
                        # Making own trio
                        elif whichFilledSpots[0] == " x ":
                            potentialMoves.insert(0, (tempPos[0], "maximum priority"))
                    else:
                        # Differently filled two pos
                        if not tempPos[0] in potentialMoves:
                            potentialMoves.append((tempPos[0], "not a priority"))
                elif filledSpotsInColumn == 1:
                    # Two spots left
                    for k in tempPos:
                        if not k in potentialMoves:
                            potentialMoves.append((k, "not a priority"))
                elif filledSpotsInColumn == 0:
                    # Three empty sppots
                    for l in tempPos:
                        if not l in potentialMoves:
                            potentialMoves.append((l, "not a priority"))

            # Checkss for potential moves in diagonals
            diagonalPos = [[], []]
            for i in range(0, len(positions)):
                diagonalPos[0].append(positions[i][i])
                diagonalPos[1].append(positions[i][2-i])
            for i in diagonalPos:
                filledSpotsInDiagonal = 0
                whichFilledSpots = []
                tempPos = []
                for j in i:
                    if j["isFilled"] == True:
                        filledSpotsInDiagonal += 1
                        whichFilledSpots.append(j["sign"])
                    elif j["isFilled"] == False:
                        tempPos.append(j["position"])
                if filledSpotsInDiagonal == 3:
                    # Full diagonal be filled
                    continue
                elif filledSpotsInDiagonal == 2:
                    # One spot left
                    if whichFilledSpots[0] == whichFilledSpots[1]:
                        # Blocking an enemy
                        if whichFilledSpots[0] == " o ":
                            potentialMoves.insert(0, (tempPos[0], "priority"))
                        # Making own trio
                        elif whichFilledSpots[0] == " x ":
                            potentialMoves.insert(0, (tempPos[0], "maximum priority"))
                    else:
                        # Differently filled two pos
                        potentialMoves.append((tempPos[0], "not a priority"))
                elif filledSpotsInDiagonal == 1:
                    # Two spots left
                    for k in tempPos:
                        potentialMoves.append((k, "not a priority"))
                elif filledSpotsInDiagonal == 0:
                    # Three empty sppots
                    for l in tempPos:
                        potentialMoves.append((l, "not a priority"))

            # Plays the actuaal moves from the potentialMoves list
            filledByEdith = False # IMPROVE THISSSSSS
            for i in potentialMoves:
                if i[1] == "maximum priority":
                    fillUp(i[0], "x")
                    filledByEdith = True
                    await ctx.send(f"**fill {i[0]}**")
                    break
            if filledByEdith == False:
                for i in potentialMoves:
                    if i[1] == "priority":
                        fillUp(i[0], "x")
                        filledByEdith = True
                        await ctx.send(f"**fill {i[0]}**")
                        break
            if filledByEdith == False:
                notAPriorityMoves = []
                for i in potentialMoves:
                    notAPriorityMoves.append(i[0])
                if positions[1][1]["isFilled"] == False:
                    notAPriorityPos = random.choice(["mid-center", random.choice(notAPriorityMoves)])
                else:
                    notAPriorityPos = random.choice(notAPriorityMoves)
                fillUp(notAPriorityPos, "x")
                filledByEdith = True
                await ctx.send(f"**fill {notAPriorityPos}**")
            await ctx.send(makeGameBoardNAC())
            await checkVictory(ctx)

    else:
        pass

async def checkVictory(ctx):
    victorious = [False, ""]

    # Checking all row trios
    for i in positions:
        rowVictory = []
        for j in i:
            rowVictory.append(j['sign'])
        if rowVictory[0] == rowVictory[1] and rowVictory[1] == rowVictory[2]:
            victorious[0] = True
            if i[0]['sign'] == " x ":
                victorious[1] = "Edith"
            elif i[0]['sign'] == " o ":
                victorious[1] = "Player"
            else:
                victorious[0] = False

    # Checking all coumn trios
    if victorious[0] == False:
        for i in range(0, len(positions[0])):
            colVictory = []
            for j in range(0, len(positions)):
                colVictory.append(positions[j][i]['sign'])
            if colVictory[0] == colVictory[1] and colVictory[1] == colVictory[2]:
                victorious[0] = True
                if positions[0][i]['sign'] == " x ":
                    victorious[1] = "Edith"
                elif positions[0][i]['sign'] == " o ":
                    victorious[1] = "Player"
                else:
                    victorious[0] = False

    # Checking both diagonal trios
    if victorious[0] == False:
        diagonalVictory = [[], []]
        for i in range(0, len(positions)):
            diagonalVictory[0].append(positions[i][i]["sign"])
            diagonalVictory[1].append(positions[i][2-i]["sign"])
        if diagonalVictory[0][0] == diagonalVictory[0][1] and diagonalVictory[0][1] == diagonalVictory[0][2]:
            victorious[0] = True
            if positions[0][0]['sign'] == " x ":
                victorious[1] = "Edith"
            elif positions[0][0]['sign'] == " o ":
                victorious[1] = "Player"
            else:
                victorious[0] = False
        if diagonalVictory[1][0] == diagonalVictory[1][1] and diagonalVictory[1][1] == diagonalVictory[1][2]:
            victorious[0] = True
            if positions[0][2]['sign'] == " x ":
                victorious[1] = "Edith"
            elif positions[0][2]['sign'] == " o ":
                victorious[1] = "Player"
            else:
                victorious[0] = False

    # Checking for a draw
    noOfSquaresFilled = 0
    for i in positions:
        for j in i:
            if j["isFilled"]:
                noOfSquaresFilled += 1
    if noOfSquaresFilled == 9:
        victorious[0] = True
        victorious[1] = "Draw"

    # Defines what eventually happens
    if victorious[0] == True:
        if victorious[1] == "Edith":
            await ctx.send("**BAHAHAHAHAHAHAHAHAHAHA I WON YOU PUNY MORTA-I meeeeeeaaaaaan, good game, kind person, good game.**")
        elif victorious[1] == "Player":
            await ctx.send("**Oh, y-you won, did you? I hate thi-I MEAN CONGRATULATIONS!**")
        elif victorious[1] == "Draw":
            await ctx.send("**AW COME ON, WHAT EVEN IS THIS?!**")
        gameSettings["isNACOn"] = False
    else:
        global isUserTurnNAC
        if isUserTurnNAC == True:
            isUserTurnNAC = False
            await EdithTurn(ctx)
        elif isUserTurnNAC == False:
            isUserTurnNAC = True




# <-------------GIFS------------->
media = {
    # Friends
    "nooo": r"https://media1.tenor.com/images/3e9e0a976d582002a4a02d690fbc12f9/tenor.gif",
    "bhap": r"https://media1.tenor.com/images/a69b9e8e2990a74f0fdfe067c0f47b67/tenor.gif",
    "thumbsup": r"https://media1.tenor.com/images/038e36f6bd6374e12084feb841a8d51f/tenor.gif",
    "shocked": r"https://media1.tenor.com/images/a5a7cc8535b02e60462214be2f5a3a67/tenor.gif",
    "wisdomous": r"https://media1.tenor.com/images/883d3cdb1d0d95b19d4f8b0411941143/tenor.gif",
    "middle-finger": r"https://media.tenor.com/images/b92364f634c5375c1d1cb5d0ea0d4979/tenor.gif",
    # Brooklyn Nine-Nine
    "noice": r"https://media.tenor.com/images/098e4852dfdc41991add5983e9262a92/tenor.gif",
    "cool": r"https://i.pinimg.com/originals/4f/db/37/4fdb373ebe3e8cec0f6ad5a4345ad011.gif",
    "toit": r"https://basicallylaurenslifetravel.files.wordpress.com/2019/04/tumblr_p0gl7i7p5i1qjvfkco2_500.gif",
    # How I Met Your Mother
    "woo": r"https://media1.tenor.com/images/b15404e06ff41a0cbed2153398b1a8ab/tenor.gif",
    "kill": r"https://media1.tenor.com/images/61ae345e267e9ce138708d8058996bf4/tenor.gif",
    # Memes
    "maybe": r"https://media.tenor.com/images/6bdd650af717980d5d898d4fd0b8ad52/tenor.gif",
    "nikal": r"https://media.tenor.com/images/7e6a7b73faa414e321811e0ecb34519e/tenor.gif",
    # Misc
    "excellent": r"https://media1.tenor.com/images/9e3409f358c9cec06061c1ec76d86d47/tenor.gif?itemid=4076853",
}

@client.command(aliases=["listofgifs", "gif-list"])
async def gifList(ctx):
    list_of_gifs = ""
    for i in media:
        list_of_gifs += "\n"
        list_of_gifs += f"> _{i}_"
    await ctx.send(f"This is a list of all the GIFs an extrordinary bot like yours truly has to offer: {list_of_gifs}")
# Friends
@client.command(aliases=["noooo", "nooooo"])
async def nooo(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(media['nooo']) as resp:
            if not resp.status == 200: # HTTP response status code 200 means okay
                await ctx.send("Could not download file :(")
            await ctx.send(file=discord.File(io.BytesIO(await resp.read()), "nooo.gif"))
@client.command()
async def bhap(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(media['bhap']) as resp:
            if not resp.status == 200: # HTTP response status code 200 means okay
                await ctx.send("Could not download file :(")
            await ctx.send(file=discord.File(io.BytesIO(await resp.read()), "bhap.gif"))
@client.command(aliases=["goodjob", "greatjob", "badiya"])
async def thumbsup(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(media['thumbsup']) as resp:
            if not resp.status == 200: # HTTP response status code 200 means okay
                await ctx.send("Could not download file :(")
            await ctx.send(file=discord.File(io.BytesIO(await resp.read()), "thumbsup.gif"))
@client.command(aliases=["gasp"])
async def shocked(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(media['shocked']) as resp:
            if not resp.status == 200: # HTTP response status code 200 means okay
                await ctx.send("Could not download file :(")
            await ctx.send(file=discord.File(io.BytesIO(await resp.read()), "shocked.gif"))
@client.command(aliases=["wise", "wisdom", "smart"])
async def wisdomous(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(media['wisdomous']) as resp:
            if not resp.status == 200: # HTTP response status code 200 means okay
                await ctx.send("Could not download file :(")
            await ctx.send(file=discord.File(io.BytesIO(await resp.read()), "wisdomous.gif"))
@client.command(aliases=["middle-finger", ":middle_finger:"])
async def middleFinger(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(media['middle-finger']) as resp:
            if not resp.status == 200: # HTTP response status code 200 means okay
                await ctx.send("Could not download file :(")
            await ctx.send(file=discord.File(io.BytesIO(await resp.read()), "middle-finger.gif"))
# Brooklyn Nine-Nine
@client.command(aliases=["nice"])
async def noice(ctx, *args):
    if len(args) == 2:
        if args[0].lower() == "one" or args[0].lower() == "one,":
            if args[1].title() == "Edith":
                await ctx.send('Thank you')
            else:
                async with aiohttp.ClientSession() as session:
                    async with session.get(media['noice']) as resp:
                        if not resp.status == 200: # HTTP response status code 200 means okay
                            await ctx.send("Could not download file :(")
                        await ctx.send(file=discord.File(io.BytesIO(await resp.read()), "noice.gif"))
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(media['noice']) as resp:
                    if not resp.status == 200: # HTTP response status code 200 means okay
                        await ctx.send("Could not download file :(")
                    await ctx.send(file=discord.File(io.BytesIO(await resp.read()), "noice.gif"))
    else:
        async with aiohttp.ClientSession() as session:
            async with session.get(media['noice']) as resp:
                if not resp.status == 200: # HTTP response status code 200 means okay
                    await ctx.send("Could not download file :(")
                await ctx.send(file=discord.File(io.BytesIO(await resp.read()), "noice.gif"))
@client.command(aliases=["coolcoolcool"])
async def cool(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(media['cool']) as resp:
            if not resp.status == 200: # HTTP response status code 200 means okay
                await ctx.send("Could not download file :(")
            await ctx.send(file=discord.File(io.BytesIO(await resp.read()), "cool.gif"))
@client.command()
async def toit(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(media['toit']) as resp:
            if not resp.status == 200: # HTTP response status code 200 means okay
                await ctx.send(f"Could not download file :(")
            await ctx.send(file=discord.File(io.BytesIO(await resp.read()), "toit.gif"))
# How I Met Your Mother
@client.command()
async def woo(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(media['woo']) as resp:
            if not resp.status == 200: # HTTP response status code 200 means okay
                await ctx.send("Could not download file :(")
            await ctx.send(file=discord.File(io.BytesIO(await resp.read()), "woo.gif"))
@client.command(aliases=["killme", "killmenow", "kmn"])
async def kill(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(media['kill']) as resp:
            if not resp.status == 200: # HTTP response status code 200 means okay
                await ctx.send("Could not download file :(")
            await ctx.send(file=discord.File(io.BytesIO(await resp.read()), "kill.gif"))
# Memes
@client.command(aliases=["maybeee", "mayyybeee"])
async def mayyybe(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(media['maybe']) as resp:
            if not resp.status == 200: # HTTP response status code 200 means okay
                await ctx.send("Could not download file :(")
            await ctx.send(file=discord.File(io.BytesIO(await resp.read()), "maybe.gif"))
@client.command(aliases=["nikallawde", "nikallavde", "pehlifursatmeinnikal"])
async def nikal(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(media['nikal']) as resp:
            if not resp.status == 200: # HTTP response status code 200 means okay
                await ctx.send("Could not download file :(")
            await ctx.send(file=discord.File(io.BytesIO(await resp.read()), "nikal.gif"))
# Misc.
@client.command(aliases=["ahhhhh"])
async def excellent(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(media['excellent']) as resp:
            if not resp.status == 200: # HTTP response status code 200 means okay
                await ctx.send("Could not download file :(")
            await ctx.send(file=discord.File(io.BytesIO(await resp.read()), "excellent.gif"))
