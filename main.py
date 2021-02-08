from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, WebDriverException
import sys
import atexit

driver = webdriver.Chrome()
driver.set_page_load_timeout(10)

def saveProgress():
    print('Saving URLs left...')
    with open(sys.argv[1], 'w') as f:
        for item in urlFileLinesCopy:
            f.write("%s" % item)
    atexit.unregister(saveProgress)
    sys.exit()

with open(sys.argv[1], 'r') as f: 
    urlFileLines = f.readlines()

urlFileLinesCopy = urlFileLines.copy()
for url in urlFileLines:
    try:
        ori_url = url
        url = url.strip('\n')
        driver.get(url)
        html = driver.execute_script('return document.documentElement.outerHTML;')
        fileName = url.replace('https://', '').replace('http://', '').replace('/', '') +'.html'
        print(fileName)
        with open('output/' + fileName + '.html', 'w+') as f:
            f.write(html)
        urlFileLinesCopy.remove(ori_url)
    except TimeoutException:
        print('Page timedout: ', url)
    except WebDriverException as e:
        print('Error:', e)
    except:
        print(sys.exc_info())
        #saveProgress()

#atexit.register(saveProgress)





