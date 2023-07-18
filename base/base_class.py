
class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print('\nCurrent url ' + get_url)

    def assert_url(self, url):
        get_url = self.driver.current_url
        assert get_url == url
        print ("url GOOD")
    def assert_word(self, word, expected_name):
        value_word = word.text()
        assert value_word == expected_name
        print('Good value word')




