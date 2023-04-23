import discord
from discord.ext import commands
from discord.ui import Button
import logging
from Client import BotClient

intents = discord.Intents.default()
intents.members = True

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

TOKEN = ""


class MyView(discord.ui.View):
    @discord.ui.button(label="Button 1", row=0, style=discord.ButtonStyle.primary)
    async def first_button_callback(self, button, interaction):
        await interaction.response.send_message("You pressed me!")

    @discord.ui.button(label="Button 2", row=1, style=discord.ButtonStyle.primary)
    async def second_button_callback(self, button, interaction):
        await interaction.response.send_message("You pressed me!")


class Archmage(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='>>>', intents=intents)

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            print(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Приветствую тебя неофит {member.name}!'
        )

    async def on_message(self, message):
        if message.author == self.user:
            return
        else:
            await message.channel.send("Спасибо за сообщение")


Bot = Archmage()

Bot.run(TOKEN)