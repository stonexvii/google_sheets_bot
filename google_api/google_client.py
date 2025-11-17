from __future__ import print_function

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

import config
import misc
from classes import UserAnswers


class GoogleAPI:
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    CLIENT = None

    def __new__(cls, *args, **kwargs):
        if cls.CLIENT is None:
            cls.CLIENT = super().__new__(cls)
        return cls.CLIENT

    def __init__(self):
        self._spreadsheet_id = config.SPREADSHEET_ID
        self._range = config.RANGE_NAME
        self._client = self._create_client()
        self._sheet_id = self._get_sheet_id()

    def _create_client(self):
        creds = Credentials.from_authorized_user_file("token.json", self.SCOPES)
        service = build("sheets", "v4", credentials=creds)
        return service

    def _get_sheet_id(self):
        metadata = self._client.spreadsheets().get(spreadsheetId=self._spreadsheet_id).execute()
        for sheet in metadata["sheets"]:
            if sheet["properties"]["title"] == config.RANGE_NAME:
                return sheet["properties"]["sheetId"]

    def request_values(self):
        sheet = self._client.spreadsheets()
        result = sheet.values().get(
            spreadsheetId=self._spreadsheet_id,
            range=self._range,
        ).execute()
        return result

    def get_headers(self):
        result = self.request_values()
        values = result.get("values", [])
        config.HEADERS = values[0][3:]
        misc.print_message('Заголовки обновлены!')

    def get_answers(self):
        result = self.request_values()
        values = result.get("values", [])
        if len(values) > 1:
            return [UserAnswers(entry) for entry in values[1:]]

    def delete_answers(self, idx: int):
        request = {
            "requests": [
                {
                    "deleteDimension": {
                        "range": {
                            "sheetId": self._sheet_id,
                            "dimension": "ROWS",
                            "startIndex": idx + 1,
                            "endIndex": idx + 2,
                        }
                    }
                }
            ]
        }

        self._client.spreadsheets().batchUpdate(
            spreadsheetId=self._spreadsheet_id,
            body=request
        ).execute()
