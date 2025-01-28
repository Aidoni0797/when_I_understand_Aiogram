import openai
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

# Установи свои API-ключи
openai.api_key = '...'
TOKEN = '...'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# Обработчик сообщений
@dp.message_handler()
async def handle_message(message: types.Message):
    user_message = message.text

    try:
        # Отправляем запрос в OpenAI API с использованием ChatCompletion
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Выбираем актуальную модель
            messages=[
                {"role": "system", "content": "Ты - полезный бот, который отвечает на вопросы."},
                {"role": "user", "content": user_message},
            ],
            max_tokens=150,
            temperature=0.7,
        )

        # Получаем ответ от OpenAI
        bot_reply = response['choices'][0]['message']['content'].strip()

        # Отправляем ответ пользователю
        await message.reply(bot_reply, parse_mode=ParseMode.MARKDOWN)

    except Exception as e:
        # Обработка ошибок
        await message.reply("Произошла ошибка: " + str(e))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
