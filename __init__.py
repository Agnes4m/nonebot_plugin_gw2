from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message,Bot, Event  # 这两个没用的别删
from .api import activity , daily,zixuns


daily_to=on_command('gw2日常',priority=10)
huodong=on_command('gw2活动',priority=20)
zixun=on_command('gw2资讯',priority=30)


@daily_to.handle()
async def _():
    data = await daily('today')
    await daily_to.finish(data)


@huodong.handle()
async def huodong_():
    data = await activity()
    await huodong.finish(data)


@zixun.handle()
async def _():
    data = await zixuns()
    await zixun.finish(data)


