from selenium.webdriver.common.by import By

import time

import config
import web
import logger

# Globals
logger = logger.instance


def reset():
    logger.info('Script started.')
    config.init_web()
    web.start()

    driver = web.driver
    driver.implicitly_wait(3)

    driver.get(config.url)
    driver.set_window_size(1680, 947)
    driver.find_element(By.ID, "showlogininfo").click()
    driver.find_element(By.ID, "txt_Username").send_keys(config.username)
    driver.find_element(By.ID, "txt_Password").send_keys(config.password)
    driver.find_element(By.ID, "loginbutton").click()
    driver.find_element(By.ID, "name_addconfig").click()
    driver.find_element(By.ID, "name_maintaininfo").click()
    driver.switch_to.frame(0)
    time.sleep(2)

    driver.find_element(By.ID, "btnsaveandreboot").click()
    driver.switch_to.alert.accept()

    wait_time = 75
    logger.info('Request submitted, sleeping {} seconds'.format(wait_time))
    time.sleep(wait_time)


if __name__ == '__main__':
    reset()
