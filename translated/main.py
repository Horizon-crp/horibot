from nextcord.ext import commands;
from nextcord import Intents;
bot = commands.Bot(command_prefix=['?'], intents=Intents.all(), help_command=None);
from os import listdir, system, environ;
import asyncio;
async def load_cogs(Folder: str) -> None:
  tasks: list = [];
  for fn in listdir(Folder):
    if fn.endswith('.py'): tasks.append(asyncio.create_task(load_ext(f'cogs.{fn[:-3]}')));
  for i in tasks: await i;
async def load_ext(ext: str):
  global bot;
  bot.load_extension(ext);
asyncio.run(load_cogs('cogs'));
bot.run(environ['token']);
