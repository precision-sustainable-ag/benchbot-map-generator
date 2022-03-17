# benchbot_map_generator
**Introduction**

This document will go over using google sheets and a python script to generate a map excel file for the bench bot

**Prerequisites**

1. Python 3.9 installed 

    1. Instructions can be found here [How to Download and Install Python on Windows - Data to Fish](https://datatofish.com/install-python/)

2. A copy of credentials.json from @mikahpinegar

**Steps**

1. Create two google sheets files for your bench bot 
   1. species_by_row: this file details which rows are planted with what species. An example can be found here https://docs.google.com/spreadsheets/d/1lFJAUB-NKeRJ3U0ZaQpUJDIxpp06S5HR5xS8JZuXFdQ/edit#gid=0
   2. pictures_per_species: this file shows how many pictures each species needs. This will be updated daily. An example can be found here https://docs.google.com/spreadsheets/d/11Pv_lzHuVwqJi83T8BJ_vmf_kwFnDysNmLpQAVCOMPE/edit#gid=0

2. Clone https://github.com/precision-sustainable-ag/benchbot_map_generator

    1. `cd <path to where you want repo>`

    2. `git clone https://github.com/precision-sustainable-ag/benchbot_map_generator`

3. Create virtual environment using python 3.9

    1. `cd benchbot_map_generator`

    2. make sure your python version is 3.9.x using `python --version`

        - if your versions is not 3.9.x, install python 3.9

    3. `python -m pip install --user virtualenv`

    4. `python -m venv .venv`

4. Activate virtual environment

    1. `./.venv/Scripts/activate`

5. Install modules

    2. `pip install -r  requirements.txt`

6. Ask @mikahpinegar for the credentials.json file and copy it into the top level directory

7. Run the generate_map.py file and insert the google sheets IDs that are found in the URL in the browser

    1. For example, if the sheets URL for species_by_row is https://docs.google.com/spreadsheets/d/1lFJAUB-NKeRJ3U0ZaQpUJDIxpp06S5HR5xS8JZuXFdQ/edit#gid=0 the ID is  1lFJAUB-NKeRJ3U0ZaQpUJDIxpp06S5HR5xS8JZuXFdQ

    2. `python ./generate_map.py '<species_by_row_google_sheets_id>' '<pictures_per_species_sheets_id>'`

    3. The command with inserted IDs should look like this except with your keys 

    4. `python .\generate_map.py '1lFJAUB-NKeRJ3U0ZaQpUJDIxpp06S5HR5xS8JZuXFdQ' '11Pv_lzHuVwqJi83T8BJ_vmf_kwFnDysNmLpQAVCOMPE'`
8. Login to your google account using the OAuth popup in your browser

9.  Look at the map.xlsx file that was generated and make sure it looks correct
