class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(10)
