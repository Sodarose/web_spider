# 一个简单的爬虫
import os
import re
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By

HTTP_PATTERN = r'(https?://\S+)'


# 创建一个webdriver
def create_edge_driver():
    service = EdgeService("MicrosoftWebDriver.exe")
    options = webdriver.EdgeOptions()
    options.use_chromium = True
    options.add_argument('--headless')
    options.add_argument('--disable-features=NetworkService')
    options.add_experimental_option('prefs', {'profile.default_content_setting_values.cookies': 2})
    return webdriver.Edge(service=service, options=options)


if __name__ == '__main__':
    # 启动一个edge模拟器
    driver = create_edge_driver()
    # 输入网址
    while True:
        url = input('请输入一个网址:')
        r = re.match(HTTP_PATTERN, url)
        if re.match('exit', url) is not None:
            driver.quit()
            print("爬虫关闭!")
            break
        if r is None:
            raise RuntimeError("无法通关检测，非正确网址!!!")
        driver.get(url)
        images = driver.find_elements(By.TAG_NAME, 'img')
        images_src = []
        for image in images:
            src = image.get_attribute('src')
            if re.match(HTTP_PATTERN, src) is not None:
                images_src.append(src)
        print(f'Found image: {images_src}')
