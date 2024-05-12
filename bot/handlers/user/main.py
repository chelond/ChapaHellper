
import requests
from aiogram import Bot, Dispatcher, executor, types

YANDEX_API_KEY = 'AQVNzFFRC8TTZEJpL1iJsWM_5RrVJgwM2gm3FFDe'



def gpt(msg):
    # запрос в Yandex GPT по API
    resp = requests.post(
        url='https://llm.api.cloud.yandex.net/foundationModels/v1/completion',
        headers={
            "Authorization": "API-KEY AQVN3oMBCwOheZH3BHwiWWVO8z7mCnUxnhxI9Qx1",
            "x-folder-id": "b1ggsg88g772sbua0enr"
        },
        json={
            "modelUri": "gpt://b1ggsg88g772sbua0enr/yandexgpt-lite",
            "completionOptions": {
                "stream": False,
                "temperature": 0.6,
                "maxTokens": "10000"
            },
            "messages": [
                {
                    "role": "system",
                    "text": msg
                }
            ]
        }
    )

    # извлекаем ответ на запрос
    answer = resp.json()

    # извлекаем текст ответа от GPT из кучи данных ответа на запрос
    reply_txt = answer['result']['alternatives'][0]['message']['text']
    return reply_txt


def register_user_handlers(dp: Dispatcher):
    @dp.message_handler(commands='ai')
    async def echo(message: types.Message):
        yandex_response = gpt(message.text)
        await message.answer(yandex_response)


