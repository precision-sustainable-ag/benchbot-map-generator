import pandas as pd

from shared_functions.read_sheet_as_df import read_sheet_as_df


def generate_map(species_by_row_sheets_key, pictures_per_species_sheets_key):
    species_by_row_sheets_range = 'A:B'
    pictures_per_species_sheets_range = 'A:C'

    species_by_row = read_sheet_as_df(
        species_by_row_sheets_key, species_by_row_sheets_range)
    species_by_row = species_by_row.assign(
        Rows=species_by_row['Rows'].str.split(',')).explode('Rows')
    species_by_row = species_by_row.set_index('Rows')

    pictures_per_species = read_sheet_as_df(
        pictures_per_species_sheets_key, pictures_per_species_sheets_range)

    map_obj = {
        'row': [],
        'pictures_per_row': [],
    }

    for index, row in species_by_row.iterrows():
        number_of_pics = pictures_per_species[pictures_per_species.Species == row.Species].tail(
            1).reset_index()
        map_obj['row'].append(index)
        map_obj['pictures_per_row'].append(
            number_of_pics['Pictures Per Row'][0])

    map_df = pd.DataFrame(map_obj)
    map_df.to_csv("map.csv", index=False)


generate_map('1lFJAUB-NKeRJ3U0ZaQpUJDIxpp06S5HR5xS8JZuXFdQ',
             '11Pv_lzHuVwqJi83T8BJ_vmf_kwFnDysNmLpQAVCOMPE')
