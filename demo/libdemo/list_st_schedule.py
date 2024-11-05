import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.srikanthtechnologies.com/")
contents = resp.text

bs = BeautifulSoup(contents, 'html.parser')

table = bs.find(id='ctl00_ContentPlaceHolder1_GridView2')
# take all rows of the table
rows = table.find_all("tr")
# Ignore heading, which is first row
for row in rows[1:]:
    cols = row.find_all("td")
    subject = cols[1].text
    timing = cols[2].text
    stdate = cols[3].text
    print(f"{subject:40}  {timing:10}   {stdate:10}")
