import httpx
import asyncio
try:
    import ujson as json
except:
    import json

async def get_json(mode):
    if mode=='today':
        url = 'https://gw2.wishingstarmoye.com/gw2api/daily'
    elif mode == 'tom':
        url = 'https://gw2.wishingstarmoye.com/gw2api/daily/tomorrow'
    elif mode == 'activity':
        url = 'https://gw2.wishingstarmoye.com/gw2api/activity'
    elif mode == 'news':
        url = 'https://gw2.wishingstarmoye.com/gw2api/news'
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0',
    }
    data:dict = json.loads(httpx.get(url=url,headers=headers).text)
    return data

async def daily(day:str):
    # 日常
    data = await get_json(day)
    date = data['date']
    data_pve = data['pve']
    data_pvp = data['pvp']
    data_wvw = data['wvw']
    data_fac = data['fractals']


    msg:str = '[+] 游戏每日日常\n'
    msg = msg + '[-] PvE\n'
    for pve in data_pve:
     msg = msg + pve['zh'] + '  '
    msg = msg.strip('  ') + '\n'
    msg = msg + '[-] PvP\n'
    for pvp in data_pvp:
     msg = msg + pvp['zh'] + '  '
    msg = msg.strip('  ') + '\n'
    msg = msg + '[-] WvW\n'
    for wvw in data_wvw:
        msg = msg + wvw['zh'] + '  '
    msg = msg.strip('  ') + '\n'
    msg = msg + '[-] 碎层\n'
    msg_tuijian = '推荐：'
    msg_4ji = '4级：'
    for fac in data_fac:
        if '推荐' in fac['zh']:
            msg_tuijian = msg_tuijian + fac['zh'][9:] + '  '
        elif '4级' in fac['zh']:
            msg_4ji = msg_4ji + fac['zh'][:-2] + '  '
    msg = msg + msg_tuijian.strip('') + '\n' + msg_4ji.strip('')
    msg = "当前时间为"+ date+'\n'+msg
    print(msg)
    return msg

async def activity():
    # 活动
    data = await get_json('activity')
    activitys = data['activitys']
    disactivitys = data['disactivitys']
    msg:str = '[+] 当前可参与活动或公告\n'
    for act in activitys:
        msg = msg + "[" + act['public_date'] + "] " + act['title'] + "\n" + act['url'] + "\n"
    msg = msg + '[x] 最近已失效活动或公告\n'
    for act in disactivitys:
        msg = msg + "[已失效] " + act['title'] + "\n" + act['url'] + "\n"
    msg = msg.strip('\n')
    return msg

async def zixuns():
    # 咨询
    json_data = await get_json('news')
    msg1:str = '[+] 第三方资讯，包括小邋遢、明眸游戏、和风议会(NGA)\n'
    for act in json_data:
        msg1 = msg1 + "[" + act['date'] + "] " + act['title'] + "\n" + act['url'] + '数据来源'+act['type'] + "\n"
    msg1 = msg1.strip('\n')
    print(msg1)
    return msg1

if __name__ == '__main__':
    # asyncio.run(daily('tom'))
    asyncio.run(zixuns())