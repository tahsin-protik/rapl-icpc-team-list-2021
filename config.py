import os, json
from googleapiclient.discovery import build
from google.oauth2 import service_account

SERVICE_ACCOUNT = None

with open("creds.json", "r") as file:
    SERVICE_ACCOUNT = json.loads(file.read())

# print(SERVICE_ACCOUNT)

SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

creds = service_account.Credentials.from_service_account_info(
    SERVICE_ACCOUNT, scopes=SCOPES)

# print(creds)

drive_service = build('drive', 'v3', credentials=creds)
sheet_service = build('sheets', 'v4', credentials=creds)
