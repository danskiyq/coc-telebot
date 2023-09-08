import os

from telethon import TelegramClient, events
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from const import COC_TO_TELEGRAM_MAPPING
from decorator import user_is_chat_member

token = os.environ.get('BOT_TOKEN', '')
bot = TelegramClient('ybot', 16734569, '8c137eecf2abd641f472740daf3ab0fa').start(bot_token=token)
rights = ChatAdminRights(
    invite_users=True,
)
print('Bot hosting now')


@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('Привіт, це бот клана yardan!')


@bot.on(events.NewMessage())
@user_is_chat_member(bot)
async def request(event):
    print(event.peer_id.user_id, 'authorised')


@bot.on(events.NewMessage(pattern='/setnick'))
@user_is_chat_member(bot)
async def set_nick(event):
    nick = event.message.message[9:]
    if nick:
        print(event.peer_id.user_id, 'nick change', nick)
        channel = await bot.get_entity(-1001718737807)
        # get rights of user and set to default if not admin else keep the same
        current_rights = await bot.get_permissions(channel, event.peer_id.user_id)
        if not current_rights.is_admin:
            rights_to_use = rights
        else:
            rights_to_use = current_rights.participant.admin_rights

        await bot(EditAdminRequest(channel=channel,
                                   user_id=event.peer_id.user_id,
                                   admin_rights=rights_to_use,
                                   rank=nick))
        await event.respond('тепер твій нік - {}'.format(nick))
    else:
        await event.respond('Трохи не так) укажи свій нік в форматі:\n/setnick твій нік')


@bot.on(events.NewMessage(pattern='/getmembers', from_users='danskiyq'))
async def get_members(event):
    participants = await bot.get_participants(-1001718737807)

    await event.respond('\n'.join(
        f"{participant.username}: {participant.participant.rank if hasattr(participant.participant, 'rank') else ''}"
        for participant in participants))


@bot.on(events.NewMessage(pattern='/getmembernick'))
async def get_member_nick(event):
    message = event.message.message
    nick = message[len('/getmembernick') + 1:]
    if nick:
        if nick in COC_TO_TELEGRAM_MAPPING:
            await event.respond(
                f"У людини з ніком: {nick} в клані,\nнік в телеграмі це: @{COC_TO_TELEGRAM_MAPPING[nick]}")
            return
        await event.respond(f"Нік {nick} не знайдено")
    else:
        await event.respond('Трохи не так) укажи нік в форматі:\n/getmembernick нік')



@bot.on(events.NewMessage(pattern='/ping', from_users='danskiyq'))
async def ping(event):
    await event.respond('pong')

if __name__ == '__main__':
    bot.run_until_disconnected()
