import discord
from discord.ext import commands # 봇 명령어와 관련된 기능을 제공하는 모듈
import asyncio
import os
from dotenv import load_dotenv
import random
from datetime import datetime
from zoneinfo import ZoneInfo
import cardName, cardMeaning


# intents는 봇이 어떤 이벤트를 수신할지 결정하는 설정입니다.
intents = discord.Intents.default()
intents.message_content = True

# bot은 discord.py 라이브러리에서 제공하는 Bot 클래스의 인스턴스입니다.
bot = commands.Bot(command_prefix='!', intents=intents)
# command_prefix=''는 호출 접두사 설정
# intents=intents를 통해 봇이 설정된 권한을 사용하도록 설정

# commands.Bot은 리스트 형태로 전달된 command_prefix에서 
# 리스트의 각 원소를 별도의 접두사로 처리하도록 설계되어 있습니다.


tarot_name = cardName.tarot_name
tarot_meaning = cardMeaning.tarot_meaning
symbolon_name = cardName.symbolon_name
symbolon_meaning = cardMeaning.symbolon_meaning

KST = ZoneInfo("Asia/Seoul")


# 카드 의미 보기 버튼을 위한 클래스
class MeaningView(discord.ui.View):
    def __init__(self, card_id, cards, meanings):
        super().__init__()
        self.card_id = card_id
        self.cards = cards
        self.meanings = meanings

    @discord.ui.button(label="카드 의미 보기", style=discord.ButtonStyle.primary)
    async def show_tarot_meaning(self, interaction: discord.Interaction, button: discord.ui.Button):
        card_name = self.cards.get(self.card_id)
        meaning = self.meanings.get(self.card_id)

        if meaning is None:
            await interaction.response.send_message(
                f"앗! 아직은 '{card_name}' 카드의 뜻이 없나 봐요.", 
                ephemeral=True
                )
        else:
            await interaction.response.send_message(
                f"{self.card_id} {card_name} 카드의 의미는: \n{meaning}", 
                ephemeral=True
                )



@bot.event
async def on_ready():
    print("타로타로봇이 로그인에 성공했어요.")


@bot.command()
async def 타로뽑기(ctx):
    card_id = random.choice(list(tarot_name))
    card_name = tarot_name[card_id]

    now = datetime.now(KST).strftime("%m/%d %H:%M:%S")
    await asyncio.sleep(3)

    view = MeaningView(card_id, tarot_name, tarot_meaning)
    await ctx.send(f'{now}에 {ctx.author.mention}님이 뽑은 타로 카드는 {card_name} !', view=view)


@bot.command()
async def 타로의미(ctx, card_name: str = None):
    if card_name is None:
        await ctx.send("이렇게 입력하면 돼요:",
                       "`!타로의미 m01`, `!타로의미 w02`, `!타로의미 ca`, `!타로의미 sk`, `!타로의미 pn`")
        return

    card_id = card_name.strip().lower()
    card = tarot_name.get(card_id)

    if card is None:
        await ctx.send(f"앗! '{card_name}'에 해당하는 카드가 없나 봐요.")
        return
    
    meaning = tarot_meaning.get(card_id)

    if meaning is None:
        await ctx.send(f"앗! 아직은 '{card}' 카드의 뜻이 없나 봐요.")
    else:
        await ctx.send(f"{card_id} {card} 카드의 의미는: \n{meaning}")


@bot.command()
async def 타로뽑기3(ctx):
    card1 = random.choice(list(tarot_name.values()))
    card2 = random.choice(list(tarot_name.values()))
    card3 = random.choice(list(tarot_name.values()))
    now = datetime.now(KST).strftime("%m/%d %H:%M:%S")
    await asyncio.sleep(3)
    await ctx.send(f'{now}에 {ctx.author.mention}님이 뽑은 타로 카드는 {card1}, {card2}, {card3} !')


@bot.command()
async def 양자택일(ctx):
    card1 = random.choice(list(tarot_name.values()))
    card2 = random.choice(list(tarot_name.values()))
    now = datetime.now(KST).strftime("%m/%d %H:%M:%S")
    await asyncio.sleep(3)
    await ctx.send(f'{now}에 {ctx.author.mention}님이 뽑은 타로 카드는 {card1} 그리고 {card2} !')


@bot.command()
async def 심볼론뽑기(ctx):
    card_id = random.choice(list(symbolon_name))
    card_name = symbolon_name[card_id]

    now = datetime.now(KST).strftime("%m/%d %H:%M:%S")
    await asyncio.sleep(3)

    view = MeaningView(card_id, symbolon_name, symbolon_meaning)

    await ctx.send(f'{now}에 {ctx.author.mention}님이 뽑은 심볼론 카드는 {card_name} !', view=view)


@bot.command()
async def 심볼론의미(ctx, card_name: str = None):
    if card_name is None:
        await ctx.send(
            "이렇게 입력하면 돼요:\n"
            "`!심볼론의미 01`"
        )
        return

    card_id = card_name.strip().lower()
    card = symbolon_name.get(card_id)

    if card is None:
        await ctx.send(f"앗! '{card_name}'에 해당하는 카드가 없나 봐요.")
        return
    
    meaning = symbolon_meaning.get(card_id)

    if meaning is None:
        await ctx.send(f"앗! 아직은 '{card}' 카드의 뜻이 없나 봐요.")
    else:
        await ctx.send(f"{card_id} {card} 카드의 의미는: \n{meaning}")


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN이 설정되지 않았습니다.")


bot.run(TOKEN)