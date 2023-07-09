import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "21748181")

API_HASH = os.environ.get("API_HASH", "b1d962414e186e0778911f3183feac33")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6371916295:AAHCF7nnlt7lBCfGucEzhZ4adLkvIEXG1lg") 

FORCE_SUB = os.environ.get("FORCE_SUB", "") 

DB_NAME = os.environ.get("DB_NAME","User_Data")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://rajbot:pass@cluster0.kgciulo.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "100"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/2acf37dd041dc8cae6fc2.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5651594253').split()]

PORT = os.environ.get("PORT", "8080")
