import requests as req
from bs4 import BeautifulSoup
import time
import multiprocessing 


def save(dev, ua):
	
	file = dev+'.txt'

	with open(file,'ab') as writer:
		writer.write(ua+'\n')

def getUserAgents(dev):

	url = 'http://www.useragentstring.com/pages/useragentstring.php?name='+dev
	r = req.get(url)

	if r.status_code == 200:
		soup = BeautifulSoup(r.content,'html.parser')
	else:
		soup = False

	if soup:
		div = soup.find('div',{'id':'liste'})
		lnk = div.findAll('a')

		for i in lnk:
			try:
				save(dev, i.text)
			except:
				print('No User Agent')
	else:
		print("So Soup for {}".formmat(dev))

DEVICES_1 = ['Firefox','Internet+Explorer','Opera','Safari','Chrome','Edge','Android+Webkit+Browser']
DEVICES_2 = ['Cerberian+Drtrs', 'BillyBobBot', 'Classilla', 'Flock', 'Avant+Browser']
DEVICES_3 = ['Netscape', 'Sleipnir', 'WeltweitimnetzBrowser', 'Playstation+3']
DEVICES_4 = ['QtWeb+Internet+Browser', 'SeaMonkey', 'Wyzo']

def fun(DEVICES):
	for x in DEVICES:
		getUserAgents(x)
		time.sleep(20)
		
p1 = multiprocessing.Process(target=fun, args=(DEVICES_1, )) 
p2 = multiprocessing.Process(target=fun, args=(DEVICES_2, ))
p3 = multiprocessing.Process(target=fun, args=(DEVICES_3, )) 
p4 = multiprocessing.Process(target=fun, args=(DEVICES_4, ))

p1.start() 
p2.start() 
p3.start() 
p4.start()

p1.join()
p2.join()
p3.join()
p4.join()  
