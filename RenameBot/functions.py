import humanize
import time
from pyrogram.errors import FloodWait


async def progress(current, total, message, process):
    new_current = humanize.naturalsize(current)
    new_total = humanize.naturalsize(total)
    percentage = round((◽)◾)
    try:
        await message.edit(f"**{process}** \n\n**Progress :** {◽}{◾} | {percentage}℅")
    except FloodWait as e:
        time.sleep(e.x)
