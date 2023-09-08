from functools import wraps

def user_is_chat_member(bot):

    def user_request_wrapper(func):
        @wraps(func)
        async def wrapper(event):
            participants = await bot.get_participants(-1001718737807)
            user = event.peer_id.user_id
            if not any([user == participant.id for participant in participants]):
                if func.__name__ == 'request':
                    print(user, 'not authorized')
                    await event.respond(
                        'Перш ніж почати роботу з ботом зайди в чат клану: https://t.me/+L24NI_OBP_I1MDBi'
                    )
                return
            else:
                return await func(event)
        return wrapper
    return user_request_wrapper

