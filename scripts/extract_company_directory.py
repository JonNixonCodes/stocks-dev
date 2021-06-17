"""
extract_company_directory.py

Description:
    Extract directory of listed companies from Australian Stock Exchange (ASX)
    
Author: 
    Jonathan Yu

Created at:
    2021-06-06
"""

#%% Import libraries
import sys
import requests

# %% User defined functions
def _download_csv(url, fpath):
    """Download CSV from www.asxlistedcompanies.com"""
    r = requests.get(url, allow_redirects=True)
    open(fpath, 'w').write(r.content)

#%% Main
def main():
    """
    Name:
        extract_company_directory.py
    Usage:
        extract_company_directory.py [YYYYmmdd]... [output_dir_path]
    Description:
        Extract ASX company list and export to file
    """
    dates = sys.argv[1:-1]
    dir_path = sys.argv[-1]
    for d in dates:
        url = "https://www.asxlistedcompanies.com/uploads/csv/{}-asx-listed-companies.csv".format(d)
        fpath = dir_path + "{}-asx-listed-companies.csv".format(d)
        _download_csv(url=url, fpath=fpath)

if __name__ == "__main__":
    main()
