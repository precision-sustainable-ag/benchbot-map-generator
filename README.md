# benchbot_map_generator
Introduction

This document will go over using google sheets and a python script to generate a map excel file for the bench bot

Prerequisites

Python 3.9 installed 

Instructions can be found here How to Download and Install Python on Windows - Data to Fish  

A copy of credentials.json from @Mikah Pinegar 

Steps

Clone https://github.com/precision-sustainable-ag/benchbot_map_generator - Connect to preview 

cd <path to where you want repo>

git clone https://github.com/precision-sustainable-ag/benchbot_map_generator

Create virtual environment using python 3.9

cd benchbot_map_generator

make sure your python version is 3.9.x using python --version

if your versions is not 3.9.x, install python 3.9

python -m pip install --user virtualenv

python -m venv .venv

Activate virtual environment

./.venv/Scripts/activate

Install modules

pip install -r  requirements.txt

Ask @Mikah Pinegar for the credentials.json file and copy it into the top level directory

Run the generate_map.py file and insert the google sheets IDs that are found in the URL in the browser

For example, if the sheets URL for species_by_row is https://docs.google.com/spreadsheets/d/1lFJAUB-NKeRJ3U0ZaQpUJDIxpp06S5HR5xS8JZuXFdQ/edit#gid=0 the ID is  1lFJAUB-NKeRJ3U0ZaQpUJDIxpp06S5HR5xS8JZuXFdQ

python ./generate_map.py '<species_by_row_google_sheets_id>' '<pictures_per_species_sheets_id>'

The command with inserted IDs should look like this except with your keys 


python .\generate_map.py '1lFJAUB-NKeRJ3U0ZaQpUJDIxpp06S5HR5xS8JZuXFdQ' '11Pv_lzHuVwqJi83T8BJ_vmf_kwFnDysNmLpQAVCOMPE'
Login to your google account using the OAuth popup in your browser

Look at the map.xlsx file that was generated and make sure it looks correct
