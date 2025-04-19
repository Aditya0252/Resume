import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_form_data(option: int):
    sheet_ids = {
        1: "sheet_id_for_avg",
        2: "sheet_id_for_good",
        3: "sheet_id_for_industry"
    }
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_key(sheet_ids[option]).sheet1
    records = sheet.get_all_records()
    return records[-1]  # latest response
