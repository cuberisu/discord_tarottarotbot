import discord
from discord.ext import commands # 봇 명령어와 관련된 기능을 제공하는 모듈
import asyncio
import os
from dotenv import load_dotenv
import random
from datetime import datetime
from zoneinfo import ZoneInfo
import cardList


intents = discord.Intents.default()  # 기본 intents 사용, 필요시 수정 가능
intents.message_content = True  # 메시지 내용을 읽으려면 True로 설정

bot = commands.Bot(command_prefix='!', intents=intents)
# bot = commands.Bot(command_prefix='', intents=intents)
# command_prefix=''는 호출 접두사 설정
# intents=intents를 통해 봇이 설정된 권한을 사용하도록 설정

# commands.Bot은 리스트 형태로 전달된 command_prefix에서 
# 리스트의 각 원소를 별도의 접두사로 처리하도록 설계되어 있습니다.

tarot = cardList.tarot
symbolon = cardList.symbolon

KST = ZoneInfo("Asia/Seoul")

@bot.event
async def on_ready():
    print("타로타로봇이 로그인에 성공했어요.")


@bot.command()
async def 타로뽑기(ctx):
    card = random.choice(list(tarot.values()))
    now = datetime.now(KST).strftime("%m/%d %H:%M:%S")
    await asyncio.sleep(3)
    await ctx.send(f'{now}에 당신이 뽑은 타로 카드는 {card} !')

@bot.command()
async def 타로뽑기3(ctx):
    card1 = random.choice(list(tarot.values()))
    card2 = random.choice(list(tarot.values()))
    card3 = random.choice(list(tarot.values()))
    now = datetime.now(KST).strftime("%m/%d %H:%M:%S")
    await asyncio.sleep(3)
    await ctx.send(f'{now}에 당신이 뽑은 타로 카드는 {card1}, {card2}, {card3} !')

@bot.command()
async def 양자택일(ctx):
    card1 = random.choice(list(tarot.values()))
    card2 = random.choice(list(tarot.values()))
    now = datetime.now(KST).strftime("%m/%d %H:%M:%S")
    await asyncio.sleep(3)
    await ctx.send(f'{now}에 당신이 뽑은 타로 카드는 {card1} 그리고 {card2} !')


@bot.command()
async def 심볼론(ctx):
    choice_symbolon = random.choice(list(symbolon.values()))
    now = datetime.now(KST).strftime("%m/%d %H:%M:%S")
    await asyncio.sleep(3)
    await ctx.send(f'{now}에 당신이 뽑은 심볼론 카드는 {choice_symbolon} !')


load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    raise RuntimeError("DISCORD_TOKEN이 설정되지 않았습니다.")


bot.run(TOKEN)