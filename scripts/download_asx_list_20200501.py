"""
download_asx_20200501.py

Description:
    Script to download the ASX list (20200501)
    
Author: 
    Jonathan Yu

Created at:
    2021-06-017
"""
# %% Search for modules in the home directory
import sys
sys.path.append(".")

# %% Import libraries
import os
from src.data.download_asx_list import download_asx_list

# %% Download ASX list
headers = {
    "authority":"www.asxlistedcompanies.com",
    "referer":"https://www.asxlistedcompanies.com/",
    "user-agent":"Mozilla/5.0"
    }
date = '20200501'
url = f"https://www.asxlistedcompanies.com/uploads/csv/{date}-asx-listed-companies.csv"
fpath = f"data/{date}-asx-listed-companies.csv"
assert('data' in os.listdir())
download_asx_list(url=url, headers=headers, fpath=fpath)
