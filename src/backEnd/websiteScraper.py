from collections import Counter
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse
from urllib.request import urlopen
import urllib


# Making a GET request

url = 'https://www.geeksforgeeks.org/python-programming-language/'
r = requests.get(url)
 
# check status code for response received
# success code - 200
 
soup = bs(r.content, 'html.parser')

links_list = soup.find_all("a")

# 1. NumDash

dashCount = 0

for c in r.url:
    if c == '-':
        dashCount += 1

print("1. # of dashes in URL:", dashCount,'\n')

# 2. NumNumericChars

numCount = 0

for c in r.url:
    if c.isnumeric():
        numCount += 1

print("2. # of numeric values in URL:", numCount,"\n")


# 3. NumSensitiveWords

numSensitive = 0 

sensitive_words = ["secure", "account", "webscr", "login","ebayisapi", "signin", "banking", "confirm"]

for word in sensitive_words:
    if word in url:
        numSensitive += 1

print('3. # of sensitive words: ',numSensitive,'\n')


# 4. PctExtHyperlinks

links = []
for link in links_list:
    links.append(link.get('href'))

external_links = [link for link in links if urlparse(link).netloc != '' and urlparse(link).netloc != urlparse(url).netloc]
external_count = len(external_links)

total_count = len(links)

percentage = (external_count / total_count) * 100
print(f'Percentage of external hyperlinks: {percentage:.2f}%')

# 5. PctNullSelfRedirectHyperlinks

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



for link in links_list:
    if(is_Null(link)): 
        nsr_links += 1

print('Total # of links: ',total_count)
print('# of null self redirecting links: ',nsr_links)
print('5. % of ext links are null, etc: ',nsr_links/total_count * 100, '%\n')

# 6. FrequentDomainNameMismatch

# extracts href, parses href for netloc (domain name), creates list of domain names
domains = [urlparse(link.get('href')).netloc for link in links_list if urlparse(link.get('href')).netloc != '']

# gets the most common domain name
most_common_domain = Counter(domains).most_common(1)[0][0]

# webpage domain name
webpage_domain = urlparse(url).netloc

print("Webpage domain name: ",webpage_domain)
print("Most frequent HTML source code domain name: ",most_common_domain)
print("Match?: ",most_common_domain == webpage_domain,'\n')

# 7. SubmitInfoToEmail

has_mailto = 0

if 'mailto' in soup.prettify():
    has_mailto = 1

print("7. Website has mailto:",has_mailto == 1,'\n')

# 8. PctExtResourceUrlsRT

urls = []


for tag in soup.find_all():
    for attribute_name, attribute_value in tag.attrs.items():
        if attribute_name in ['src', 'href']:
            parsed_url = urlparse(attribute_value)
            urls.append(parsed_url)

external_urls = [parsed_url for parsed_url in urls if parsed_url.netloc != '' and parsed_url.netloc != urlparse(url).netloc]
external_count = len(external_urls)

total_count = len(urls)

percentage = (external_count / total_count) * 100
print("external_count: ",external_count)
print(f'Percentage of external resource URLs: {percentage:.2f}%')




# 9. ExtMetaScriptLinkRT

# 10. PctExtNullSelfRedirectHyperlinksRT


