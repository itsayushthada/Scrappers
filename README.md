# Scrappers
Small Python scripts for scrapping the data from various sources like Twitter.

To scrap data from twitter, you first install tweepy. It can be directly downloadaed from terminal or command prompt using the command 
                *pip install tweepy*
provided pip is installed.<br/>

* Go to apps.twitter.com
* Sign in with your Twitter Account.
* Select *Create New App* button and then fill the details.
* A dialog bos will appear with heading *Access Token*. Select *Create my access Token*.
* Choose what access you need.
* Notedown you OAuth settings. For tweepy we need<br/>
   Consumer Key  
   Consumer Secret  
   OAuth Access Token  
   OAuth Access Token Secret  
  In case these field are not present click on OAuth.
* Write down these values in the python_scrapper.py; change the username(account whose tweets you want to scrap) and run the script.
