from services.openweather_api import fetch_weather #wywoluje z innego pliku funkcje ktora stworzylam
from services.excel_file import save_to_excel, read_excel_file
from config import Config
import time



while True:
    weather = fetch_weather()
    save_to_excel(weather)
    weather_data = read_excel_file(Config.XLSX_PATH)
    print("pobrałem dane")

    time.sleep(10)