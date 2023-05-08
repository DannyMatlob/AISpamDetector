from collections import Counter
import requests 
from bs4 import BeautifulSoup as bs
from urllib.parse import urlparse
from urllib.request import urlopen
import urllib
import joblib
import numpy
import argparse



def getPhishing(url):

    array = []

    
    r = requests.get(url)

    if r.status_code == 200:

        soup = bs(r.content, 'html.parser')

        links_list = soup.find_all('a')


        # 1. NumDash

        dashCount = 0

        for c in r.url:
            if c == '-':
                dashCount += 1

        print("1. # of dashes in URL:", dashCount)
        array.append(dashCount)

        # 2. NumNumericChars

        numCount = 0

        for c in r.url:
            if c.isnumeric():
                numCount += 1

        print("2. # of numeric values in URL:", numCount)
        array.append(numCount)

        # 3. NumSensitiveWords

        numSensitive = 0 

        sensitive_words = ["secure", "account", "webscr", "login","ebayisapi", "signin", "banking", "confirm"]

        for word in sensitive_words:
            if word in url:
                numSensitive += 1

        print('3. # of sensitive words: ',numSensitive)
        array.append(numSensitive)

        # 4. PctExtHyperlinks

        external_count = 0

        current_domain = urlparse(url).hostname

        for link in links_list:
            href = urlparse(link.get("href"))
            link_domain = href.hostname
            
            if link_domain is None:  # Skip if href is a relative link
                continue
            
            if link_domain != current_domain and not link_domain.endswith('.' + current_domain):
                external_count += 1

        total_count = len(links_list)
        percentage = 0

        if(external_count != 0): percentage = (external_count / total_count)
        print('Total # of links', total_count)
        print('Total # of ext links', external_count)
        print(f'4. Percentage of external hyperlinks: {percentage*100:.2f}%')
        array.append(percentage)

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
        percentage = 0

        if(external_count != 0): percentage = (nsr_links/total_count)
        print('5. % of ext links are null, etc: ',percentage, '%')
        array.append(percentage)

        # 6. FrequentDomainNameMismatch

        # extracts href, parses href for netloc (domain name), creates list of domain names
        domains = []

        for link in links_list:
            if urlparse(link.get('href')).netloc:
                domains.append(urlparse(link.get('href')).netloc)
        

        # gets the most common domain name

        # webpage domain name
        webpage_domain = urlparse(url).netloc
        webpage_domain = ".".join(webpage_domain.split(".")[-2:])

        if domains: 
            most_common_domain = Counter(domains).most_common(1)[0][0]
            most_common_domain = ".".join(most_common_domain.split(".")[-2:])
                

        print("Webpage domain name: ",webpage_domain)
        print("Most frequent HTML source code domain name: ",most_common_domain)
        print("6. Frequent Domain Name Mismatch?: ",most_common_domain != webpage_domain)
        if most_common_domain != webpage_domain: array.append(1)
        else: array.append(0)

        # 7. SubmitInfoToEmail

        has_mailto = 0

        if 'mailto' in soup.prettify():
            has_mailto = 1

        print("7. Website has mailto:",has_mailto == 1)
        if has_mailto == 1: array.append(1)
        else: array.append(0)

        # 8. PctExtResourceUrlsRT

        urls = []


        for tag in links_list:
            for attribute_name, attribute_value in tag.attrs.items():
                if attribute_name in ['src', 'href']:
                    parsed_url = urlparse(attribute_value)
                    urls.append(parsed_url)

        external_urls = [parsed_url for parsed_url in urls 
                        if parsed_url.netloc != '' and parsed_url.netloc != urlparse(url).netloc]

        external_count = len(external_urls)

        total_count = len(urls)

        if(external_count != 0 and total_count != 0): percentage = (external_count / total_count)
        else: percentage = 0
        print(f'8. Percentage of external resource URLs: {percentage*100:.2f}%')
        if (percentage * 100 < 22): 
            #print("1\n")
            array.append(1)
        elif (percentage * 100 >= 22 and percentage * 100 > 61): 
            #print("0\n")
            array.append(0)
        else: 
            #print("-1\n")
            array.append(-1)



        # 9. ExtMetaScriptLinkRT

        tags = []
        for tag in soup.find_all(['meta', 'script', 'link']):
            tags.append(tag)

        external_tags = []
        for tag in tags:
            for attribute_name, attribute_value in tag.attrs.items():
                if attribute_name in ['src', 'href']:
                    parsed_attribute_value = urlparse(attribute_value)
                    if parsed_attribute_value.netloc != '' and (parsed_attribute_value.netloc != urlparse(url).netloc or parsed_attribute_value.hostname.split('.')[-2:] != urlparse(url).hostname.split('.')[-2:]):
                        external_tags.append(tag)

        
        external_count = len(external_tags)

        total_count = len(tags)

        if(external_count != 0 and total_count != 0): percentage = (external_count / total_count)
        else: percentage = 0
        print('# of external tags: ',external_count)
        print('Total # of tags: ',total_count)
        print(f'9. Percentage of tags containing external URLs: {percentage*100:.2f}%')
        if percentage * 100 < 17:
            #print('1\n')
            array.append(1)
        elif percentage * 100 >= 17 and percentage * 100 <= 81:
            #print('0\n')
            array.append(0)
        else:
            #print('-1\n')
            array.append(-1)


        # 10. PctExtNullSelfRedirectHyperlinksRT

        dictionary = ['#','#skip','#content','javascript:void(0)']

        external_links = []
        for link in links_list:
            href = link.get('href')
            if href is not None:
                parsed_href = urlparse(href)
                if parsed_href.netloc:
                    root_domain = '.'.join(parsed_href.netloc.split('.')[-2:])
                    url_root_domain = '.'.join(urlparse(url).netloc.split('.')[-2:])
                    if root_domain != url_root_domain or href in dictionary:
                        external_links.append(link)


        external_count = len(external_links)
        total_count = len(links_list)

        if(external_count != 0 and total_count != 0): percentage = (external_count / total_count)
        else: percentage = 0
        print(f'10. Percentage of external links with different domain names, starts with "#", or using "JavaScript ::void(0)": {percentage*100}%')
        if percentage * 100 < 31:
            #print('1\n')
            array.append(1)
        elif percentage * 100 >= 31 and percentage <= 67:
            #print('0\n')
            array.append(0)
        else:
            #print('-1\n')
            array.append(-1)



        # Predicting
        model_path = "models/Phishing_RFC.joblib"
        model = joblib.load(model_path)
        input = numpy.array(array).reshape(1,-1)
        prediction = model.predict(input)
        return prediction
    
    else:
        return "Error connecting to website"