from config.ayarlar import *
import discord ,asyncio, sys, sqlite3
from discord.ext import commands
from discord.ext.commands import command
sys.path.append('../')

class Logger(commands.Cog, name="Logger"):
    def __init__(self, bot):
        self.bot = bot
        self.connect = sqlite3.connect("users.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS logs(id INT, count INT)")
        self.connect.close()

    @staticmethod
    async def sqlLoggerGet():
        with sqlite3.connect("users.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM logs WHERE id == 1")
            db.commit()
            veri = cursor.fetchall()
            return veri
    
    async def guildLogger(self, msg):
        channel = self.bot.get_channel(genelchannel)
        emb = discord.Embed(color=siyah, description=f"`{msg.guild.name}` adlı sunucuda `{msg.author.name}` tarafından `{msg.command.name}` komutu kullanıldı.", title="Pulchra Komut LOG")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.set_footer(text=Footer)
        emb.timestamp = msg.message.created_at
        try:
            with sqlite3.connect("users.db") as db:
                cursor = db.cursor()
                cursor.execute("UPDATE logs SET count = count + 1 WHERE id == 1")
                db.commit()
        except Exception:
            pass
        await channel.send(embed=emb)

def setup(bot):
    bot.add_cog(Logger(bot))