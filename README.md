# Scrappers
Small Python scripts for scrapping the data from various sources like Twitter.

### 1. Tweets Mining
To scrap data from twitter, you first install tweepy. It can be directly downloadaed from terminal or command prompt using the command 
                *pip install tweepy*
provided pip is installed.<br>

* Go to https://developer.twitter.com/en/apps
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

### 2. CryptoCurrency Data Mining
A Python Notebook is added with all details the data for 100+ cryptocurrencies.<br>
I've used this script for my Data and Information Visualization project.

### 3. User Agents Mining
The User-Agent request header contains a characteristic string that allows the network protocol peers to identify the application type, operating system, software vendor or software version of the requesting software user agent. While sending the requests different user agents can be used to simulate the requests from the diffrent environments.<br><br>

I've written a script to parallely scrap the user agents from internet. Kindly adjust the number of process with respect to your no of cores and the hyper threading status. I'll add addition bash scripts to bind the process with CPU to prevent the time loss due to context switch.

### 4. Weights Fetching From the Torrent Networks
While working on a distributed learning environment, I've tried to store the weights of the different parts of the Neural Network on different Computing Nodes. Hence when the learning gets over, weightsfetecher.py script downloads the weights fro all the distributed locations where ever this script is invoked. It requires a Magnet link to initiate the down also all the different model weights files. For more peer to peer networking can be found on [Source Paper](http://web.cs.ucla.edu/classes/cs217/05BitTorrent.pdf)
