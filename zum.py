import discord
from urllib.request import urlopen, Request
import urllib
import urllib.request
from bs4 import BeautifulSoup

token = '★봇토큰★'

client = discord.Client()

@client.event
async def on_connect():
    print('ready')

@client.event
async def on_message(message):
    if message.content == '!실검' or message.content == '!실시간검색어':
        url = 'http://issue.zum.com/'
        req = Request(url)
        html = urllib.request.urlopen(req)
        soup = BeautifulSoup(html, "html.parser")

        s = soup.find_all('div', {'class': 'cont'})

        rank = 1
        data = []
        for title in s:
            tt = title.find('span', {'class': 'word'}).text
            data.append(f'**{rank}**. {tt}')
            rank += 1
            if rank > 10:
                break

        dat = str(data)
        dat = dat.replace("'", "")
        dat = dat.replace(", ", "\n")
        dat = dat[1:-1]
        embed = discord.Embed(title='줌 실시간 검색어 순위', description=dat, colour=0x19CE60)
        await message.channel.send(embed=embed)

client.run(token)


