# Module by @DeBotMod
from telethon import events
from userbot import client

from time import perf_counter

info = {'category': 'fun', 'pattern': '.ping', 'description': ' Узнай свой пинг!'}


@client.on(events.NewMessage(outgoing=True, pattern=".ping"))
async def ping_commands(event):
    start = perf_counter()
    await event.edit('⌲')
    end = perf_counter()
    await event.edit(f'⌲ Пинг: {round(end - start, 3)}сек.')