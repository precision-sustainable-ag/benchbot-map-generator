import pandas as pd

from shared_functions.read_sheet_as_df import read_sheet_as_df

species_by_row_sheets_key = '1lFJAUB-NKeRJ3U0ZaQpUJDIxpp06S5HR5xS8JZuXFdQ'
species_by_row_sheets_range = 'A:B'
pictures_per_species_sheets_key = '11Pv_lzHuVwqJi83T8BJ_vmf_kwFnDysNmLpQAVCOMPE'
pictures_per_species_sheets_range = 'A:C'

species_by_row = read_sheet_as_df(
    species_by_row_sheets_key, species_by_row_sheets_range)
species_by_row = species_by_row.assign(
    Rows=species_by_row['Rows'].str.split(',')).explode('Rows')
species_by_row = species_by_row.set_index('Rows')

pictures_per_species = read_sheet_as_df(
    pictures_per_species_sheets_key, pictures_per_species_sheets_range)
# pictures_per_species['Species'] = pictures_per_species.set_index('Species')

map_obj = {
    'row': [],
    'pictures_per_row': [],
}

print(species_by_row)
print(pictures_per_species)
# print(pictures_per_species)

for index, row in species_by_row.iterrows():
    # print(
    #     pictures_per_species[pictures_per_species.Species == row.Species].tail(1))
    # print(row['Rows'], row['Species'])
    # print(pictures_per_species['Species'])
    # print(row['Species'])
    number_of_pics = pictures_per_species[pictures_per_species.Species == row.Species].tail(
        1).reset_index()

    # print((number_of_pics))
    # print((number_of_pics['Pictures Per Row'][0]))
    # print(len(number_of_pics[0]))
    # print(type(number_of_pics))
    # print(number_of_pics[len(number_of_pics)-1])

    map_obj['row'].append(index)
    map_obj['pictures_per_row'].append(number_of_pics['Pictures Per Row'][0])

map_df = pd.DataFrame(map_obj)
map_df.to_csv("map.csv", index=False)
