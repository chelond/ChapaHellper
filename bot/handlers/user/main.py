from bot.misc.env import TgKeys
import requests
from aiogram import Bot, Dispatcher, executor, types, utils

YANDEX_API_KEY = 'AQVNzFFRC8TTZEJpL1iJsWM_5RrVJgwM2gm3FFDe'
bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')

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

    @dp.message_handler(commands='file')
    async def file(message: types.Message):
        buttons = [
            [
                {"text": "Алехин", "callback_data": "OS"},
                {"text": "Терехин", "callback_data": "BD"},
                {"text": "ОАиП", "callback_data": "OAIP"}
            ]
        ]
        await message.answer(text='Выбери предмет/препода который хочешь найти', reply_markup={"inline_keyboard": buttons})

    @dp.callback_query_handler(text="OS")
    async def buttonOS_handler(call: types.CallbackQuery):
        document = open('bot/handlers/user/file/Sbornik_LR_po_OS_IB.doc', 'rb')
        await bot.send_document(call.message.chat.id, document=document, caption="Алехин")

    @dp.callback_query_handler(text="BD")
    async def button_bd_handler(call: types.CallbackQuery):
        media = types.MediaGroup()
        media.attach_document(types.InputFile('bot/handlers/user/file/TK_1.docx'), caption="ТК1")
        media.attach_document(types.InputFile('bot/handlers/user/file/TK_2.docx'), caption='ТК2')
        media.attach_document(types.InputFile('bot/handlers/user/file/TK__3.docx'), caption='ТК3')
        media.attach_document(types.InputFile('bot/handlers/user/file/TK_4.docx'), caption='ТК4')
        media.attach_document(types.InputFile('bot/handlers/user/file/TK_5.docx'), caption='ТК5')
        media.attach_document(types.InputFile('bot/handlers/user/file/TK_6.docx'), caption='ТК6')
        media.attach_document(types.InputFile('bot/handlers/user/file/TK_7.docx'), caption='ТК7')
        media.attach_document(types.InputFile('bot/handlers/user/file/TK_8.docx'), caption='ТК8')
        media.attach_document(types.InputFile('bot/handlers/user/file/TK_9.docx'), caption='ТК9')

        await bot.send_media_group(call.message.chat.id, media=media)

    @dp.callback_query_handler(text="OAIP")
    async def button_oaip_handler(call: types.CallbackQuery):
        document = open('bot/handlers/user/file/Сборник_практических_занятий_ОАиП_28_48.pdf', 'rb')
        await bot.send_document(call.message.chat.id, document=document, caption="Лабы C#")

    @dp.message_handler(commands='mehebek')
    async def mehebek(message: types.Message):
        photo_path = 'bot/handlers/user/file/photo_2024-05-01_16-26-49.jpg'  # Укажите путь к файлу на вашем компьютере
        await message.answer_photo(types.InputFile(photo_path), caption='Всем хорошего мэхэбэка!')







