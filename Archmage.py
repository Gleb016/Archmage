import discord
from discord.ext import commands
from discord.ui import Button
import logging
import sqlite3


con = sqlite3.connect("Explanation")
cur = con.cursor()

intents = discord.Intents.default()
intents.members = True

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

TOKEN = "MTA5OTY2Nzk3MjUzNDA0Njc1MA.G5qtn6.TjBfo3suqhD2663jB5okWvR_OCEGfaaNWi6fuU"


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
        self.Term = False

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
        self.message = message
        if message.author == self.user:
            return
        if self.Term:
            if len(self.term()) == 2:
                a, b = self.term()
                await message.channel.send(a)
                await message.channel.send(b)
            else:
                await message.channel.send(self.term())
        else:
            if "приветствую" in message.content.lower():
                await message.channel.send(self.told())
            else:
                await message.channel.send("Спасибо за сообщение")

            if 'поведайте' or 'объясните' in self.message:
                self.told()

    def told(self):
        message = self.message.content.lower()
        if 'term' in message or 'terms' in message \
                or 'термин' in message or 'термины' in message:
            self.Term = True
            return f'Приветствую тебя неофит {str(self.message.author)[:-5]}, что именно тебя интересует?'
        elif 'rule' in self.message or 'rules' in self.message \
                or 'правила' in self.message or 'правило' in self.message \
                or 'механику' in self.message or 'механики' in self.message:
                pass

    def term(self):
        message = self.message.content.lower()
        result = cur.execute(f"""Select Name,Explanation From Term
                        Where name LIKE "{message.upper()}%" """).fetchall()

        print(result)
        if len(result) == 1:
            self.Term = False
            return f'**{result[0][0]}**', f'{result[0][1]}'
        else:
            result = cur.execute(f"""Select Name,Explanation From Term
                        Where name LIKE "{message.upper()}%" """).fetchall()
            if len(result) != 0:
                return f"Может ты имел в ввиду {', '.join([i[0] for i in result])}"
            else:
                return 'прости неофит не могу понят о чем ты толкуешь'



Bot = Archmage()

Bot.run(TOKEN)