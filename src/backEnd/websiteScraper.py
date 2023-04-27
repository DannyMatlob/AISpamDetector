import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse as up

# Making a GET request

url = 'https://www.geeksforgeeks.org/python-programming-language/'
r = requests.get(url)

total_Links = 0
 
# check status code for response received
# success code - 200
 
soup = bs(r.content, 'html.parser')


# NumDash

dashCount = 0

for c in r.url:
    if c == '-':
        dashCount += 1

print("# of dashes in URL:", dashCount,'\n')

# NumNumericChars

numCount = 0

for c in r.url:
    if c.isnumeric():
        numCount += 1

print("# of numeric values in URL:", numCount,"\n")


# NumSensitiveWords

numSensitive = 0 

sensitive_words = ["secure", "account", "webscr", "login","ebayisapi", "signin", "banking", "confirm"]

for word in sensitive_words:
    if word in url:
        numSensitive += 1

print('# of sensitive words: ',numSensitive,'\n')


# PctExtHyperlinks

extLink_Count = 0
domain = up(url).netloc

def is_external_link(link, domain):
    parsed_link = up(link)
    return parsed_link.netloc != domain


for link in soup.find_all("a"):
    total_Links += 1
    if is_external_link(link.get("href"), domain):
        extLink_Count += 1

print('Total # of links: ', total_Links)
print('# of ext links: ', extLink_Count)
print('% of links are ext ', extLink_Count/total_Links * 100, '%\n')

# PctNullSelfRedirectHyperlinks

nsr_links = 0

def is_Null(link):
    count = 0
    href = link.get("href")
    if href is None:
        count += 1
    elif href == r.url and count == 0:  
        count += 1
    elif isinstance(href, str) and '#' in href and count == 0:
        count += 1
    elif isinstance(href, str) and 'file://' in href and count == 0:
        count += 1
    return count > 0



for link in soup.find_all("a"):
    if(is_Null(link)): 
        nsr_links += 1

print('Total # of links: ', total_Links)
print('# of null self redirecting links: ', nsr_links)
print('% of links are ext ', nsr_links/total_Links * 100, '%\n')

# FrequentDomainNameMismatch

# SubmitInfoToEmail

has_mailto = 0

for link in soup.find_all("a"):
    if(isinstance(link.get("href"), str) and 'mailto' in link.get("href")): 
        has_mailto = 1
        break

print("Website has mailto:", has_mailto == 1)

# PctExtResourceUrlsRT

# ExtMetaScriptLinkRT

# PctExtNullSelfRedirectHyperlinksRT


