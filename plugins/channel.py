
# Don't Remove Credit @VJ_Bots

from pyrogram import Client, filters
from info import CHANNELS
from database.ia_filterdb import save_file
import logging

logger = logging.getLogger(__name__)

media_filter = filters.document | filters.video

@Client.on_message(filters.chat(CHANNELS) & media_filter)
async def media_handler(bot, message):
    try:
        media = getattr(message, message.media.value, None)

        if not media:
            logger.warning("No media found in message %s", message.id)
            return

        logger.info(
            "Channel media received: chat_id=%s, message_id=%s",
            message.chat.id,
            message.id
        )

        media.caption = message.caption
        result = await save_file(media)
        logger.info("MongoDB save result: %s", result)

    except Exception:
        logger.exception("Channel media save failed")
