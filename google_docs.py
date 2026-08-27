
import requests
from urllib.parse import urlencode
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive.file",
]

def config(st):
    c = st.secrets.get("google_oauth", {})
    return {
        "client_id": c.get("client_id", ""),
        "client_secret": c.get("client_secret", ""),
        "redirect_uri": c.get("redirect_uri", ""),
    }

def configured(st):
    c = config(st)
    return all(c.values())

def auth_url(st):
    c = config(st)
    params = {
        "client_id": c["client_id"],
        "redirect_uri": c["redirect_uri"],
        "response_type": "code",
        "scope": " ".join(SCOPES),
        "access_type": "offline",
        "prompt": "consent",
    }
    return "https://accounts.google.com/o/oauth2/v2/auth?" + urlencode(params)

def exchange(st, code):
    c = config(st)
    r = requests.post("https://oauth2.googleapis.com/token", data={
        "code": code,
        "client_id": c["client_id"],
        "client_secret": c["client_secret"],
        "redirect_uri": c["redirect_uri"],
        "grant_type": "authorization_code",
    }, timeout=20)
    r.raise_for_status()
    return r.json()

def creds(st):
    t = st.session_state.get("google_token")
    if not t:
        return None
    c = config(st)
    return Credentials(
        token=t.get("access_token"),
        refresh_token=t.get("refresh_token"),
        token_uri="https://oauth2.googleapis.com/token",
        client_id=c["client_id"],
        client_secret=c["client_secret"],
        scopes=SCOPES,
    )

def create_doc(st, title, text):
    cr = creds(st)
    if not cr:
        raise RuntimeError("Google-kontot är inte anslutet.")
    docs = build("docs", "v1", credentials=cr, cache_discovery=False)
    doc = docs.documents().create(body={"title": title}).execute()
    doc_id = doc["documentId"]
    docs.documents().batchUpdate(
        documentId=doc_id,
        body={"requests": [{"insertText": {"location": {"index": 1}, "text": text}}]},
    ).execute()
    return doc_id
