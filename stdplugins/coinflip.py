"""CoinFlip for @UniBorg
Syntax: .coinflip [optional_choice]"""
from telethon import events
import random, re
from uniborg.util import admin_cmd


@borg.on(admin_cmd("tanga ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    r = random.randint(1, 100)
    input_str = event.pattern_match.group(1)
    if input_str:
        input_str = input_str.lower()
    if r % 2 == 1:
        if input_str == "oldi":
            await event.edit("Tanganing: **Oldi tomoni**. \n Siz to'g'ri topdingiz.")
        elif input_str == "tails":
            await event.edit("Tanganing: **Oldi tomoni**. \n Noto'g'ri topdingiz ...")
        else:
            await event.edit("Tanganing: **Oldi tomoni**.")
    elif r % 2 == 0:
        if input_str == "orqa":
            await event.edit("Tanganing: **Orqa tomoni**. \n Siz to'g'ri topdingiz.")
        elif input_str == "heads":
            await event.edit("Tanganing: **Orqa tomoni**. \n Noto'g'ri topdingiz ...")
        else:
            await event.edit("Tanganing: **Orqa tomoni**.")
    else:
        await event.edit("¯\_(ツ)_/¯")
