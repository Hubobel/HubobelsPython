from selenium import webdriver
from PIL import Image
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--start-maximized')

br = webdriver.Chrome(options=chrome_options)

br.set_window_size(1024, 1400)
br.get('https://www.hessenschau.de/wetter/wiesbaden/index.html')
br.refresh()
br.save_screenshot('Wetterscreenshot.png')
br.quit

im = Image.open("Wetterscreenshot.png")
area = (20, 600, 1600, 2500)
cropped_img = im.crop(area)

cropped_img.save('Wetterscreenshot2.png')


