import websiteScraper

legit_websites = ['https://www.google.com',
            'https://www.w3schools.com/python/python_try_except.asp',
            'https://www.youtube.com',
            'https://www.tmall.com',
            'https://www.facebook.com',
            'https://www.baidu.com',
            'https://www.taobao.com',
            'https://www.jd.com',
            'https://www.yahoo.com',
            'https://www.amazon.com',
            'https://www.wikipedia.org',
            'https://www.weibo.com',
            'https://www.reddit.com',
            'https://www.live.com',
            'https://www.netflix.com',
            'https://www.vk.com',
            'https://www.yandex.ru',
            'https://www.mail.ru',
            'https://www.instagram.com',
            'https://www.microsoft.com',
            'https://www.twitch.tv',
            'https://www.aliexpress.com',
            'https://www.office.com',
            'https://www.stackoverflow.com',
            'https://www.imdb.com',
            'https://www.naver.com',
            'https://www.github.com',
            'https://www.apple.com',
            'https://www.bing.com',
            'https://www.booking.com',
            'https://www.blogger.com',
            'https://www.bbc.com',
            'https://www.wikia.com',
            'https://www.nordvpn.com']

phishing_sites = [
                  'http://wmdigmulpk.duckdns.org', 
                  'http://winufjbwcv.duckdns.org', 
                  'https://customerinvoice-534998.web.app/', 
                  'https://fb-restriction-case-47d8e.web.app/', 
                  'https://fb-restriction-case-99a3d.web.app/', 
                  'https://fb-restriction-case-e2a64.web.app/', 
                  'https://fb-submit-appeal-5c720.web.app/', 
                  'https://fb-submit-appeal-58e31.web.app/', 
                  'https://gariu6q.web.app/', 
                  'https://gariu6q.firebaseapp.com/', 
                  'https://mygov-aus.web.app/', 
                  'https://mygov-aus.firebaseapp.com/', 
                  'https://rbfcualert-cc654.web.app/', 
                  'https://vmi-kompensacija.web.app/', 
                  'https://vmi-kompensacija.firebaseapp.com/', 
                  'https://www.condongbowlingclub.com.au/.auth/', 
                  'https://steamcommunity.sytes.net', 
                  'https://clicki-9cd58.firebaseapp.com/',
                  'http://junior-projet.ml/scc/', 
                  'https://54-174-35-95.cprapid.com/nordea_no/',
                  'https://isiyama89.noor.jp/newcodingLinkedin/',
                  'https://lt27.de/BBzobw', 
                  'https://urlz.fr/lJ3l', 
                  'https://tinyurl.com/4sdvsa9f', 
                  'https://boy.login.njdazk.ink/', 
                  'https://nasjones304.wixsite.com/my-site', 
                  'https://gonzo1060.wixsite.com/my-site', 
                  'https://boy.login.aptdzk.ink/', 
                  'https://bancolombia.com7mua70281.repl.co/',
                  'https://bt-voice-04c87e.webflow.io/']


# legit_total = 0
# legit_wrong = 0
# for link in legit_websites:
#     legit_total += 1
#     result = websiteScraper.getPhishing(link)
#     print(link, result,'\n')
#     if result != 0:
#         legit_wrong += 1
# print(legit_total, "Legit Websites Accuracy =", ((legit_total-legit_wrong)/legit_total) * 100)

# phish_total = 0
# phish_wrong = 0
# for link in phishing_sites:
#     phish_total += 1
#     result = websiteScraper.getPhishing(link)
#     print(link, result,'\n')
#     if result != 1:
#         phish_wrong += 1
# print(phish_total, "Phish Website Accuracy =", ((phish_total-phish_wrong)/phish_total) * 100)

result = websiteScraper.getPhishing('https://www.geeksforgeeks.org/python-web-scraping-tutorial/#')
print('https://www.geeksforgeeks.org/python-web-scraping-tutorial/#', result,'\n')
result = websiteScraper.getPhishing('https://www.w3schools.com/python/python_try_except.asp')
print('https://www.w3schools.com/python/python_try_except.asp', result,'\n')
result = websiteScraper.getPhishing('https://dannymatlob.github.io/')
print('https://dannymatlob.github.io/', result,'\n')