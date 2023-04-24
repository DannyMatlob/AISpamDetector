import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse as up

# Making a GET request

url = 'https://www.geeksforgeeks.org/python-programming-language/'
r = requests.get(url)
 
# check status code for response received
# success code - 200
 
soup = bs(r.content, 'html.parser')


# NumDash

print("# of dashes in URL")

dashCount = 0

for c in r.url:
    if c == '-':
        dashCount += 1

print(dashCount, '\n')

# NumNumericChars

print("# of numeric values in URL")

numCount = 0

for c in r.url:
    if c.isnumeric():
        numCount += 1

print(numCount, "\n")


# NumSensitiveWords

numSensitive = 0 

sensitive_words = ["secure", "account", "webscr", "login","ebayisapi", "signin", "banking", "confirm"]

for word in sensitive_words:
    if word in url:
        numSensitive += 1

print('# of sensitive words')
print(numSensitive,'\n')


# PctExtHyperlinks

extLink_Count = 0
total_Links = 0
domain = up(url).netloc

def is_external_link(link, domain):
    parsed_link = up(link)
    return parsed_link.netloc != domain


for link in soup.find_all("a"):
    total_Links += 1
    if is_external_link(link.get("href"), domain):
        extLink_Count += 1

print('Total # of links ', total_Links)
print('# of ext links ', extLink_Count)
print('% of links are ext ', extLink_Count/total_Links * 100, '%\n')

# PctNullSelfRedirectHyperlinks



# FrequentDomainNameMismatch

# SubmitInfoToEmail

# PctExtResourceUrlsRT

# ExtMetaScriptLinkRT

# PctExtNullSelfRedirectHyperlinksRT


