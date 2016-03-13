from splinter import Browser

with Browser() as browser:	
	browser.visit('http://www.facebook.com')
	browser.fill('email',UserEmail)
	browser.fill('pass',UserPass)
	button = browser.find_by_id('loginbutton')
	button.click()
	browser.visit('https://m.facebook.com/')
	button=browser.find_by_name('view_privacy')
	button.click()
	browser.click_link_by_text('Public')
	browser.fill('xc_message','I occasionally, as in pretty much daily, go on Omegle and do roleplays as a 25 year old woman whose into being tied up.')
	button=browser.find_by_name("view_post")
	button.click()

	
