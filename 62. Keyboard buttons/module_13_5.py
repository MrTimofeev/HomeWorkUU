from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import asyncio
from aiogram import F
from os import getenv
import dotenv

# Загрузка виртуального окружения
dotenv.load_dotenv()
# получение токена
API_TOKEN = getenv("API_TOKEN")


dp = Dispatcher()
buttons_start = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Рассчитать"), KeyboardButton(text="Информация")]
    ],
    resize_keyboard=True
)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message(CommandStart())
async def command_start_handler(message: Message):

    await message.answer("Привет я бот помогающий твоему здоровью!", reply_markup=buttons_start)


@dp.message(F.text == "Информация")
async def set_age(message: Message):
    await message.answer('Это бот для подсчета суточной нормы кллорий, для работы нажмите кнопку "Рассчитать"')

@dp.message(F.text == "Рассчитать")
async def set_age(message: Message, state: FSMContext):
    await message.answer("Введите свой возраст:")
    await state.set_state(UserState.age)


@dp.message(UserState.age)
async def set_weight(message: Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await state.set_state(UserState.weight)


@dp.message(UserState.weight)
async def set_growth(message: Message, state: FSMContext):
    await state.update_data(weight=message.text)
    await message.answer("Введите свой вес:")
    await state.set_state(UserState.growth)


@dp.message(UserState.growth)
async def send_calories(message: Message, state: FSMContext):
    await state.update_data(growth=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # Упрощённая формула Миффлина-Сан Жеора для мужчин:
    # BMR = 10 * вес + 6.25 * рост - 5 * возраст + 5
    bmr = 10 * weight + 6.25 * growth - 5 * age + 5
    await message.answer(f"Ваша норма каллорий: {bmr}")

    # Завершение машины состояний
    await state.clear()


async def main() -> None:
    bot = Bot(token=API_TOKEN, default=DefaultBotProperties(
        parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
