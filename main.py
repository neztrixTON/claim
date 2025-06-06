#!/usr/bin/env python3
import time
import logging
from datetime import datetime
import requests

# Настройки логирования
LOGFILE = "claim.log"
logging.basicConfig(
    filename=LOGFILE,
    level=logging.INFO,
    format="%(asctime)s — %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# URL и заголовки для запроса
URL = "https://api.tonverse.app/galaxy/collect"
HEADERS = {
    "Accept": "*/*",
    "Accept-Language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
    "Origin": "https://app.tonverse.app",
    "Referer": "https://app.tonverse.app/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
    ),
    "X-Application-Version": "1.0.9",
    "X-Client-Time-Diff": "1749210249-0",
    "X-Requested-With": "XMLHttpRequest",
    # Обратите внимание на экранирование кавычек внутри строки
    "sec-ch-ua": '"Microsoft Edge";v="136", "Microsoft Edge WebView2";v="136", "Not.A/Brand";v="99", "Chromium";v="136"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}

# Данные запроса (имитирует --data-raw)
DATA = {
    "session": "fjCPO6U5BG8QiME1RCC146AC1SwIVUX2PCRCisAmtOZh4ZTj5s5_nZG0RrhnWRiLblUdXbBUqDmQp1HPLpXHsWMo7rQUQ5b3PSTzbkDMra_DbQ52qSUJ5e7cbjiAjgER"
}

def do_claim():
    try:
        response = requests.post(URL, headers=HEADERS, data=DATA, timeout=30)
        if response.status_code == 200:
            logging.info("Клейм выполнен успешно")
        else:
            logging.error(f"Клейм завершился с кодом {response.status_code}")
    except Exception as e:
        logging.error(f"Ошибка при выполнении клейма: {e}")

def main():
    while True:
        do_claim()
        # Ждём 30 минут (1800 секунд)
        time.sleep(1800)

if __name__ == "__main__":
    main()
