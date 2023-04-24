import discord
from Rule import game_beginning, starting_phase
from discord.ext import commands
from discord.ui import Button, View
import logging
import sqlite3
import random


con = sqlite3.connect("Explanation")
cur = con.cursor()

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
    async def first_player(self, message):
        await message.channel.send(random.choice(message.content.split('; ')))

    async def cards_pack(self, message):
        await message.channel.send(random.choice(['черные', 'белые', 'синие', 'красные', 'зеленые']))

    async def on_message(self, message):
        self.channel = message.channel
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
                await self.told(message)
            else:
                await message.channel.send("Спасибо за сообщение")

            if 'поведайте' or 'объясните' in self.message:
                await self.told(message)


    async def told(self, message):
        message_txt = str(message.content.lower())
        if 'term' in message_txt or 'terms' in message_txt \
                or 'термин' in message_txt or 'термины' in message_txt:
            self.Term = True
            await message.channel.send(f'Приветствую тебя неофит {str(self.message.author)[:-5]},'
                                       f' что именно тебя интересует?')
        elif 'rule' in message_txt or 'rules' in message_txt \
                or 'правила' in message_txt or 'правило' in message_txt \
                or 'механику' in message_txt or 'механики' in message_txt:
            await self.rule(message)
    async def rule(self, message):
         ctx = await self.get_context(message)
         async def move_1(interaction):
            await interaction.response.send_message(game_beginning())
         async def move_2(interaction):
            await interaction.response.send_message(starting_phase())

         buttun_1 = Button(label='Начало игры', style=discord.ButtonStyle.gray)
         buttun_2 = Button(label='Начало хода', style=discord.ButtonStyle.green)
         buttun_3 = Button(label='Начало игры', style=discord.ButtonStyle.red)
         buttun_4 = Button(label='Начало игры', style=discord.ButtonStyle.green)
         buttun_5 = Button(label='Видео игрок по MTG', url='https://www.youtube.com/watch?v=kXOD7S8F48c')
         view = View()
         buttun_1.callback = move_1
         buttun_2.callback = move_2

         view.add_item(buttun_1)
         view.add_item(buttun_2)
         view.add_item(buttun_3)
         view.add_item(buttun_4)
         view.add_item(buttun_5)
         await ctx.send(view=view)




    def term(self):
        message = self.message.content.lower()
        result = cur.execute(f"""Select Name,Explanation From Term
                        Where name LIKE "{message.upper()}%" """).fetchall()


        if len(result) == 1:
            self.Term = False
            return f'**{result[0][0]}**', f'{result[0][1]}'
        else:
            result = cur.execute(f"""Select Name,Explanation From Term
                        Where name LIKE "{message.upper()}%" """).fetchall()
            if len(result) != 0:
                return f"Может ты имел в ввиду {', '.join([i[0] for i in result])}"
            else:
                return 'прости неофит не могу понять, о чем ты толкуешь'




Bot = Archmage()

Bot.run(TOKEN)
