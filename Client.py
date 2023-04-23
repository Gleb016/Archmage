import discord

class BotClient(discord.Client):
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