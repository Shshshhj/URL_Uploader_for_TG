from pyrogram import Client, Message, Filters
from bot import COMMAND
from bot.handlers import leech_handler

@Client.on_message(Filters.private & Filters.command(COMMAND.LEECH))
async def func(client, update):
  if (" " in update.text) and (update.reply_to_message is not None):
    cmd, file_name = update.text.split(" ", 1)
  message = update.reply_to_message
  message.text = "/" + COMMAND.LEECH + " " + message.text
  return await leech_handler.func(client, message)
