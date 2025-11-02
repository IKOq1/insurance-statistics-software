import asyncio
import logging
import os
import sys
from aiogram import Bot, Dispatcher, types, F, Router
from pathlib import Path
from aiogram.filters.command import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.types import FSInputFile
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import  FSMContext

sys.path.append (str(Path(__file__).parent.parent.parent))
from DbTg.dbAsync import save_information

import app.keyboards as kb

class daTa(StatesGroup):
    TypeS = State()
    TypeS_id = State()
    object = State()
    sCount = State()
    sCaseCount = State()
    year = State()


router = Router()


meow = "https://i.gifer.com/nRq.gif" #1ая гифка
meow2 = 'https://i.gifer.com/av.gif' #2ая гифка






@router.message(CommandStart())                                                          #start
async def cmd_start(message: Message):
    await message.answer(f"""
        \nПривет, {message.from_user.first_name},
        \n🦹Это бот🦹 
        \n🦸который поможет тебе заполнить🦸
        \n📟базу данных по страхованию📟
        \n🎆Нажми на /help и мы начнем!🎆
        """)
    
@router.callback_query(F.data == 'Помощь')
async def help_hand(callback: CallbackQuery, bot: Bot):
    await callback.answer()
    


    await bot.send_animation(
        chat_id= callback.message.chat.id,
        animation = meow2,
        caption="""
        \n😤Смотри, тут все просто✅
        \n▶️Посмотри вниз или нажми /help▶️
        \n🫷И по кнопки <b>Добавить</b>🫸
        \n☝️Ты сможешь <b>ввести</b> данные для БД☝️
        """,
        parse_mode='HTML',
        show_caption_above_media=False,
        reply_markup=kb.settings)

@router.message(Command('help'))                                                          #help
async def get_help(message: Message):
    await message.answer_animation(        
        meow,
        caption=f"""
        Внизу находяться кнопки🔔
        \nНажимай на них чтобы получить отклик⏱️
        """,
        show_caption_above_media = False,
        reply_markup=kb.settings
    )


@router.callback_query(F.data =='Добавить')                                                          #daTa
async def add(callback: CallbackQuery): 
    await callback.answer('')
    await callback.message.edit_caption(text="Йоу", reply_markup=await kb.inline_TypeS())




temp_storage = {} #МОЛЮ, ЗАПОМНИ ЭТУ СВЯТЫНЮ , КОТОРАЯ СПАСЛА ТЕБЯ ПОСЛЕ ДВУХ ЧАСОВ БЕЗУСПЕШНОЙ ОТКЛАДКИ







@router.callback_query(F.data.in_([
    'Личное страхование',
    'Имущественное страхование',
    'Страхование ответственности'
    ]))
async def process_insurance_type(callback:CallbackQuery, state:FSMContext, bot:Bot):
    
    #new way
    user_id = callback.from_user.id
    temp_storage[user_id] = {'edit_message_id':callback.message.message_id}

    type_mapping = {
    'Личное страхование': 2,
    'Имущественное страхование': 1,
    'Страхование ответственности': 3
    }


    await callback.answer('')
    await state.update_data(TypeS = callback.data,
                            TypeS_id= type_mapping[callback.data])
    await state.set_state(daTa.object)
    


    #gifka
    await callback.message.edit_caption(
        caption=f'Введите объект страхования',
        show_caption_above_media=False
    )


#ПЕРЕХОД


@router.message(daTa.object)
async def object(message: Message, state: FSMContext, bot: Bot):
    user_id = message.from_user.id
    edit_message_id = temp_storage [user_id]['edit_message_id']
    
    
    await state.update_data(object = message.text)
    await state.set_state(daTa.sCount)
    
    
    await bot.edit_message_caption(
        chat_id=message.chat.id,
        message_id=edit_message_id,
        caption=f'Введите количеcтво договоров',
        show_caption_above_media=False
    )


#ПЕРЕХОД 2 sCount



@router.message(daTa.sCount)
async def sCount(message:Message, state: FSMContext, bot: Bot):
    
    user_id = message.from_user.id
    edit_message_id = temp_storage [user_id]['edit_message_id']

    await state.update_data(sCount = message.text)
    await state.set_state(daTa.sCaseCount)

    await bot.edit_message_caption(
        chat_id=message.chat.id,
        message_id=edit_message_id,
        caption=f'Введите количество страховых случаев',                               
        show_caption_above_media=False
    )



#ПЕРЕХОД 3 sCaseCount



@router.message(daTa.sCaseCount)
async def sCaseCount(message: Message, state: FSMContext, bot: Bot):
    user_id = message.from_user.id
    edit_message_id = temp_storage [user_id]['edit_message_id']

    await state.update_data(sCaseCount = message.text)
    await state.set_state(daTa.year)

    await bot.edit_message_caption(
        chat_id=message.chat.id,
        message_id=edit_message_id,
        caption=f'Введите год',
        show_caption_above_media=False
    )   



@router.message(daTa.year)
async def year(message:Message, state: FSMContext, bot: Bot):
    await state.update_data(year=message.text)
    data = await state.get_data()
    user_id = message.from_user.id
    edit_message_id = temp_storage [user_id]['edit_message_id']


    try:
        success = await save_information(data)
        if not success:
            await message.answer('⚠️Произошла ошибка при сохранении данных⚠️')
    except Exception as e:
        logging.error(f'Error in work with DB {e}')
        await message.answer('⚠️Сервис временено недоступен⚠️' \
        '🙇‍♂️Приносим свои извиненния🙇‍♂️')


    result = (
        "Все данные получены" 
        f"\n<b>Тип страхования:</b> {data.get('TypeS', 'не указано')}"
        f"\n<b>Объект страхования:</b> {data.get('object', 'не указано')}"
        f"\n<b>Количество договоров:</b> {data.get('sCount', 'не указано')}"
        f"\n<b>Количество страховых случаев:</b> {data.get('sCaseCount', 'не указано')}"
        f"\n<b>год:</b> {data.get('year','не указано' )}"
    )



    await bot.edit_message_caption(
        chat_id=message.chat.id,
        message_id=edit_message_id, # Всё тот же ID
        caption=result,
        show_caption_above_media=False,
        parse_mode='HTML'
    )   
    del temp_storage[user_id]
    await state.clear()