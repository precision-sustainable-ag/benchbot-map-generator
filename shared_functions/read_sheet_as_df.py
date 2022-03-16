from __future__ import print_function

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import pandas as pd

from .generate_creds import generate_creds


def read_sheet_as_df(sheet_id, range):
    creds = generate_creds()

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=sheet_id,
                                    range=range).execute()
        values = result.get('values', [])

        df = pd.DataFrame(values[1:], columns=values[0])

        return df

    except HttpError as err:
        print(err)
