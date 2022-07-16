from googleapiclient.discovery import build
from google.oauth2 import service_account


# To give permissions
SERVICE_ACCOUNT_FILE = 'keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


# The ID
SAMPLE_SPREADSHEET_ID = '1xUq2H4eQiBW_U3NOysJWLsuIBFHwKqm3TzERjfTogyo'
service = build('sheets', 'v4', credentials=creds)


# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                        range="Sheet1!A2:G1216").execute()


values = result.get('values', [])

def listoftuples(values):
        final = []
        tem = []
        a = 1
        for i in values:
                for J in i:
                        if a!=1 and a!=7 and a!=6:
                                J = float(J)
                        if a==6:
                                J=int(J)
                        tem.append(J)
                        a = a + 1
                final.append(tuple(tem))
                tem=[]
                a=1       
        return final
final = listoftuples(values)


 


