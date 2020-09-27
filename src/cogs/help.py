import discord, sys
import asyncio
from discord.ext import commands
from discord.ext.commands import command
sys.path.append('../')
from config.ayarlar import *
from log.logger import Logger

class Help(commands.Cog, name="Yardım"):
    def __init__(self, bot):
        self.bot = bot

    async def owner(self, msg):
        emb = discord.Embed(color=msg.guild.me.color, title="Ekonomi Komutları")
        emb.set_footer(text=f"Sayfa 7/10")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.add_field(name=f"`{prefix}bakiye`", value="Bottaki bakiyenizi sorgular eğer ilk defa kullandıysanız hesabınıza para aktarılır.", inline=False)
        emb.add_field(name=f"`{prefix}dilen`", value="Para dilenirsiniz şansınız yaver giderse para kazanırsınız.", inline=False)
        emb.add_field(name=f"`{prefix}sıralama`", value="Sunucudaki kullanıcıların bakiye sıralamasını yapar en zenginler ortaya çıkar.", inline=False)
        emb.add_field(name=f"`{prefix}paragönder`", value="Etiketlediğiniz kullanıcıya bellirttiğiniz miktarda para gönderir.", inline=False)
        return emb

    async def aliases(self, msg):
        msj = f"Komut kısaltmalarını [Buraya](https://pulchra.glitch.me/komutlar.html) tıklayarak ögrenebilirsiniz"
        emb = discord.Embed(color=msg.guild.me.color, description=msj, title="Komut Kısaltmaları")
        emb.set_footer(text="Sayfa 8/10")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        return emb

    async def support(self, msg):
        msj = "**Bir sorunun varsa destek sunucumuz:** [PulchraSUPPORT](https://discord.gg/C8wvJqG)\n"
        msj += "**Botumuzun Web Sitesi:** [PulchraBOT](https://pulchra.glitch.me)\n"
        msj += "**Botumuzun Tüm Komutları:** [Komutlar](https://pulchra.glitch.me/komutlar.html)\n"
        msj += f"**Yazılımcı:** <@!{owner}>\n"
        msj += "**Grafik Ve Tasarımcımız:** <@!384328582912278540>\n"
        emb = discord.Embed(color=msg.guild.me.color, description=msj, title="İletişim Ve Destek")
        emb.set_footer(text="Sayfa 10/10")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        return emb
        
    async def botstat(self, msg):
        ping = self.bot.latency * 1000
        emojiCount = len(self.bot.emojis)
        commandCount = len(self.bot.commands)
        guildCount = len(self.bot.guilds)
        userCount = len(self.bot.users)
        muzikCalınanSunucu = len(self.bot.voice_clients)
        KKsayısı = await Logger.sqlLoggerGet()
        msj = f"**Ping:** `{ping:.2f}`\n"
        msj += f"**Sunucu Sayısı:** `{guildCount}`\n"
        msj += f"**Kullanıcı Sayısı:** `{userCount}`\n"
        msj += f"**Bu Zamana Kadar Kullanılan Komut Sayısı:** `{KKsayısı[0][1]}`\n"
        msj += f"**Emoji Sayısı:** `{emojiCount}`\n"
        msj += f"**Komut Sayısı:** `{commandCount}`\n"
        msj += f"**Müzik Çalınan Sunucu Sayısı:** `{muzikCalınanSunucu}`"
        emb = discord.Embed(color=msg.guild.me.color, title="Bot İstatistik", description=msj)
        emb.set_footer(text="Sayfa 9/10")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        return emb
    
    async def spotify(self, msg):
        emb = discord.Embed(color=msg.guild.me.color, title="Spotify", description="Bu komut bu botu özel kılan bir komuttur bir nevi spotify premium olarak adlandırılabilir.")
        emb.set_footer(text=f"Sayfa 2/10")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.add_field(name=f"`{prefix}spotify`", value="Spotifydan müzik dinliyorsanız +spotify. Başkasının şarkılarını dinlemek istiyosanız +spotify @kullanıcı şeklinde kullanılır. Kullanıcı o an spotifydan ne dinliyosa botta aynı müzigi çalar müzik değişirse bottada değişir.", inline=False)
        emb.add_field(name=f"`{prefix}dur`", value="Döngüyü ve şarkıyı durdurur.", inline=False)
        return emb

    async def games(self, msg):
        emb = discord.Embed(color=msg.guild.me.color, title="Oyunlar")
        emb.set_footer(text=f"Sayfa 6/10")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.add_field(name=f"`{prefix}sayıtahmin`", value="Sayı tahmin oyunu oynatır.", inline=False)
        emb.add_field(name=f"`{prefix}gorilla`", value="Goril temalı xox oyunu oynarsınız.", inline=False)
        emb.add_field(name=f"`{prefix}slot`", value="Slot oynarsınız **[Para basmanız gerek]**", inline=False)
        emb.add_field(name=f"`{prefix}yazıtura`", value="Yazıtura oynarsınız **[Para basmanız gerek]**", inline=False)
        return emb

    async def general(self, msg):
        emb = discord.Embed(color=msg.guild.me.color, title="Genel Komutlar")
        emb.set_footer(text=f"Sayfa 5/10")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.add_field(name=f"`{prefix}pp`", value="Avataranızı veya etiketlerseniz o kişinin avatarını göterir.", inline=False)
        emb.add_field(name=f"`{prefix}çeviri`", value="yazdıgınız cümlenin hangi dil oldugunu algılayıp onu belirttiginiz dile çevirir.'+çeviri ru yarın görüşürüz' kullanımı bu şekildedir.", inline=False)
        emb.add_field(name=f"`{prefix}kbilgi`", value="Hesabınız hakkında bilgi verir başka bir kullanıcıda etiketlenebilir.", inline=False)
        emb.add_field(name=f"`{prefix}sunucu`", value="Sunucu hakkında bilgi verir.", inline=False)
        emb.add_field(name=f"`{prefix}tahmin`", value="Sayı tahmin oyunu oynatır.", inline=False)
        emb.add_field(name=f"`{prefix}yaz`", value="Bota istediğiniz mesajı yazdırır.", inline=False)
        emb.add_field(name=f"`{prefix}davet`", value="Botun davet linkini atar.", inline=False)
        emb.add_field(name=f"`{prefix}eyaz`", value="Yazdıgınız mesajı emojiye çevirir.", inline=False)
        return emb

    async def music2(self, msg):
        emb = discord.Embed(color=msg.guild.me.color, title="Müzik Komutları")
        emb.set_footer(text=f"Sayfa 4/10")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.add_field(name=f"`{prefix}çıkar`", value=f"**{prefix}sıradakiler** komutu ile numarası ögrenilen şarkı listeden çıkarılır.", inline=False)
        emb.add_field(name=f"`{prefix}katıl`", value="Odaya katılır", inline=False)
        emb.add_field(name=f"`{prefix}çık`", value="Odadan ayrılır", inline=False)
        emb.add_field(name=f"`{prefix}duraklat`", value="Çalan parçayı +devam yazana kadar duraklatır.", inline=False)
        emb.add_field(name=f"`{prefix}devam`", value="Duraklatılmış şarkıyı devam ettirir.", inline=False)
        emb.add_field(name=f"`{prefix}çalan`", value="Çalan şarkıyı gösterir.", inline=False)
        emb.add_field(name=f"`{prefix}ses`", value="Ses seviyesini ayarlar. Yanına sayı belirtmeden kullanımda anlık olarak ses değiştirebileceginiz arayüz atar.", inline=False)
        emb.add_field(name=f"`{prefix}arama`", value="Youtube veya soundcloud platformlarından arama yapar dilerseniz sonucu botta çalmaya başlar.", inline=False)
        return emb

    async def music(self, msg):
        emb = discord.Embed(color=msg.guild.me.color, title="Müzik Komutları")
        emb.set_footer(text=f"Sayfa 3/10")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        emb.add_field(name=f"`{prefix}çal`", value="Şarkı ismi, youtubeURL, ve spotifyURL girdilerini bulup botta çalmaya başlar.", inline=False)
        emb.add_field(name=f"`{prefix}dur`", value="Çalan müziği durdurur ve sırada müzik varsa hepsini siler.", inline=False)
        emb.add_field(name=f"`{prefix}tekrar`", value="Çalan şarkıyı siz bidaha bu komutu kullanana kadar tekrar tekrar çalar.", inline=False)
        emb.add_field(name=f"`{prefix}reset`", value="Çalan şarkıyı başa sarar.", inline=False)
        emb.add_field(name=f"`{prefix}karıştır`", value="Sırada şarkı varsa o şarkı kuyruğunu karıştırır.", inline=False)
        emb.add_field(name=f"`{prefix}geç`", value=f"Sırada şarkı varsa bir sonraki şarkıya geçer **{prefix}sıradakiler** komutu ile sıradaki şarkı numarasına görede geçiş yapılabilir.", inline=False)
        emb.add_field(name=f"`{prefix}sıradakiler`", value="Sırada şarkı varsa onları gösterir.", inline=False)
        return emb

    async def mainpage(self, msg):
        msj = "**Spotify:** `sayfa 2`\n"
        msj += "**Müzik:** `sayfa 3-4`\n"
        msj += "**Genel:** `sayfa 5`\n"
        msj += "**Oyunlar:** `sayfa 6`\n"
        msj += "**Ekonomi:** `sayfa 7`\n"
        msj += "**Komut kısaltmalar:** `sayfa 8`\n"
        msj += "**Bot bilgi:** `sayfa 9`\n"
        msj += "**İletişim ve Destek:** `sayfa 10`"
        emb = discord.Embed(color=msg.guild.me.color, title="Yardım", description=msj)
        emb.set_footer(text=f"{Footer} 1/10")
        emb.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
        return emb

    @command(aliases=["help", "h", "hlp"])
    async def yardım(self, msg):
        await Logger.guildLogger(self, msg)
        botstat = await self.botstat(msg)
        mainpage = await self.mainpage(msg)
        owner = await self.owner(msg)
        spotify = await self.spotify(msg)
        music = await self.music(msg)
        music2 = await self.music2(msg)
        genel = await self.general(msg)
        kısaltmalar = await self.aliases(msg)
        destek = await self.support(msg)
        oyunlar = await self.games(msg)
        embed = await msg.send(embed=mainpage)
        await embed.add_reaction('\u23EE')  # baş
        await embed.add_reaction('\u25c0')  # sol
        await embed.add_reaction('\u25b6')  # sağ
        await embed.add_reaction('\u23ED')  # son
        pages = [mainpage,spotify,music,music2,genel,oyunlar,owner,kısaltmalar,botstat,destek]
        i = 0
        click = ""
        while True:
            if click == '\u23EE':
                if i != 0:
                    i = 0
                    await embed.edit(embed=pages[i])
            elif click == '\u25c0':
                if i > 0:
                    i -= 1
                    await embed.edit(embed=pages[i])
            elif click == '\u25b6':
                if i < 9:
                    i += 1
                    await embed.edit(embed=pages[i])
            elif click == '\u23ED':
                if i != 9:
                    i = 9
                    await embed.edit(embed=pages[i])
            
            def check(react, user):
                return user == msg.author
            
            try:
                react, user = await self.bot.wait_for('reaction_add', timeout=60, check=check)
            except asyncio.TimeoutError:
                break
            click = str(react.emoji)

def setup(bot):
    bot.add_cog(Help(bot))