import pyrogram
from pyrogram import Client, Message, filters
from bot import COMMAND
from bot.handlers import leech_handler

@Client.on_message(Filters.private & pyrogram.filters.command(["leech"]))
async def func(client, update):
  cmd, file_name = update.text.split(" ", 1)
  message = update.reply_to_message
  message.text = "/" + COMMAND.LEECH + " " + message.text
  return await leech_handler.func(client, message)
