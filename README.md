# AISpamDetector
Group Project for CS 166: Information Security. Machine learning technique applied to Spam Detection

Project Overview 

Phishing is a prevalent online scam involving attackers posing as trustworthy entities to deceive victims into providing sensitive information, such as usernames, passwords, credit card numbers, and other personal data. The term "phishing" originates from the word "fishing," as attackers use baits designed to appear genuine and often mimic well-known companies or banks.
During the COVID-19 pandemic in early 2020, there was a significant increase in phishing attacks targeting individuals seeking to make money online. Attackers exploited the situation by using fake NFT websites and job applications to scam people, stealing their personal information and money. 
Concurrently, spam emails have been a persistent problem, cluttering inboxes and often containing malicious links or attachments. Websites that disguise themselves as trustworthy entities attempt to acquire sensitive information like usernames, passwords, and credit card information. Both phishing websites and spam emails are critical threats to address, as they can lead to financial losses or reputational damage for individuals and organizations. Attackers can use sensitive information to gain unauthorized access to accounts, inject malware, or spy on victims.

Objectives and Scope

Phishing is a prevalent online scam involving attackers posing as trustworthy entities to deceive victims into providing sensitive information, such as usernames, passwords, credit card numbers, and other personal data.

Architecture

Spam Detection:
The training Model that was used for spam detection was logistic regression. Logistic regression is a function that helps find the relationship between variables and map that relationship between 0 and 1. To train the independent variable, in this case, the spam email body. A vectorizer function was used to find the term frequency of each word or character giving numerical value to the text. 


Phishing Detection:
Training Model
The first step to training the phishing detection model was to find a dataset. During the project term, we trained using two different datasets. The first dataset was much larger at 50,000 entries and 50 features per entry. Having trained a Support Vector Machine on the top 20 best features of the dataset, we arrived at a maximum accuracy of 86.7%. In order to discover the top features, we had to perform statistical correlations on the data, including a mutual info correlation, as well as a Spearman correlation. Training on more or less than 20 features resulted in decreased accuracy, therefore 20 features was the optimal amount to train on.

We ran into the issue of vague and non-reproducible features however, and opted for a better documented, albeit smaller dataset. This new dataset comprised 10,000 entries with 10 features per entry, and resulted in an accuracy of 95% using a Random Forest Classifier. The features chosen for this dataset were based on a study that sought to find the top 10 features for phishing detection, and the features tended to be more robust and sophisticated. With a working and highly accurate model, we can now begin work on the website scraper in order to apply the model to websites outside of the training set.

Website Scraper

In order to gather the data required for our prediction, we needed to program a website scraper. This Python program requests and parses a website's HTML source code using the BeautifulSoup library to parse, and the requests library to make HTTP requests . The program websiteScraper.py has the getPhishing() method. It takes in the URL of a website HTML source code.



After extracting the 10 features, based on this project and this study, we append them to an array. After saving and loading the Phishing model from a .joblib file, the array is used as the parameter for the prediction() method, returning a result of 1, phishing, or 0, legitimate.








Issues


	An issue that we encountered during the implementation and testing of websiteScraper was that some websites had DDoS protection or were blocked by the current network, causing the program to not run properly. If a website would return an error code of 403 or 404, the HTML source code returned by the request library would be empty. The empty HTML source code caused the testing on legitimate and phishing websites to be incorrect, decreasing the accuracy of our program. We addressed this problem by surrounding the request.get() function in a try/except block and only running the program if we get a successful response, indicated by the status code 200.

	Another issue that we faced was our predictions being incorrect due to the way that certain websites worked compared to our model. An example would be domain name mismatches. Our model predicts based on the domain name in HTML source code and the actual domain. A number of reputable websites use different domains and subdomains, which can affect our prediction results.

Results and Analysis

Phishing






	We were able to get ~55% accuracy out of 34 legit websites. Therefore one problem with our program and model is that there is a high rate of false positives on legitimate websites, especially ones that are in languages other than english (naver, baidu, etc) . In the future, we would take into account different named subdomains during our feature extraction. However, a random sample of 22 websites from the PhishTank database gave us an accuracy of ~86%. 


Spam email:
We tested the model with a 3rd dataset and resulted with an 84% accuracy score.  We still get 16% false positive result, which might not be that high, but I believe we can achieve a higher accuracy score if we were to include the subject and email as the independent variable. 


Future Work

Phishing:
Some improvements that could be made in the future regarding phishing include
adding the ability to parse websites through DDoS protection
training and testing our model and program on a larger dataset
implementing a complete website application in order to make the program more user friendly.

Spam Email:
Future improvements that could be made for the spam email detection:
including the subject in training, not only the body text
parsing and training on images and links within the email


Conclusion
Phishing and spam detection is a difficult subject due to the many factors that need to be accounted for. As phishing website technology changes and evolves, current detection methods could be rendered obsolete. A convincing and sophisticated phishing website requires in-depth analysis and digging on many fronts in order to discover malicious intent. However, the majority of phishing websites out there tend to be on the amateur side and showcase common patterns that can be detected by our AI model. It is because of this that our work remains a useful tool for detecting the legitimacy of websites.


Contributions
Nathan: Website scraper
Danny: Phishing Detection Model
Seungpil: Phishing Detection Model
Minh: Spam Email Detection Model
Nguyen: Spam Email Detection Model










References

Chiew KL, Tan CL, Wong K, Yong KSC, Tiong WK. 2019. A new hybrid ensemble feature selection framework for machine learning-based phishing detection system. Information Sciences. 484:153–166. doi:https://doi.org/10.1016/j.ins.2019.01.064.
Palmieri A. 2023 May 5. ML with Phishing. GitHub. https://github.com/andpalmier/MLWithPhishing.
Python Web Scraping Tutorial. 2021 Dec 3. GeeksforGeeks. https://www.geeksforgeeks.org/python-web-scraping-tutorial/.
PhishTank https://phishtank.org/
