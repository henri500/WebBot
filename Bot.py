from selenium  import webdriver
from selenium.webdriver.common.keys import Keys#enable bot to submit text to forms 
import time 

class facebookBot(object):
		"""
-Create an object from this class with to argurments(username,password)
-The QuitBrowser is used to close the browser once its done allthe preprogrammed tasks
-the login fucntion will start up the bot
-to locate the xpath on the web page:
		-Inspect the webpage (Ctrl+shif+i on )  
		-right click on the element you want and select "copy xpath"
-oncomment the background mode if you want the bot to work in the back ground
-NOTE;
		- This class can't be used for every webpage, make sure to modify the element(xpath) and web page url.
		-Make sure the chromedriver(for chrome) or gekodriver(firefox) are in your systeme variable(Path) for selenium to access these drivers
		OR modify "self.driver=webdriver.Chrome() " to -----> self.driver=webdriver.Chrome([path to where you stored the drivers])
	"""
	def __init__(self, username,password):
		self.username=username
		self.password=password
		'''
		#------------ruuning the bot in the background---------------------
		This part of the code is inspired from Mahesh Reddy tutorial on his website :
										 https://www.built.io/blog/run-selenium-tests-in-headless-browser
		
		options = webdriver.ChromeOptions() #if you have a chrome browser 
		options.add_argument('headless')
		options.add_argument('window-size=1200x600')
		options.add_argument('window-size=1200x600')
		self.driver = webdriver.Chrome(chrome_options=options)
		#------------------------------------------------
		'''
		self.driver=webdriver.Chrome()

	def quiteBrowser(self):
		self.driver.close()

	def login(self):
		driver=self.driver
		driver.get("https://www.facebook.com")# 
		time.sleep(2)#loading page delay this is subject to your internet speed
		UserNameElemt=driver.find_element_by_xpath("//input[@name='email']") 
		UserNameElemt.clear()
		UserNameElemt.send_keys(self.username)#enter username  mobile phone 
		passwordElement=driver.find_element_by_xpath("//input[@name='pass']")
		passwordElement.clear()
		passwordElement.send_keys(self.password)#enter text in password field
		passwordElement.send_keys(Keys.RETURN)

#test1=facebookBot(username,password) initialize the bot
#test1.login() to start the bot
