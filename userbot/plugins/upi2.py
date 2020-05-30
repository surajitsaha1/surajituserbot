"""command - .upi2"""

from telethon import events
import asyncio


from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern=f"upi2", allow_sudo=True))
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.4

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "upi2":

        await event.edit(input_str)

        animation_chars = [
        "`surajit`",
        "`111`",
        "`@paytm`",
        "`surajit111@paytm`"
        ]
        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])
