import sys
import unittest
import pandas as pd

sys.path.append('../Logic')
from scrape_reviews import *
from Scraping_general import *

class TestClass(unittest.TestCase):
    url1 = "https://www.amazon.it/12-regole-vita-antidoto-caos/dp/8863865825/ref=sr_1_1?crid=4FDIE8N0GFA7&keywords=12+regole+per+la+vita&qid=1678737099&sprefix=12+regole%2Caps%2C336&sr=8-1"
    url2 = "https://www.amazon.it/s/ref=nb_sb_noss_2?__mk_it_IT=ÅMÅŽÕÑ&url=search-alias%3Daps&field-keywords=12+regole+per+la+vita&crid=LY6AOEEEUN7M&sprefix=12+%2Caps%2C219"
    
    #TODO
    '''
    def check(df, self):
        if isinstance(df, pd.DataFrame) and not result.empty:
            result = "Test passed"
        else:
            result = "Test failed"
        
        self.assertEqual(result, "Test passed")
    '''
    
    def test_reviews(self):
        result = getLink(self.url1, 5)
        print(result)
        print(type(result))
        self.check(result, self)
    

    def test_categories(self):
        result = get_product_info(self.url2)

        keys = result.values()
        result = "Test failed"

        for key in keys:
            if key != None:
                result = "Test passed"
        self.assertEqual(result, "Test passed")
   
       
# Run the tests
if __name__ == '__main__':
    print("Starting the tests")
    unittest.main()

