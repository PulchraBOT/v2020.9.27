import discord, sys, asyncio, sqlite3, random
from discord.ext import commands
from discord.ext.commands import command
sys.path.append('../')
from config.ayarlar import *
from log.logger import Logger

class Economy(commands.Cog, name="Ekonomi"):
    def __init__(self, bot):
        self.bot = bot
        self.connect = sqlite3.connect("users.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users(id INT, money INT)")
        self.connect.close()

    @staticmethod
    async def negativeSentences():
        sentences = ['sana RKO çekti', 
        'seninle top gibi oynadı', 
        'sana başını alırsın dedi', 
        'annenden iste dedi', 
        'git camide dilen dedi', 
        'pışık yağlı kaşık dedi',
        'sana batista bomb çekip evereste yolladı',
        'sana 619 çekti',
        'seni tek yumrukla yere serdi',
        'seni çalım manyagı yaptı',
        'seni outplay etti mal oldun amk',
        'seni polise ihbar etti bi tık boku yedin',
        'seni uzaya yolladı',
        'seni parasıyla tokatladı ve başını verdi',
        'kafana yam fırlattı',
        'seni kafes dövüşünde patates etti',
        'sana orta parmak çekti',
        'seni sürgün etti',
        'sana koronasın diyerek para vermedi',
        'seni engizisyon mahkemesine yolladı',
        'sana BRUH dedi',
        'kafana C4 fırlattı ganaya savruldun',
        'aç kardeşim aras kargo dedi',
        'adamlarını toplayıp sana grup yaptılar geçmiş olsun agam',
        'sana ankarada gemiyle çarptı diyarbakıra savruldun',
        'sana uçakla çarptı',
        'drift yaparken yanlışlıkla sana kaydı',
        'ile uçakdan paraşütle atladınız ama paraşütün yokmuş aga',
        'ile yüzerken balina çarptı',
        'kişisini soymaya karar verdin ama koruması kafana bozuka attı',
        'sana EZBIRÇİME dedi',
        'ile gezerken merdivenlerden yuvarlandın'
        ]
        sentence = random.choice(sentences)
        return sentence

    @staticmethod
    async def begGenarator():
        number = random.randint(30,300)
        return number

    @staticmethod
    async def historyName():
        mans = ['Bekir', 'Ahmet', 'Berkecan', 'Umut', 'Burhan', 'İlhan', 'Furkan', 'Mert', 'Hamza' 'Yakup', 'Kadir', 'Erdem', 'Cem', 'Veysel', 'Cüneyt', 'Muzaffer', 'Aptülrezzak', 'Polat']
        man = random.choice(mans)
        return man

    @staticmethod    
    async def people():
        peoples = ['**Elon Musk**', 
        '**Alicem**', 
        '**Erdem**',
        '**Pulchra**', 
        '**Ali Ağaoğlu**',
        '**Barış Özcan**', 
        '**Barış Bra**', 
        '**Berat Albayrak**', 
        '**Recep Tayyip Erdoğan**', 
        '**Orospu Çocuğu**', 
        '**Kemal Kılıçdaroğlu**',
        '**Cübbeli Ahmet Hoca**', 
        '**Jonny Sins**', 
        '**Allah**', 
        '**HZ.Muhammed**', 
        '**Kuş Adam**', 
        '**PornHub**', 
        '**Brazzers**',
        '**Jesus**',
        '**Tonguç Akademi**',
        '**Devlet Bahçeli**',
        '**Ricardo Milos**',
        '**Thomas Ve Arkadaşları**',
        '**Garip Kont**',
        '**Stüdyo King**',
        '**Tekerlekli Sandalye İle Yüzen Engelli Japon Balığı**',
        '**3T**',
        '**Ege Fitness**',
        '**Acun Ilıcalı**',
        '**Omar Souleyman**',
        '**DJ Ercik**',
        '**Şah Batur**',
        '**Aleyna Tilki**',
        '**Donald Trump**',
        '**Efe Aydal**',
        '**Gorilla**',
        '**Umut**',
        '**Köksal Baba**',
        '**Kim Busik**',
        '**George Floyd**',
        '**Niggalar**',
        '**Doktor Ali Vefa**',
        '**Duygu Özaslan**',
        '**DJ Dikkat**', 
        '**Aykut Elmas**']
        people = random.choice(peoples)
        return people

    @staticmethod
    async def accountCreate(msg, user):
        with sqlite3.connect("users.db") as db:
            if user.bot:
                return
            cursor = db.cursor()
            cursor.execute(f"INSERT INTO users VALUES({user.id},31)")
            db.commit()
            emb = discord.Embed(color=msg.guild.me.color, description=f"Dostum seni yeni gördüm ve senin için yeni bir hesap oluşturdum.\n**Yüklenen Bakiye:** `31₺`", title=f"Hoşgeldin {user.name}")
            emb.set_author(name=user.name, icon_url=user.avatar_url)
            emb.set_footer(text=Footer)
            await msg.send(embed=emb)

    @staticmethod
    async def sqlGet(user):
        with sqlite3.connect("users.db") as db:
            cursor = db.cursor()
            cursor.execute(f"SELECT * FROM users WHERE id == {user.id}")
            db.commit()
            veri = cursor.fetchall()
            return veri

    @staticmethod
    async def sqlUpdate(user, value):
        with sqlite3.connect("users.db") as db:
            cursor = db.cursor()
            cursor.execute(f"UPDATE users SET money = {value} WHERE id == {user.id}")
            db.commit()
            return

    @command(aliases=['cüzdan', 'balance', 'bal'])
    async def bakiye(self, msg, member: discord.Member=None):
        await Logger.guildLogger(self, msg)
        if member is None:
            user = msg.author
            veri = await self.sqlGet(user)
            if veri:
                emb = discord.Embed(color=msg.guild.me.color, title=f"**Bakiye:** `{veri[0][1]:,d}₺`")
                emb.set_author(name=user.name, icon_url=user.avatar_url)
                emb.set_footer(text=Footer)
                await msg.send(embed=emb)     
            else:
                await self.accountCreate(msg, user)
        elif member is not None:
            user = member
            veri = await self.sqlGet(user)
            if veri:
                emb = discord.Embed(color=msg.guild.me.color, title=f"**Bakiye:** `{veri[0][1]:,d}₺`")
                emb.set_author(name=user.name, icon_url=user.avatar_url)
                emb.set_footer(text=Footer)
                await msg.send(embed=emb)     
            else:
                await self.accountCreate(msg, user)

    @command(aliases=['beg'])
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def dilen(self, msg):
        await Logger.guildLogger(self, msg)
        with sqlite3.connect("users.db") as db:
            user = msg.author
            veri = await self.sqlGet(user)
            if veri:
                balance = veri[0][1]
                result = random.randint(0,3)
                people = await self.people()
                if result == 2 or result == 3:
                    result2 = random.randint(1,30)
                    num = await self.begGenarator()
                    if result2 == 5:
                        balance -= num
                        await self.sqlUpdate(user,balance)
                        emb = discord.Embed(color=msg.guild.me.color, title=f"**Papa** sana cenneten arsa sattı `-{num}₺` kaybettin")
                        emb.set_author(name=user.name, icon_url=user.avatar_url)
                        emb.set_footer(text=Footer)
                        await msg.send(embed=emb)
                    elif result2 == 10:
                        balance -= num
                        await self.sqlUpdate(user,balance)
                        emb = discord.Embed(color=msg.guild.me.color, title=f"Dilenirken zabıtaya yakalandın `-{num}₺` kaybettin")
                        emb.set_author(name=user.name, icon_url=user.avatar_url)
                        emb.set_footer(text=Footer)
                        await msg.send(embed=emb)
                    elif result2 == 15:
                        adam = await self.historyName()
                        emb = discord.Embed(color=msg.guild.me.color, title=f"Dilenirken {adam} adında biri sana yasadışı bir iş teklif etti kabul edicekmisin ?\n __E = Evet, H = Hayır__")
                        emb.set_author(name=user.name, icon_url=user.avatar_url)
                        emb.set_footer(text=Footer)
                        soruemb = await msg.send(embed=emb)
                        await soruemb.add_reaction("🇪")
                        await soruemb.add_reaction("🇭")

                        def check(react, user):
                            return user == msg.author

                        try:
                            react, user = await self.bot.wait_for('reaction_add', timeout=30, check=check)
                        except asyncio.TimeoutError:
                            return await soruemb.delete()
                        
                        if str(react.emoji) == '🇪':
                            biraderdenemesi = random.randint(0,4)
                            bıcak = random.randint(1,10)
                            buyukpara = random.randint(5000, 10000)
                            losemoney = random.randint(350, 1000)
                            if biraderdenemesi == 2:
                                balance += buyukpara
                                await self.sqlUpdate(user,balance)
                                emb = discord.Embed(color=msg.guild.me.color, title=f"İş gayet kaliteli gitti {bıcak} kişiye bıçagı taktın ve parayı kaptın\n**Kazanılan Para:** `{buyukpara:,d}₺`")
                                emb.set_author(name=user.name, icon_url=user.avatar_url)
                                emb.set_footer(text=Footer)
                                await soruemb.edit(embed=emb)
                            else:
                                balance -= losemoney
                                await self.sqlUpdate(user,balance)
                                emb = discord.Embed(color=msg.guild.me.color, title=f"İş berbat gitti sana bıçağı taktılar hastahanedesin paralar gitti moruq\n**Kaybedilen Para:** `-{losemoney}₺`")
                                emb.set_author(name=user.name, icon_url=user.avatar_url)
                                emb.set_footer(text=Footer)
                                await soruemb.edit(embed=emb)
                        else:
                            emb = discord.Embed(color=msg.guild.me.color, title="Teklif reddedildi para kazanamadın belkide bu senin için daha iyi bir seçimdir.")
                            emb.set_author(name=user.name, icon_url=user.avatar_url)
                            emb.set_footer(text=Footer)
                            return await soruemb.edit(embed=emb)
                    else:
                        balance += num
                        await self.sqlUpdate(user,balance)
                        emb = discord.Embed(color=msg.guild.me.color, title=f"{people} sana `{num}₺` verdi")
                        emb.set_author(name=user.name, icon_url=user.avatar_url)
                        emb.set_footer(text=Footer)
                        await msg.send(embed=emb)
                else:
                    sentence = await self.negativeSentences()
                    emb = discord.Embed(color=msg.guild.me.color, title=f"{people} {sentence}")
                    emb.set_author(name=user.name, icon_url=user.avatar_url)
                    emb.set_footer(text=Footer)
                    await msg.send(embed=emb)
            else:
                await self.accountCreate(msg,user)
                msg.command.reset_cooldown(msg)

    @dilen.error
    async def dilen_error(self, msg, err):
        if isinstance(err, commands.CommandOnCooldown):
            emb = discord.Embed(color=Kırmızı, title="Bekleme Süresi", description=f"Bu komutun **20.0s** bekleme süresi vardır\n**Kalan Süre:** `{err.retry_after:.2f}s`")
            emb.set_author(name=msg.author.name, icon_url=msg.author.avatar_url)
            emb.set_footer(text=Footer)
            await msg.send(embed=emb, delete_after=10)
            await asyncio.sleep(10)
            return await msg.message.delete()

    @command(aliases=['leaderboard', 'rich', 'zenginler'])
    async def sıralama(self, msg):
        await Logger.guildLogger(self, msg)
        with sqlite3.connect("users.db") as db:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM users ORDER BY money DESC")
            db.commit()
            msj = ""
            count = 1
            for i in cursor.fetchall():
                if count == 11:
                    break
                for j in msg.guild.members:
                    if j.id == i[0]:
                        if j.bot:
                            continue
                        msj += f"{count}. {j.mention} = `{i[1]:,d}₺`\n"
                        count += 1                       
            emb = discord.Embed(color=msg.guild.me.color, title="Sunucu Zenginleri", description=msj)
            emb.set_footer(text=Footer)
            emb.set_thumbnail(url=msg.guild.icon_url)
            await msg.send(embed=emb)

    @command()
    async def admin(self, msg, *, sql=None):
        await Logger.guildLogger(self, msg)
        if msg.author.id != owner:
            await msg.send(":no_entry: `Sadece sahibim kullanabilir!`", delete_after=25)
            await asyncio.sleep(25)
            return await msg.message.delete()
        if sql is None:
            return
        with sqlite3.connect("users.db") as db:
            try:
                cursor = db.cursor()
                cursor.execute(sql)
                db.commit()
                await msg.message.add_reaction("☑️")
            except Exception:
                await msg.message.add_reaction("⚠️")

    @command(aliases=['transfer', 'pg'])
    async def paragönder(self, msg, member: discord.Member=None, miktar: int=None):
        await Logger.guildLogger(self, msg)
        if member is None:
            emb = discord.Embed(color=Kırmızı, description=f"{msg.author.mention}, bir kullanıcı etiketlemelisin.\n```+paragönder @kullanıcı [miktar]```")
            return await msg.send(embed=emb, delete_after=25)
        if miktar is None:
            emb = discord.Embed(color=Kırmızı, description=f"{msg.author.mention}, bir miktar belirtmelisin.\n```+paragönder @kullanıcı [miktar]```")
            return await msg.send(embed=emb, delete_after=25)
        if miktar < 0:
            emb = discord.Embed(color=Kırmızı, description=f"{msg.author.mention}, göndermek istediğiniz miktar `0` dan küçük olamaz.")
            return await msg.send(embed=emb, delete_after=25)
        user = msg.author
        veri = await self.sqlGet(user)
        if veri:
            if veri[0][1] < miktar:
                emb = discord.Embed(color=Kırmızı, description=f"{user.mention}, `{0}-{veri[0][1]}` arasında bir para gönderebilirsin")
                return await msg.send(embed=emb, delete_after=25)
            veri1 = await self.sqlGet(member)
            if veri1:
                balance = veri[0][1]
                balance -= miktar
                await self.sqlUpdate(user, balance)
                balance = veri1[0][1]
                balance += miktar
                await self.sqlUpdate(member, balance)
                emb = discord.Embed(color=msg.guild.me.color, title=f"**{str(member)}** adlı kullanıcıya `{miktar}₺` gönderdin.")
                emb.set_author(name=user.name, icon_url=user.avatar_url)
                emb.set_footer(text=Footer)
                return await msg.send(embed=emb)
            else:
                emb = discord.Embed(color=Kırmızı, description=f"{user.mention}[{member.mention}] kullanıcısının hesabı yok o yüzden para gönderilemedi.")
                return await msg.send(embed=emb, delete_after=25)
        else:
            await self.accountCreate(msg,user)
    
    @paragönder.error
    async def paragönder_error(self, msg, err):
        if isinstance(err, commands.BadArgument):
            emb = discord.Embed(color=Kırmızı, description=f"{msg.author.mention}, bir kullanıcı etiketlemelisin.\n```+paragönder @kullanıcı [miktar]```")
            return await msg.send(embed=emb, delete_after=25)

    @command(aliases=['inventory', 'env'])
    async def envanter(self, msg, member: discord.Member=None):
        await Logger.guildLogger(self, msg)

    @command(aliases=['shop'])
    async def market(self, msg):
        await Logger.guildLogger(self, msg)

def setup(bot):
    bot.add_cog(Economy(bot))

