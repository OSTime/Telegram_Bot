from bot import telegram_chatbot
import gamble
import gizoogle
import profiles

bot = telegram_chatbot("config.cfg")

#intializes everyone's points
profile_dict = profiles.restart_points()

def make_reply(msg, name):
    reply = ''
    if msg is not None:
        reply = ''
        if '!' in msg:
            reply = bot.read_command(msg, name, profile_dict)
    return reply

update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            name = item["message"]["from"]["first_name"]
            reply = make_reply(message, name)
            bot.send_message(reply, from_)