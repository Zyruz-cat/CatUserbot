
import asyncio
import random
import re
import time
from random import choice, randint
from collections import deque
from telethon import events
import requests

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName


from userbot import CMD_HELP
from userbot.utils import register, admin_cmd


# ================= CONSTANT =================


GAMBAR_TITIT = """
🍆🍆
🍆🍆🍆
  🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
          🍆🍆🍆
      🍆🍆🍆🍆
 🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆       🍆🍆
"""

# ===========================================

@borg.on(admin_cmd(pattern=r"hf$"))
async def facepalm(e):
    """ Facepalm  🤦‍♂ """
    await e.edit("🤦‍♂")

@borg.on(admin_cmd(pattern=r"corona$"))
async def iqless(e):
    await e.edit("Antivirus scan was completed \n⚠️ Warning! This  donkey has Corona Virus")


@borg.on(admin_cmd(pattern=r"ggl (.*)"))
async def let_me_google_that_for_you(lmgtfy_q):
    textx = await lmgtfy_q.get_reply_message()
    qry = lmgtfy_q.pattern_match.group(1)
    if qry:
        query = str(qry)
    elif textx:
        query = textx
        query = query.message
    query_encoded = query.replace(" ", "+")
    lfy_url = f"http://lmgtfy.com/?s=g&iie=1&q={query_encoded}"
    payload = {'format': 'json', 'url': lfy_url}
    r = requests.get('http://is.gd/create.php', params=payload)
    await lmgtfy_q.edit(f"Tap this blue, help yourself.\
    \n[{query}]({r.json()['shorturl']})")


@register(outgoing=True, pattern="^.fail$")
async def fail(e):
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ `" 
                     "`\n████▌▄▌▄▐▐▌█████ `"    
                     "`\n████▌▄▌▄▐▐▌▀████ `"       
                     "`\n▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀ `")    


@register(outgoing=True, pattern="^.lol$")
async def lol(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n╱┏┓╱╱╱╭━━━╮┏┓╱╱╱╱ `" 
                     "`\n╱┃┃╱╱╱┃╭━╮┃┃┃╱╱╱╱ `"       
                     "`\n╱┃┗━━┓┃╰━╯┃┃┗━━┓╱ `" 
                     "`\n╱┗━━━┛╰━━━╯┗━━━┛╱ `") 
 
 
                                                                                   
@register(outgoing=True, pattern="^.lool$")
async def lool(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n╭╭━━━╮╮┈┈┈┈┈┈┈┈┈┈\n┈┃╭━━╯┈┈┈┈▕╲▂▂╱▏┈\n┈┃┃╱▔▔▔▔▔▔▔▏╱▋▋╮┈`"
                     "`\n┈┃╰▏┃╱╭╮┃╱╱▏╱╱▆┃┈\n┈╰━▏┗━╰╯┗━╱╱╱╰┻┫┈\n┈┈┈▏┏┳━━━━▏┏┳━━╯┈`"
                     "`\n┈┈┈▏┃┃┈┈┈┈▏┃┃┈┈┈┈ `")
                     



@register(outgoing=True, pattern="^.nih$")
async def nih(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n(\_/)`"
                     "`\n(•_•)`"
                     "`\n >🌹 *`"
                     "`\n                    `"
                     "`\n(\_/)`"
                     "`\n(•_•)`"
                     "`\n🌹<\ *`")


@register(outgoing=True, pattern="^.hoi$")  
async def gtfo(e):
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n█████████`" 
                     "`\n█▄█████▄█`"    
                     "`\n█▼▼▼▼▼`"       
                     "`\n█  Hello Man`"
                     "`\n█▲▲▲▲▲`"
                     "`\n█████████`"
                    "`\n ██   ██`")               


@register(outgoing=True, pattern="^.ml(?: |$)(.*)")
async def gtfo(e):
   message = e.pattern_match.group(1)
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n█████████`" 
                     "`\n█▄█████▄█`"    
                     "`\n█▼▼▼▼▼`"       
                     f"`\n█  {message}`"
                     "`\n█▲▲▲▲▲`"
                     "`\n█████████`"
                    "`\n ██   ██`")               


@register(outgoing=True, pattern="^.taco$")  
async def taco(e):
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("\n{\__/}"
                     "\n(●_●)"
                     "\n( >🌮 Want a taco?")


@register(outgoing=True, pattern="^.paw$")  
async def paw(e):
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`(=ↀωↀ=)")


@register(outgoing=True, pattern="^.tf$")  
async def tf(e):
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(̿▀̿ ̿Ĺ̯̿̿▀̿ ̿)̄  ")  
      

@register(outgoing=True, pattern="^.gay$")            
async def gey(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n┈┈┈╭━━━━━╮┈┈┈┈┈\n┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈`"
                     "`\n┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n┈┈╭┻┊┊╰━┻━╮┈┈┈┈`"
                     "`\n┈┈╰┳┊╭━━━┳╯┈┈┈┈\n┈┈┈┃┊┃╰━━┫┈U GAY`"
                    "\n┈┈┈┈┈┈┏━┓┈┈┈┈┈┈")    


@register(outgoing=True, pattern="^.bot$")
async def bot(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("` \n   ╲╲╭━━━━╮ \n╭╮┃▆┈┈▆┃╭╮ \n┃╰┫▽▽▽┣╯┃ \n╰━┫△△△┣━╯`"
                     "`\n╲╲┃┈┈┈┈┃  \n╲╲┃┈┏┓┈┃ `")


@register(outgoing=True, pattern="^.hai$")
async def hey(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("\n┈┈┈╱▔▔▔▔╲┈╭━━━━━\n┈┈▕▂▂▂▂▂▂▏┃HELLO!┊😀`"
                     "`\n┈┈▕▔▇▔▔┳▔▏╰┳╮HELLO!┊\n┈┈▕╭━╰╯━╮▏━╯╰━━━\n╱▔▔▏▅▅▅▅▕▔▔╲┈┈┈┈`"
                     "`\n▏┈┈╲▂▂▂▂╱┈┈┈▏┈┈┈`")


@register(outgoing=True, pattern="^.nou$")
async def nou(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`\n┈╭╮╭╮\n┈┃┃┃┃\n╭┻┗┻┗╮`"
                     "`\n┃┈▋┈▋┃\n┃┈╭▋━╮━╮\n┃┈┈╭╰╯╰╯╮`"
                     "`\n┫┈┈  NoU\n┃┈╰╰━━━━╯`"
                     "`\n┗━━┻━┛`")



@register(outgoing=True, pattern="^.mf$")  
async def gtfo(e):
   if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(
"\n......................................../´¯/) "
"\n......................................,/¯../ "
"\n...................................../..../ "
"\n..................................../´.¯/"
"\n..................................../´¯/"
"\n..................................,/¯../ "
"\n................................../..../ "
"\n................................./´¯./"
"\n................................/´¯./"
"\n..............................,/¯../ "
"\n............................./..../ "
"\n............................/´¯/"
"\n........................../´¯./"
"\n........................,/¯../ "
"\n......................./..../ "
"\n....................../´¯/"
"\n....................,/¯../ "
"\n.................../..../ "
"\n............./´¯/'...'/´¯¯`·¸ "
"\n........../'/.../..../......./¨¯\ "
"\n........('(...´...´.... ¯~/'...') "
"\n.........\.................'...../ "
"\n..........''...\.......... _.·´ "
"\n............\..............( "
"\n..............\.............\...")



@register(outgoing=True, pattern="^.sayhi$")
async def shalom(e):
    await e.edit(
        "\n💛💛💛💛💛💛💛💛💛"
        "\n💛🔷🔷🔷🔷🔷🔷🔷💛"
        "\n💛💛💛💛🔷💛💛💛💛"
        "\n💛💛💛💛🔷💛💛💛💛"
        "\n💛💛💛💛🔷💛💛💛💛"
        "\n💛🔷🔷🔷🔷️🔷🔷🔷💛"
        "\n💛💛💛💛💛💛💛💛💛"
        "\n💛💛💛💛💛💛💛💛💛"
        "\n💛🔷💛💛️💛💛💛🔷💛"
        "\n💛🔷🔷🔷🔷🔷🔷🔷💛"
        "\n💛🔷🔷🔷🔷🔷🔷️🔷💛"
        "\n💛🔷💛💛💛💛️💛🔷💛"
        "\n💛💛💛💛💛💛💛💛💛")

@register(outgoing=True, pattern=r"^\.(?:penis|dick)\s?(.)?")
async def emoji_penis(e):
    emoji = e.pattern_match.group(1)
    titid = GAMBAR_TITIT
    if emoji:
        titid = titid.replace('🍆', emoji)
    await e.edit(titid)


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 100)

    input_str = event.pattern_match.group(1)

    if input_str == "muth":

        await event.edit(input_str)

        animation_chars = [

            "8✊️===D",

            "8=✊️==D",

            "8==✊️=D",

            "8===✊️D",

            "8==✊️=D",

            "8=✊️==D",

            "8✊️===D",

            "8===✊️D💦",

            "8==✊️=D💦💦",

            "8=✊️==D💦💦💦"

        ]

        for i in animation_ttl:
        
            await asyncio.sleep(animation_interval)
        
            await event.edit(animation_chars[i % 8])
