from config import sheet_service
import os


def getSheet():
    sheetId="11UwCmk_Curae-IG0-ypej1M4IZ9YOAwX7DeIRmGD6Os"
    print(sheetId)
    sheetRange="Form Responses 1!C1:O100"
    result = sheet_service.spreadsheets().values().get(spreadsheetId=sheetId, range=sheetRange, majorDimension = "ROWS").execute()
    return result

def updateSheet():
    sheetId="11clHWJ2VwoKArVuNb3ZCbjNqIB1aDRlQjDA2nJvOStg"
    sheetRange="Sheet1!B1:O100"
    spaceAfter=100
    result=getSheet()
    result=result['values']
    manush=len(result)
    ret=[]
    for i in range(manush):
        tmp=[]
        for j in range(len(result[i])):
            if (result[0][j]=='Team Name' or result[0][j]=='Email Address'):
                tmp.append(result[i][j])
        ret.append(tmp)
        if i!=0 and i%spaceAfter==0:
            ret.append(['','','',''])
            ret.append(['','','',''])
    body={
        "values": ret
    }
    response=sheet_service.spreadsheets().values().update(
    spreadsheetId=sheetId, range=sheetRange,
    valueInputOption='USER_ENTERED', body=body).execute()
    print(response)

updateSheet()

