"""command - .wallet2"""

from telethon import events
import asyncio


from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern=f"wallet2", allow_sudo=True))
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.2

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "wallet2":

        await event.edit(input_str)

        animation_chars = [
        "`9`",
        "`8`",
        "`3`",
        "`2`",
        "`5`",
        "`8`",
        "`5`",
        "`2`",
        "`5`",
        "`3`",
        "`9832585253`"
        ]
        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])
            
#Modified by @surajit1
