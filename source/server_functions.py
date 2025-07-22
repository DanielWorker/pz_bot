import os
import time

from config import LOG_PATH, SCREEN_NAME, SERVER_NAME


def start_message():
    return ("Hello gamers, вот доступные команды:\n"
            "/start_server - запустить с сервер\n"
            "/stop - выключить сервер (/save тоже выполняется)\n"
            "/save - сохранить сервер (на всякий случай)\n"
            "/status - узнать статус сервера")


def start_server():
    is_running = os.popen(f'screen -ls | grep {SCREEN_NAME}').read()
    if is_running:
        return '⚠️ Сервер уже запущен или запускается'

    os.system(f'screen -dmS {SCREEN_NAME} bash -lc "cd ~/pzserver && ./start-server.sh -servername {SERVER_NAME}"')
    return '🚀 Сервер запускается...'


def save_server():
    is_running = os.popen(f'screen -ls | grep {SCREEN_NAME}').read()
    if not is_running:
        return '🔴 Сервер уже выключен'

    os.system(f'screen -S {SCREEN_NAME} -p 0 -X stuff "save\\n"')
    return '💾 Сервер сохранён'


def stop_server():
    is_running = os.popen(f'screen -ls | grep {SCREEN_NAME}').read()
    if not is_running:
        return '🔴 Сервер уже выключен'

    os.system(f'screen -S {SCREEN_NAME} -p 0 -X stuff "save\\n"')
    time.sleep(3)

    os.system(f'screen -S {SCREEN_NAME} -p 0 -X stuff "quit\\n"')
    return '🛑 Сервер остановлен'


# ====================== #

def get_server_status():
    # Проверка: есть ли screen
    screen_output = os.popen(f'screen -ls | grep {SCREEN_NAME}').read()
    if not screen_output:
        return '🔴 Сервер выключен'
    else:
        return '🟢 Сервер запущен'
