import os
import sys
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request


def create_service(SCOPES=str, API_NAME=str, API_VERSION=str, OAuthPath=str):
    """
    OAuth 2.0 Scopes for Google APIs + API Version:
        - https://developers.google.com/identity/protocols/oauth2/scopes

    Google APIs Explorer:
        - https://developers.google.com/apis-explorer

    OAuthPath:
        - Specify the path to OAuth 2.0 Client IDs file.

    Examle:
         - google('https://www.googleapis.com/auth/spreadsheets', 'sheets', 'v4', 'C:\\Users\\user_name\\Documents\\cred\\OAuth.json')

    ** pickle file will be created with api name 
    after authentication in the same folder as OAuth credentials
    """
    cred = None
    credPath = os.path.join(os.path.dirname(OAuthPath), f'{API_NAME}.pickle')

    if os.path.exists(credPath):
        with open(credPath, 'rb') as token:
            cred = pickle.load(token)
    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(OAuthPath, [SCOPES])
            cred = flow.run_local_server()
        with open(credPath, 'wb') as token:
            pickle.dump(cred, token)
    try:
        service = build(API_NAME, API_VERSION, credentials=cred)
        return service
    except Exception as error:
        print(f'An error occurred: {error}')