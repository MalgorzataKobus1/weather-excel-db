from services.openweather_api import fetch_weather #wywoluje z innego pliku funkcje ktora stworzylam
from services.excel_file import save_to_excel, read_excel_file
from config import Config
import time
from services.dashboard import  create_plots

while True:
    weather = fetch_weather()
    save_to_excel(weather)
    #weather_data = read_excel_file(Config.XLSX_PATH)
    weather_data = read_excel_file('./services/pogoda_rozszerzona.xlsx.')
    #line_chart(weather_data,"Lisbon")
    create_plots(weather_data)
    print("pobrałem dane")

    time.sleep(1000)

