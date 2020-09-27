from config.ayarlar import *
import discord ,asyncio, random, sys, sqlite3
from discord.ext import commands
from discord.ext.commands import command
from src.cogs.economy import Economy
from log.logger import Logger
sys.path.append('../')


class Oyun(commands.Cog, name="Oyun"):
    def __init__(self, bot):
        self.bot = bot
    
    @command(aliases=['xox', 'sos'])
    @commands.cooldown(1, 300)
    async def gorilla(self, msg, member: discord.Member=None):
        await Logger.guildLogger(self, msg)
        if member is None:
            msg.command.reset_cooldown(msg)
            emb = discord.Embed(color=Kırmızı, description=f"{msg.author.mention}, bir kullanıcı etiketlemelisin.")
            return await msg.send(embed=emb, delete_after=25)
        
        elif member.bot == True:
            msg.command.reset_cooldown(msg)
            emb = discord.Embed(color=Kırmızı, description=f"{msg.author.mention}, bu oyunu botlar ile oynayamazsın.")
            return await msg.send(embed=emb, delete_after=25)

        elif member.id == msg.author.id:
            msg.command.reset_cooldown(msg)
            emb = discord.Embed(color=Kırmızı, description=f"{msg.author.mention}, dostum ama sen çok zekisin. Bu zekayla bu oyunu neden oynayamadığını tahmin et dostum.")
            return await msg.send(embed=emb, delete_after=25)

        emb = discord.Embed(color=msg.guild.me.color, description=f"{member.mention}, dostum kalk sana oyun daveti geldi eğer oynamak istiyorsan <a:dndostum:756864243646726244> emojisine bas dostum.", title="Gorilla davet")
        giriş = await msg.send(embed=emb)
        await giriş.add_reaction("<a:dndostum:756864243646726244>")

        def check(react, user):
            return user == member and str(react.emoji) == '<a:dndostum:756864243646726244>'
        try: 
            react, user = await self.bot.wait_for('reaction_add', timeout=45, check=check)
        except asyncio.TimeoutError:
            await giriş.delete()
            msg.command.reset_cooldown(msg)
            emb = discord.Embed(color=Kırmızı, description=f"{member.mention}, emojiye basmadığı için oyun iptal edildi.")
            return await msg.send(embed=emb, delete_after=25)
        await giriş.delete()

        seçim = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        bir = True
        iki = False
        karar = {"1":":one:", "2":":two:", "3":":three:", "4":":four:", "5":":five:", "6":":six:", "7":":seven:", "8":":eight:", "9":":nine:"}
        tabla = f"""{msg.author.mention}, şimdi senin sıran `1-9` arasında sayı belirt. İconun: <a:dndostum:756864243646726244>

                    {karar['1']} | {karar['2']} | {karar['3']}
                    ——————
                    {karar['4']} | {karar['5']} | {karar['6']}
                    ——————
                    {karar['7']} | {karar['8']} | {karar['9']}"""
        emb = discord.Embed(color=msg.guild.me.color, description=tabla, title="Gorilla Oyunu")
        emb.set_author(name=msg.author.name, icon_url=msg.author.avatar_url)
        emb.set_footer(text=Footer)
        embed = await msg.send(embed=emb)
        def winnerCheck():
            return (karar['1'] == karar['2'] and karar['1'] == karar['3']) or (karar['1'] == karar['4'] and karar['1'] == karar['7']) or (karar['4'] == karar['5'] and karar['4'] == karar['6']) or (karar['2'] == karar['5'] and karar['2'] == karar['8']) or (karar['7'] == karar['8'] and karar['7'] == karar['9']) or (karar['3'] == karar['6'] and karar['3'] == karar['9']) or (karar['1'] == karar['5'] and karar['1'] == karar['9']) or (karar['3'] == karar['5'] and karar['3'] == karar['7'])
        
        sayac = 0
        while True:
            sonuc = winnerCheck()
            if sonuc is True:
                await embed.delete()
                if bir is False and iki is True:
                    msg.command.reset_cooldown(msg)
                    emb = discord.Embed(color=Yeşil, title=f"{msg.author.name} Kazandı", description=f"{msg.author.mention} kullanıcısı {member.mention} kullanıcısına RKO çekti ve yerle bir etti kaybeden goril üzgün görünüyor")
                    emb.set_thumbnail(url=msg.author.avatar_url)
                    emb.set_footer(text=Footer)
                    await msg.send(embed=emb)
                elif bir is True and iki is False:
                    msg.command.reset_cooldown(msg)
                    emb = discord.Embed(color=Yeşil, title=f"{member.name} Kazandı", description=f"{member.mention} kullanıcısı {msg.author.mention} kullanıcısına RKO çekti ve yerle bir etti kaybeden goril üzgün görünüyor")
                    emb.set_thumbnail(url=member.avatar_url)
                    emb.set_footer(text=Footer)
                    await msg.send(embed=emb)
                break

            if sayac == 9:
                msg.command.reset_cooldown(msg)
                await embed.delete()
                emb = discord.Embed(color=discord.Color.from_rgb(255,255,0), description=f"{msg.author.mention} ile {member.mention} berabere kaldı.", title="Berabere")
                emb.set_footer(text=Footer)
                emb.set_thumbnail(url="https://discordapp.com/assets/e8b3b5a31c0a3c541960bd3ddccc538f.svg")
                await msg.send(embed=emb)
                break

            if bir is True:
                def check1(m):
                    return m.author == msg.author and m.content in seçim
                try:
                    mesaj = await self.bot.wait_for('message', timeout=45, check=check1)
                except asyncio.TimeoutError:
                    msg.command.reset_cooldown(msg)
                    await embed.delete()
                    emb = discord.Embed(color=Kırmızı, discription=f"{msg.author.mention}, kullanıcısının süresi doldu oyun iptal edildi.")
                    await msg.send(embed=emb, delete_after=25)
                    break
                seçim.remove(mesaj.content)
                karar[mesaj.content] = "<a:dndostum:756864243646726244>"
                newtabla = f"""{member.mention}, şimdi senin sıran `1-9` arasında sayı belirt. İconun: <a:gorilla22:757375918842052648>

                    {karar['1']} | {karar['2']} | {karar['3']}
                    ——————
                    {karar['4']} | {karar['5']} | {karar['6']}
                    ——————
                    {karar['7']} | {karar['8']} | {karar['9']}"""
                emb2 = discord.Embed(color=msg.guild.me.color, description=newtabla, title="Gorilla Oyunu")
                emb2.set_author(name=member.name, icon_url=member.avatar_url)
                emb2.set_footer(text=Footer)
                await embed.edit(embed=emb2)
                await mesaj.delete()
                sayac += 1
                bir = False
                iki = True
                continue
            
            if iki is True:
                def check2(m):
                    return m.author == member and m.content in seçim
                try:
                    mesaj = await self.bot.wait_for('message', timeout=45, check=check2)
                except asyncio.TimeoutError:
                    msg.command.reset_cooldown(msg)
                    await embed.delete()
                    emb = discord.Embed(color=Kırmızı, discription=f"{member.mention}, kullanıcısının süresi doldu oyun iptal edildi.")
                    await msg.send(embed=emb, delete_after=25)
                    break
                seçim.remove(mesaj.content)
                karar[mesaj.content] = "<a:gorilla22:757375918842052648>"
                newtabla = f"""{msg.author.mention}, şimdi senin sıran `1-9` arasında sayı belirt. İconun: <a:dndostum:756864243646726244>

                    {karar['1']} | {karar['2']} | {karar['3']}
                    ——————
                    {karar['4']} | {karar['5']} | {karar['6']}
                    ——————
                    {karar['7']} | {karar['8']} | {karar['9']}"""
                emb2 = discord.Embed(color=msg.guild.me.color, description=newtabla, title="Gorilla Oyunu")
                emb2.set_author(name=msg.author.name, icon_url=msg.author.avatar_url)
                emb2.set_footer(text=Footer)
                await embed.edit(embed=emb2)
                await mesaj.delete()
                sayac += 1
                bir = True
                iki = False
                continue

    @gorilla.error
    async def gorilla_error(self, msg, err):
        if isinstance(err, commands.CommandOnCooldown):
            emb = discord.Embed(color=Kırmızı, description=f"**Gorilla** oyunu şuan bu sunucuda oynanıyor lütfen bitmesini bekle [{msg.author.mention}]")
            await msg.send(embed=emb, delete_after=25)
            await asyncio.sleep(5)
            return await msg.message.delete()
  
    @command(aliases=["sayıtahmin"])
    @commands.cooldown(1, 300)
    async def tahmin(self, ctx):
        await Logger.guildLogger(self, ctx)
        try:
            await ctx.message.delete()
            channel = ctx.message.channel
            bilgi = discord.Embed(title="Sayı Tahmin", color=ctx.guild.me.color,
                                  description=f"Merhaba `{ctx.message.author.name}` Hazırsan Başlıyalım.\nOyuna Başlamak için sohbete `başla` yaz `20` saniyen var.")
            bilgi.set_author(name=self.bot.user.name,
                             icon_url=self.bot.user.avatar_url)
            bilgi.set_footer(text=Footer)
            msg = await ctx.send(embed=bilgi, delete_after=20)

            try:
                wait = await self.bot.wait_for("message", timeout=20)
            except asyncio.TimeoutError:
                await ctx.send(f"{ctx.author.mention} Süren Doldu Oyun İptal Edildi.", delete_after=10)
                ctx.command.reset_cooldown(ctx)
                await ctx.message.delete()

            if wait.author != ctx.message.author:
                pass
            elif wait.author == ctx.message.author:
                if wait.content != "başla":
                    await ctx.send(f"{ctx.author.mention} `başla` yazmadıgın için oyun iptal edildi.", delete_after=10)
                    ctx.command.reset_cooldown(ctx)

                elif wait.content == "başla" and wait.channel == channel:
                    await asyncio.sleep(0.3)
                    await wait.delete()
                    await msg.delete()
                    hak = 10
                    sayı = random.randint(1, 50)
                    print(f"Tutulan Sayı: {sayı}")
                    embed = discord.Embed(title="Sayı Tahmin", color=ctx.guild.me.color,
                                          description=f"**Sayı Aralığı**: `1-50`Arasında\n**Belirlenen Hak**: `{hak}`\n**Her Tahmin İçin Beklenecek Süre**: `60sn`\n__**Hadi Tahmin Etmeye Başla**__")
                    embed.set_author(name=ctx.author.name,
                                     icon_url=ctx.author.avatar_url)
                    embed.set_footer(text=Footer)
                    emebed = await ctx.send(embed=embed)

                    try:
                        while hak > 0:
                            tahmin = await self.bot.wait_for("message", timeout=60)
                            if tahmin.author != ctx.message.author:
                                pass

                            elif tahmin.author == ctx.message.author:
                                if int(tahmin.content) <= 50 and int(tahmin.content) >= 1:
                                    if int(tahmin.content) < sayı:
                                        await asyncio.sleep(0.3)
                                        await tahmin.delete()
                                        hak -= 1
                                        doldur = f":arrow_up: `Yukarı`\n:envelope_with_arrow: **Gönderdigin Sayı**: `{int(tahmin.content)}`"
                                        hesap = discord.Embed(
                                            title=f"Kalan Hak: {hak}", color=ctx.guild.me.color, description=doldur)
                                        hesap.set_author(
                                            name=ctx.author.name, icon_url=ctx.author.avatar_url)
                                        hesap.set_footer(text=Footer)
                                        await emebed.edit(embed=hesap)
                                        continue

                                    elif int(tahmin.content) > sayı:
                                        await asyncio.sleep(0.3)
                                        await tahmin.delete()
                                        hak -= 1
                                        doldur = f":arrow_down: `Aşagı`\n:envelope_with_arrow: **Gönderdigin Sayı**: `{int(tahmin.content)}`"
                                        hesap = discord.Embed(
                                            title=f"Kalan Hak: {hak}", color=ctx.guild.me.color, description=doldur)
                                        hesap.set_author(
                                            name=ctx.author.name, icon_url=ctx.author.avatar_url)
                                        hesap.set_footer(text=Footer)
                                        await emebed.edit(embed=hesap)
                                        continue

                                    elif int(tahmin.content) == sayı:
                                        await asyncio.sleep(0.3)
                                        await tahmin.delete()
                                        await asyncio.sleep(0.1)
                                        await emebed.delete()
                                        hak -= 1
                                        hesap = discord.Embed(
                                            title=f"Tebrikler {tahmin.author.name}", color=Yeşil,
                                            description=f"**Tutulan Sayı**: `{sayı}`\n**Kaç Denemede Bulundu**: `{10 - hak}`")
                                        hesap.set_author(
                                            name=ctx.author.name, icon_url=ctx.author.avatar_url)
                                        hesap.set_footer(text=Footer)
                                        hesap.set_thumbnail(
                                            url=ctx.author.avatar_url)
                                        hesap.timestamp = ctx.message.created_at
                                        await ctx.send(embed=hesap)
                                        ctx.command.reset_cooldown(ctx)
                                        break

                                else:
                                    await tahmin.delete()
                                    await emebed.delete()
                                    süre = discord.Embed(
                                        title="Hata", color=Kırmızı,
                                        description=":warning: : Yazdıgınınız değer `sayı` olmalı.\n:warning: : Yazdığınız Değer `1-50` arasında olmalı.\n:warning: : Her hak süresi `60sn`.")
                                    süre.set_author(
                                        name=ctx.author.name, icon_url=ctx.author.avatar_url)
                                    süre.set_footer(text=Footer)
                                    await ctx.send(embed=süre, delete_after=15)
                                    ctx.command.reset_cooldown(ctx)
                                    break

                        if hak == 0:
                            await emebed.delete()
                            await ctx.send(f"Knk Üzgünüm Ama Hakkın Bitti.\n**Tuttugum Sayı**: `{sayı}`", delete_after=60)
                            ctx.command.reset_cooldown(ctx)
                    except Exception:
                        await asyncio.sleep(0.2)
                        await tahmin.delete()
                        süre = discord.Embed(
                            title="Hata", color=Kırmızı,
                            description=":warning: : Yazdıgınınız değer `sayı` olmalı.\n:warning: : Yazdığınız Değer `1-50` arasında olmalı.\n:warning: : Her hak süresi `60sn`.")
                        süre.set_author(name=ctx.author.name,
                                        icon_url=ctx.author.avatar_url)
                        süre.set_footer(text=Footer)
                        await ctx.send(embed=süre, delete_after=15)
                        ctx.command.reset_cooldown(ctx)
        except Exception as err:
            print(err)
            ctx.command.reset_cooldown(ctx)

    @tahmin.error
    async def tahmin_error(self, msg, err):
        if isinstance(err, commands.CommandOnCooldown):
            emb = discord.Embed(color=Kırmızı, description=f"**Tahmin** oyunu şuan bu sunucuda oynanıyor lütfen bitmesini bekle [{msg.author.mention}]")
            await msg.send(embed=emb, delete_after=25)
            await asyncio.sleep(5)
            return await msg.message.delete()

    @staticmethod
    async def slotGenerator():
        fires = ['🍒', '🍇', '🍑', '🍉', '🍆', '🍎', '🍌']
        one = random.choice(fires)
        two = random.choice(fires)
        three = random.choice(fires)
        return one, two ,three

    @command(aliases=['slots'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def slot(self, msg, bahis: int=None):
        await Logger.guildLogger(self, msg)
        if bahis is None:
            emb = discord.Embed(color=Kırmızı, description="Bi bahis koy ortaya knk")
            msg.command.reset_cooldown(msg)
            return await msg.send(embed=emb, delete_after=25)
        if bahis < 100:
            emb = discord.Embed(color=Kırmızı, description="Hocam `100₺` den az para basamazsın")
            msg.command.reset_cooldown(msg)
            return await msg.send(embed=emb, delete_after=25)
        user = msg.author
        veri = await Economy.sqlGet(user)
        if veri:
            if veri[0][1] < bahis:
                emb = discord.Embed(color=Kırmızı, description="Paran yetmiyo agam paranın yettiği kadar bas eğer yoksa `+dilen` ile dilenebilirsin")
                return await msg.send(embed=emb, delete_after=25)
            eksilt = veri[0][1]
            eksilt -= bahis
            await Economy.sqlUpdate(user, eksilt)
            veri = await Economy.sqlGet(user)
            sonuc = await self.slotGenerator()
            msj = f"""{user.mention}, `{bahis}₺` bastın bakalım ne gelicek
            ——————
            {sonuc[0]} | {sonuc[1]} | {sonuc[2]}
            ——————"""
            emb = discord.Embed(color=msg.guild.me.color, description=msj)
            emb.set_author(name=user.name, icon_url=user.avatar_url)
            emb.set_footer(text=Footer)
            embed = await msg.send(embed=emb)
            await asyncio.sleep(0.5)
            # Efekt
            for i in range(6):
                sonuc = await self.slotGenerator()
                msj = f"""{user.mention}, `{bahis}₺` bastın bakalım ne gelicek
                ——————
                {sonuc[0]} | {sonuc[1]} | {sonuc[2]}
                ——————"""
                emb = discord.Embed(color=msg.guild.me.color, description=msj)
                emb.set_author(name=user.name, icon_url=user.avatar_url)
                emb.set_footer(text=Footer)
                await embed.edit(embed=emb)
                await asyncio.sleep(0.5)
            await asyncio.sleep(5)
            if sonuc[0] == sonuc[1] and sonuc[0] == sonuc[2]:
                bahis *= random.randint(5,7)
                balance = bahis + veri[0][1]
                await Economy.sqlUpdate(user,balance)
                emb = discord.Embed(color=Yeşil, title=f"Hepsini tutturdun `{bahis}₺` Kazandın!")
                emb.set_author(name=user.name, icon_url=user.avatar_url)
                emb.set_footer(text=Footer)
                return await embed.edit(embed=emb)
            elif sonuc[0] == sonuc[1] or sonuc[0] == sonuc[2] or sonuc[1] == sonuc[2]:
                bahis *= 2
                balance = veri[0][1] + bahis
                await Economy.sqlUpdate(user, balance)
                emb = discord.Embed(color=Yeşil, title=f"İki tane tutturdun `{bahis}₺` Kazandın!")
                emb.set_author(name=user.name, icon_url=user.avatar_url)
                emb.set_footer(text=Footer)
                return await embed.edit(embed=emb)
            else:
                emb = discord.Embed(color=Kırmızı, title=f"`-{bahis}₺` Kaybettin")
                emb.set_author(name=user.name, icon_url=user.avatar_url)
                emb.set_footer(text=Footer)
                await embed.edit(embed=emb)
        else:
            await Economy.accountCreate(msg, user)

    @slot.error
    async def slot_error(self, msg, err):
        if isinstance(err, commands.CommandOnCooldown):
            emb = discord.Embed(color=Kırmızı, title="Bekleme Süresi", description=f"Bu komutun **5.0s** bekleme süresi vardır\n**Kalan Süre:** `{err.retry_after:.2f}s`")
            emb.set_author(name=msg.author.name, icon_url=msg.author.avatar_url)
            emb.set_footer(text=Footer)
            await msg.send(embed=emb, delete_after=5)
            await asyncio.sleep(5)
            return await msg.message.delete()

    @command(aliases=['spincoin', 'yt'])
    async def yazıtura(self, msg, bahis: int=None):
        await Logger.guildLogger(self, msg)
        if bahis is None:
            emb = discord.Embed(color=Kırmızı, description="Bi bahis koy ortaya knk")
            msg.command.reset_cooldown(msg)
            return await msg.send(embed=emb, delete_after=25)
        if bahis < 100:
            emb = discord.Embed(color=Kırmızı, description="Hocam `100₺` den az para basamazsın")
            msg.command.reset_cooldown(msg)
            return await msg.send(embed=emb, delete_after=25)
        user = msg.author
        veri = await Economy.sqlGet(user)
        if veri:
            if veri[0][1] < 100:
                emb = discord.Embed(color=Kırmızı, description="Paran yetmiyo agam paranın yettiği kadar bas eğer yoksa `+dilen` ile dilenebilirsin")
                return await msg.send(embed=emb, delete_after=25)
            
            emb = discord.Embed(color=msg.guild.me.color, title="Yazı Tura", description="**Yazımı Turamı dostum seç bakalım.**\n__**Yazı= Y || Tura= T**__")
            emb.set_author(name=user.name, icon_url=user.avatar_url)
            emb.set_footer(text=Footer)
            embed = await msg.send(embed=emb)
            await embed.add_reaction("🇾")
            await embed.add_reaction("🇹")
            def check(react, userr):
                return userr == user
            try:
                react, userr = await self.bot.wait_for('reaction_add', timeout=31, check=check)
            except asyncio.TimeoutError:
                emb = discord.Embed(color=Kırmızı, description="Cevap verme süren doldu")
                return await msg.send(embed=emb, delete_after=25)
            balance = veri[0][1]
            balance -= bahis
            await Economy.sqlUpdate(user,balance)
            result = random.randint(0,101)
            yazı = False
            tura = False
            paradik = False
            if result > 0 and result <= 50:
                yazı = True
            elif result > 50 and result <= 100:
                tura = True
            elif result == 101:
                paradik = True

            await embed.edit(content="**Sonuç Bekleniyor :** `■■□□□□□□□□`")
            await asyncio.sleep(0.3)
            await embed.edit(content="**Sonuç Bekleniyor :** `■■■■□□□□□□`")
            await asyncio.sleep(0.3)
            await embed.edit(content="**Sonuç Bekleniyor :** `■■■■■■□□□□`")
            await asyncio.sleep(0.3)
            await embed.edit(content="**Sonuç Bekleniyor :** `■■■■■■■■□□`")
            await asyncio.sleep(0.3)
            await embed.edit(content="**Sonuç Bekleniyor :** `■■■■■■■■■■`")
            await asyncio.sleep(0.3)
            
            if str(react.emoji) == "🇹":
                if paradik is True:
                    bahis *= 10
                    balance += bahis
                    await Economy.sqlUpdate(user,balance)
                    emb = discord.Embed(color=Mor, title=f"Para dik geldi `{bahis:,d}₺` Kazandın!")
                    emb.set_author(name=user.name, icon_url=user.avatar_url)
                    emb.set_footer(text=Footer)
                    return await embed.edit(embed=emb)
                if tura is True:
                    bahis *= 2
                    balance += bahis
                    await Economy.sqlUpdate(user,balance)
                    emb = discord.Embed(color=Yeşil, title=f"Tura geldi `{bahis:,d}₺` Kazandın!")
                    emb.set_author(name=user.name, icon_url=user.avatar_url)
                    emb.set_footer(text=Footer)
                    return await embed.edit(embed=emb)
                else:
                    emb = discord.Embed(color=Kırmızı, title=f"Yazı geldi `{bahis:,d}₺` Kaybettin!")
                    emb.set_author(name=user.name, icon_url=user.avatar_url)
                    emb.set_footer(text=Footer)
                    return await embed.edit(embed=emb)
            elif str(react.emoji) == "🇾":
                if paradik is True:
                    bahis *= 10
                    balance += bahis
                    await Economy.sqlUpdate(user,balance)
                    emb = discord.Embed(color=Mor, title=f"Para dik geldi `{bahis:,d}₺` Kazandın!")
                    emb.set_author(name=user.name, icon_url=user.avatar_url)
                    emb.set_footer(text=Footer)
                    return await embed.edit(embed=emb)
                if yazı is True:
                    bahis *= 2
                    balance += bahis
                    await Economy.sqlUpdate(user,balance)
                    emb = discord.Embed(color=Yeşil, title=f"Yazı geldi `{bahis:,d}₺` Kazandın!")
                    emb.set_author(name=user.name, icon_url=user.avatar_url)
                    emb.set_footer(text=Footer)
                    return await embed.edit(embed=emb)
                else:
                    emb = discord.Embed(color=Kırmızı, title=f"Tura geldi `{bahis:,d}₺` Kaybettin!")
                    emb.set_author(name=user.name, icon_url=user.avatar_url)
                    emb.set_footer(text=Footer)
                    return await embed.edit(embed=emb)
        else:
            await Economy.accountCreate(msg, user)

def setup(bot):
    bot.add_cog(Oyun(bot))
        