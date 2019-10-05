import asyncio

import discord
import openpyxl
import datetime

from discord import Embed
from openpyxl.comments import author

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("디스코드봇")
    await client.change_presence(status=discord.Status.online, activity=game)


    @client.event
    async def on_message(message):
        if message.content.startswith("!파엠서버"):
            await message.channel.send("https://discord.gg/NqwRaK5")
        if message.content.startswith("!노래 명령어"):
            await message.channel.send("!play"
                                        "!skip"
                                         "!stop")
        if message.content.startswith("!사진 명령어"):
            await message.channel.send("!사진 파일이름.jpg")
        if message.content.startswith("!사진"):
            pic = message.content.split(" ")[1]
            await message.channel.send(file=discord.File(pic))
        if message.content.startswith("!경고 명령어"):
            await message.channel.send("!경고 ID")
        if message.content.startswith("!채널메시지 명령어"):
            await message.channel.send("!채널메시지 ID 할말")
        if message.content.startswith("!채널메시지"):
            channel = message.content[7:25]
            msg = message.content[26:]
            await client.get_channel(int(channel)).send(msg)
        if message.content.startswith("!경고"):
            author = message.guild.get_member(int(message.content [4:22]))
            file = openpyxl.load_workbook("경고.xlsx")
            sheet = file.active
            i = 1
            while True:
                if sheet["A" + str(i)].value == str(author.id):
                    sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                    file.save("경고.xlsx")
                    if sheet["B" + str(i)].value == 2:
                        await message.guild.ban(author)
                        await message.channel.send("경고 2회 누적입니다. 서버에서 추방됩니다.")
                    else:
                        await message.channel.send("경고를 1회 받았습니다.")
                    break
                if sheet["A" + str(i)].value ==None:
                    sheet["A" + str(i)].value = str(author.id)
                    sheet["B" + str(i)].value = 1
                    file.save("경고.xlsx")
                    await message.channel.send("경고를 1회 받았습니다.")
                    break
                i += 1

@client.event
async def on_message(message):
    if message.content.startswith("!정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="이름", value=message.author.name, inline=True)
        embed.add_field(name="서버닉네임", value=message.author.display_name, inline=True)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=True)
        embed.add_field(name="아이디", value=message.author.id, inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        await message.channel.send(embed=embed)

@client.event
async def on_message(message):
    if message.content.startswith("!서버"):
        list = []
        for server in client.servers:
            list.append(server.name)
        await client.send_message(message.channel , '\n'.join(list))

    if message.content.startswith("!시간"):
        a = datetime.datetime.today().year
        b = datetime.datetime.today().month
        c = datetime.datetime.today().day
        d = datetime.datetime.today().hour
        e = datetime.datetime.today().minute
        await client.send_message(message.channel, str(a) + "년 " +str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 입니다.")








client.run('NjI5NjQ5NTAxNzQ0OTIyNjQ3.XZc05w.2Qv3wVZI3G1DVudRejZs99H0tFU')
