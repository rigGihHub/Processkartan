import requests
from urllib.parse import urlencode
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
]

def config(st):
    c = st.secrets.get("google_oauth", {})
    return {"client_id": c.get("client_id",""), "client_secret": c.get("client_secret",""), "redirect_uri": c.get("redirect_uri","")}

def configured(st):
    return all(config(st).values())

def auth_url(st):
    c=config(st)
    return "https://accounts.google.com/o/oauth2/v2/auth?" + urlencode({
        "client_id":c["client_id"],"redirect_uri":c["redirect_uri"],"response_type":"code",
        "scope":" ".join(SCOPES),"access_type":"offline","prompt":"consent","include_granted_scopes":"true"
    })

def exchange(st, code):
    c=config(st)
    r=requests.post("https://oauth2.googleapis.com/token",data={
        "code":code,"client_id":c["client_id"],"client_secret":c["client_secret"],
        "redirect_uri":c["redirect_uri"],"grant_type":"authorization_code"
    },timeout=20)
    r.raise_for_status()
    return r.json()

def creds(st):
    t=st.session_state.get("google_token")
    if not t:return None
    c=config(st)
    return Credentials(token=t.get("access_token"),refresh_token=t.get("refresh_token"),
        token_uri="https://oauth2.googleapis.com/token",client_id=c["client_id"],client_secret=c["client_secret"],scopes=SCOPES)

def create_doc(st,title,text):
    cr=creds(st)
    if not cr: raise RuntimeError("Google-kontot är inte anslutet.")
    docs=build("docs","v1",credentials=cr,cache_discovery=False)
    doc=docs.documents().create(body={"title":title}).execute()
    did=doc["documentId"]
    docs.documents().batchUpdate(documentId=did,body={"requests":[{"insertText":{"location":{"index":1},"text":text}}]}).execute()
    return did

def create_sheet(st,title,step_rows,link_rows):
    cr=creds(st)
    if not cr: raise RuntimeError("Google-kontot är inte anslutet.")
    sheets=build("sheets","v4",credentials=cr,cache_discovery=False)
    res=sheets.spreadsheets().create(body={"properties":{"title":title},"sheets":[{"properties":{"title":"Processsteg"}},{"properties":{"title":"Kopplingar"}}]},fields="spreadsheetId,spreadsheetUrl").execute()
    sid=res["spreadsheetId"]
    steps=["Ordning","ID","Typ","Text","Dokumentlänk","Inputs","Outputs","Nästa steg","Föregående steg","X","Y","Bredd","Höjd"]
    links=["Från ID","Från steg","Till ID","Till steg","Anslutning"]
    sheets.spreadsheets().values().batchUpdate(spreadsheetId=sid,body={"valueInputOption":"RAW","data":[
        {"range":"Processsteg!A1","majorDimension":"ROWS","values":[steps]+step_rows},
        {"range":"Kopplingar!A1","majorDimension":"ROWS","values":[links]+link_rows}
    ]}).execute()
    meta=sheets.spreadsheets().get(spreadsheetId=sid,fields="sheets(properties(sheetId,title))").execute()
    ids={x["properties"]["title"]:x["properties"]["sheetId"] for x in meta["sheets"]}
    req=[]
    for nm,endcol in [("Processsteg",13),("Kopplingar",5)]:
        sh=ids[nm]
        req.append({
            "repeatCell":{
                "range":{"sheetId":sh,"startRowIndex":0,"endRowIndex":1,"startColumnIndex":0,"endColumnIndex":endcol},
                "cell":{"userEnteredFormat":{
                    "backgroundColor":{"red":0.122,"green":0.435,"blue":0.333},
                    "textFormat":{"bold":True,"foregroundColor":{"red":1,"green":1,"blue":1}}
                }},
                "fields":"userEnteredFormat(backgroundColor,textFormat)"
            }
        })
        req.append({
            "updateSheetProperties":{
                "properties":{"sheetId":sh,"gridProperties":{"frozenRowCount":1}},
                "fields":"gridProperties.frozenRowCount"
            }
        })
        req.append({
            "setBasicFilter":{
                "filter":{"range":{
                    "sheetId":sh,
                    "startRowIndex":0,
                    "startColumnIndex":0,
                    "endColumnIndex":endcol
                }}
            }
        })
        req.append({
            "autoResizeDimensions":{
                "dimensions":{
                    "sheetId":sh,
                    "dimension":"COLUMNS",
                    "startIndex":0,
                    "endIndex":endcol
                }
            }
        })
    sheets.spreadsheets().batchUpdate(spreadsheetId=sid,body={"requests":req}).execute()
    return sid, res.get("spreadsheetUrl") or f"https://docs.google.com/spreadsheets/d/{sid}/edit"
