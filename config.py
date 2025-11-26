import dotenv
import os
dotenv.load_dotenv()


class Config:
    QUERY = os.getenv("QUERY")
    API_KEY = os.getenv("API_KEY")
    XLSX_PATH = "pogoda.xlsx"
