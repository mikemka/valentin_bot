import aiogram.types
import aiogram.utils.deep_linking
import bot
import dispatcher
import filters


@dispatcher.dp.message_handler(filters.UserStatus('send_to^'))
async def send_message_to(message: aiogram.types.Message) -> None:
    await message.answer(bot.user_status[message.from_user.id])
    try:
        await message.bot.send_message(
            bot.user_status[message.from_user.id].split('^')[1],
            f'У вас новое анонимное признание:\n\n<b>{message.text}</b>'
        )
        await message.answer(
            '<b>Готово, твое сообщение отправлено!</b>\n'
            '\n'
            '📌 Начни получать анонимные признания от своих знакомых прямо сейчас! Вот твоя ссылка:\n'
            '\n'
            f'{await aiogram.utils.deep_linking.get_start_link(message.from_user.id)}'
        )
    except:
        await message.answer(
            '<b>Произошла ошибка!</b>\n'
            '\n'
            'Не удалось отправить сообщение. Возможно, пользователь заблокировал бота.'
        )
    bot.user_status[message.from_user.id] = '^'


@dispatcher.dp.message_handler()
async def start_command(message: aiogram.types.Message) -> None:
    _args = message.get_args()
    if not _args:
        return await message.answer(
            f'<b>Привет! Вот твоя ссылка:</b>\n'
            '\n'
            f'{await aiogram.utils.deep_linking.get_start_link(message.from_user.id)}\n'
            '\n'
            '📌 Начни получать анонимные признания от своих знакомых прямо сейчас! Размести персональную ссылку в '
            'соцсетях!'
        )
    bot.user_status[message.from_user.id] = f'send_to^{_args}'
    await message.answer(
        '✨ Здесь ты можешь анонимно рассказать о своих чувствах к человеку, который опубликовал эту ссылку.\n'
        '\n'
        'Напиши сюда всё, что о нем думаешь в одном сообщении и через несколько мгновений он его получит, но '
        'не будет знать от кого оно.\n'
        '\n'
        '<b>📌 Для того чтобы получить свою личную ссылку - сначала напиши что нибудь!</b>'
    )