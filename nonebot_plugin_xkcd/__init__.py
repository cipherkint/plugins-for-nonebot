from nonebot import get_driver
from nonebot.plugin import on_keyword
from .config import Config
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.adapters.onebot.v11 import Message, MessageSegment
import httpx
import json

import random

global_config = get_driver().config
config = Config.parse_obj(global_config)

kt = on_keyword(['/今日xkcd'])


def get_a_random():
    n = random.randint(1, 2793)
    return n


@kt.handle()
async def kt_handle(bot: Bot, event: Event):
    msg = await get_pic()
    await kt.finish(MessageSegment.image(msg))


async def get_pic():
    n = get_a_random()
    url = "https://xkcd.com/" + str(n) + "/info.0.json"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        get_dic = json.loads(resp.text)
    data = get_dic["img"]
    return data

