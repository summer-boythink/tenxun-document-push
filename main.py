# -*- encoding=utf8 -*-
__author__ = "tang"

from airtest.core.api import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from airtest_selenium.proxy import WebChrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from configparser import ConfigParser
import os

driver = WebChrome()
driver.implicitly_wait(20)
auto_setup(__file__)

cf = ConfigParser()
file_path = os.path.join(os.path.abspath('.'),'config.ini')
if not os.path.exists(file_path):
    raise FileNotFoundError("文件不存在")

cf.read(file_path)

QQuser = cf.get("Info", "QQuser")
QQpass = cf.get("Info", "QQpass")
rename = cf.get("Info", "rename")
keepname = cf.get("Info", "keepname")
sendtag = cf.get("Info", "sendtag")

# 登录
driver.get("https://docs.qq.com/desktop?_t=1612365322648")

driver.implicitly_wait(200)
driver.switch_to.frame("login_frame")
sleep(2)
driver.find_element_by_id("switcher_plogin").click()
driver.implicitly_wait(20)
driver.find_element_by_id("u").send_keys(QQuser)
driver.find_element_by_id("p").send_keys(QQpass)
driver.find_element_by_id("login_button").click()
driver.implicitly_wait(60)

#重命名文档
driver.find_element_by_xpath("//*[@class=\"layout-view-header\"]/div/div/div[2]/span[1]").click()
driver.implicitly_wait(80)
driver.find_element_by_xpath("//*[@id=\"root\"]/div/div[2]/div[2]/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div/div/div/div/span/span").click()
driver.switch_to_new_tab()
driver.find_element_by_xpath("//input[@autocomplete='off']").send_keys(Keys.CONTROL,'a')
driver.find_element_by_xpath("//input[@autocomplete='off']").send_keys(Keys.BACK_SPACE)
driver.find_element_by_xpath("//input[@autocomplete='off']").send_keys(rename)




driver.find_element_by_xpath("//*[@id=\"root\"]/div[2]/div/div/div/div[2]").click()


def check(driver):
    num = driver.find_elements(By.XPATH,"//*[@id=\"fillBodyContent\"]/div/div[2]/div/div/div/div")
    return len(num)


while check(driver)!=1:
    # 删
    div = driver.find_element_by_xpath("//*[@id=\"fillBodyContent\"]/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/div")
    text = div.get_attribute('innerText')
    print(text)
    if text != keepname:
        ele = driver.find_element_by_xpath("//*[@id=\"fillBodyContent\"]/div/div[2]/div/div/div/div/div/div/div/div")
    else:
        ele = driver.find_element_by_xpath("//*[@id=\"fillBodyContent\"]/div/div[2]/div/div/div/div[2]/div/div/div/div")

    actionChains = ActionChains(driver)
    actionChains.context_click(ele).perform()
    driver.find_element_by_xpath("//ul[@style='width: 100px;']").click()

    driver.find_element_by_xpath("/html/body/div[last()]/div/div[4]/button[2]").click()
    sleep(1)



# 发送
driver.find_element_by_xpath("//*[@id=\"root\"]/div/header/span[4]/button").click()
sleep(2)
driver.find_element_by_xpath("/html/body/div[last()]/div/div[4]/button[2]/div").click()
sleep(2)
driver.find_element_by_xpath("//*[@id=\"share-container\"]/div/div/div/div[3]/div[2]/div[2]/ul/li[2]").click()
sleep(2)
driver.find_element_by_xpath("//*[@id=\"share-container\"]/div/div/div/div[3]/div[4]/div/div/div/div").click()
sleep(2)
driver.find_element_by_xpath("//input[@placeholder='搜索']").send_keys(sendtag)
driver.find_element_by_xpath("//img[@src='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAAXNSR0IArs4c6QAAAERlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAA6ABAAMAAAABAAEAAKACAAQAAAABAAAAIKADAAQAAAABAAAAIAAAAACshmLzAAACzElEQVRYCcWXPY8SQRjHdxcIL9FAAUGhI8SAH4DOhFITaxpjcrlY0PIFDLGj4hsYEtSC2sKSmgYrJQYIBUJAC2h4OV7W+Y3MhTvMgpfb5Ul2Jzu78/yemZ155j+6drrptVotlkwmn/v9/ozb7X7icrme0nyz2Xxbr9c/5vN5o91uf8nlcgNRbZ7iWj/2UTabdZfL5YtgMPjOMIzHx77n/Xa7HU6n07eFQqFSr9fXVm2sAtAbjcbLcDj8XoDDOPF4PFogENB8Pp8mei8v6sUIyGuxWGiz2UxbrVZUE8hvYZeZTOazeDxpRGRDet1qtT70ej2Tazwem1dXV+apxre0Ue3xhU/p/NitVCo97HQ6TRr3+31T9OpU7sF3tMUHvvBZLBYfWPKJUsGHw6EpJtaB0/+twAe+VBC3R2J/DuhiqKri/77yer1aNBrVdH3/tWXsli9F0NpoNNKWy6UmRuVjKpV6LRrIOWGolkw44GJ5aZFI5N7g+Kcj+MQ3DFiKKwNgWJjtVIryenarj+6jZNXgG4N141c0m803/CNmrt2mVgdMgmEEdJIMD6FQiMJWU4wdUzdIr2Q4kgyX3aY4MCWb3A6UDOeUKRZsg40FMOnVKVMs2Aa7GmBmqVOmWLAN8SC3VFXpRBCKBfs6ETkB/gfDNBATvGBLdcoUS5TfDZTMuQKAbSCjCAAx4ZQpFmwDDQcYJeOUKRZs9lu92+3+JDPFYjHbsyFybTAYSN2YSCTirAITAUnvJ5MJha2mGDvmX53I1ihG4Rc7IjLKLsM3DFhqO5Z5AOmMeqXrorRlSbL08L1jXCq5vq+5zivJRGRmPp+/EJF+Rbuh4VTCkGHf8YYPpQfxDQOWcndjBxL/ZxuPxz+l0+kX4lDxiOWCQEXL3cXoiFBA8qACvFqtPqtUKscTDhPEqYPJ/hy43UlHjmZWAciAGI1zHU4PRsSO4/kfClWUuEHO/N0AAAAASUVORK5CYII=']").click()
driver.find_element_by_xpath("//*[@id=\"FriendSelectorDialog\"]/div/div[2]/div/button").click()
