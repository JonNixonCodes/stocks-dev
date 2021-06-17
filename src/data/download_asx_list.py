"""
download_asx_list.py

Description:
    Download listed companies from Australian Stock Exchange (ASX)
    
Author: 
    Jonathan Yu

Created at:
    2021-06-06
"""

#%% Import libraries
import sys
import requests

# %% Define functions
def download_asx_list(url, headers, fpath):
    """Get ASX list from www.asxlistedcompanies.com"""
    r = requests.get(url=url, headers=headers, allow_redirects=True)
    open(fpath, 'wb').write(r.content)

#%% Main
def main():
    """
    Name:
        download_asx_list.py
    Usage:
        download_asx_list.py [output_dir_path] [YYYYmmdd]...
    Description:
        Download ASX company list and export to file
    """
    dir_path = sys.argv[1]
    dates = sys.argv[2:]
    headers = {
        "authority":"www.asxlistedcompanies.com",
        "referer":"https://www.asxlistedcompanies.com/",
        "user-agent":"Mozilla/5.0"
        }
    for d in dates:
        url = "https://www.asxlistedcompanies.com/uploads/csv/{}-asx-listed-companies.csv".format(d)
        fpath = dir_path + "{}-asx-listed-companies.csv".format(d)
        download_asx_list(url=url, headers=headers, fpath=fpath)

if __name__ == "__main__":
    main()
